#===============================================================================
# This project uses the Google GeoCoding API to retrieve data and then uses
# Google Maps to visualize the data.
# This part of the project reads the data from a database and writed the
# parts into a javascript file for future visualisation.
#===============================================================================

#--- Importing libraries
import sqlite3
import json
import codecs

#--- Opening connection to the SQLite database
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

#--- Reading everything from the database into the cursor
cur.execute('SELECT * FROM Locations')

#--- Opening javascript file for writing data for visualisation
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

#--- Looping through all the data read from the database
for row in cur :
    #--- Transforming and loading the data into a JSON object
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    #--- Checking if the status is all right
    if not('status' in js and js['status'] == 'OK') : continue

    #--- Getting the latitude, longitude and the formatted address
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    
    #--- Printing the latitude, longitude and the formatted address
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

#--- Finishing writing into the javascript file and closing the file
fhand.write("\n];\n")
cur.close()
fhand.close()

#--- Printing the number of records written into the javascript file and a message
#--- to continue with visualisation of the data in 'where.html'
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

