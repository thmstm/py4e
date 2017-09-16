# This program scrapes a website for numbers and returns their count and sum.

# Importing
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Initialising the count and total
count = 0
total = 0

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking user to input the URL
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()

# Creating an organised string (soup) with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Trying to convert the tag's content into integer
    try:
        total = total + int(tag.contents[0])
        count = count + 1
    except:
        continue

# Printing the results
print('Count',count)
print('Sum',total)