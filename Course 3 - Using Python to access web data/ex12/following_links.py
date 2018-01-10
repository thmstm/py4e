# This program follows links at a given position for a given number of times and lists the resulting chain

# Importing
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Initialising the count and total
name = list()

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking user to input parameters
url = input('Enter URL: ')
pos_str = input('Scanning for a tag that is at the following position relative to the first name in the list: ')
rep_str = input('Repeating the process to follow the link for the following number of times: ')

# Converting the inputs
position = int(pos_str)
repeat = int(rep_str)

# Looping through the layers of webpages 4 times
for repeat in range(repeat):
    # Reading the whole fine into a single long string
    html = urlopen(url, context=ctx).read()
    
    # Creating an organised string (soup) with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieving all of the 'a' tags
    tags = soup('a')
    
    # Adding the name of the person at the given position to the list
    name.append(tags[position-1].contents[0])
    
    # Updating the URL for the next loop
    url = tags[position-1].get('href', None)

# Printing the list with the names
print(name)