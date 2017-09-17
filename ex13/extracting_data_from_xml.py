# This programme reads an online XML file from which it extracts the values of the <count> tags and sums those values

# Importing libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# Initialising
total_count = 0

# Asking user to input the source URL of the XML data file
url = input('Enter URL: ')
uhandle = urllib.request.urlopen(url)
data = uhandle.read()

# Transforming the text of the XML file to a tree
tree = ET.fromstring(data)

# Finding all the <comment> tags and putting them into a list
counts_str = tree.findall('.//count')

# Looping through all the <count> nodes
for count_str in counts_str:
    # Converting the text of the <count> nodes into an integer and summing
    try:
        total_count = total_count + int(count_str.text)
    except:
        continue

# Printing the result
print('Receiving',len(data),'characters')
print('Count:',len(counts_str))
print('Sum:',total_count)