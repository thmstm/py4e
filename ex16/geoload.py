#===============================================================================
# This project uses the Google GeoCoding API to retrieve data and then uses
# Google Maps to visualize the data.
# This part of the project reads the data from a file, requests geocode of
# the read location from the Google Maps Geocoding API and writes the results
# into a database.
#===============================================================================

#--- Importing libraries
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

#--- Initialising
api_key = 'AIzaSyD9z8vvTzJzjSbTXyR082e7BzUWQsimj-w' #False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?" #place/textsearch/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

#--- Opening connection to the SQLite database
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

#--- Initialising database
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

#--- Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#--- Opening connection to the data file
fh = open("where.data")
count = 0
#--- Looping through the data file by 200 lines at a time
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    #--- Getting the geodata of the address from the database
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    #--- ... and printing message if geodata is already in the database
    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    #--- Constructing the encoded URL using the address and the API key
    parms = dict()
    parms["address"] = address #parms["query"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    #--- Printing the URL for the user's convenience
    print('Retrieving', url)
    
    #--- Submitting the service request by opening the URL
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #--- Printing the first 20 characters of the result
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    #--- Loading the received result in as JSON object or printing an error message
    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    #--- Printing an error message if something is wrong with the status
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    #--- Adding the received result into the SQLite database
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    
    #--- Adding a delay at every 10 request
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(1)

#--- Printing a message at the end to continue with dumping the data using 'geodump.py'
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
