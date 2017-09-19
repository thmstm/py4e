#===============================================================================
# This programme reads an online JSON file from which it extracts the first
# "place_id", which uniquely identifies a place on Google Maps
#===============================================================================

# Importing libraries
import urllib.request, urllib.parse, urllib.error
import json

# Initialising
service_url = 'http://py4e-data.dr-chuck.net/geojson?'

# Asking user to input the source URL of the JSON data file
loc = input('Enter location: ')

# Concatinating the URL for the request
url = service_url + urllib.parse.urlencode({'address' : loc}) 
print('Retrieving', loc, 'here:', url)

# Opening connection to the JSON data file
uhandle = urllib.request.urlopen(url)
data = uhandle.read().decode()
print('Retrieved', len(data), 'characters')
 
# Transforming the text of the JSON file into a tree
try:
    tree = json.loads(data)
except:
    tree = None
 
# Finding the first "place_id" in the JSON data file
place_id = tree["results"][0]["place_id"]
 
# Printing the result
print('Place ID:', place_id)