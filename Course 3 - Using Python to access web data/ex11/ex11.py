# Importing the regex library
import re

# Asking user to enter the source file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"
# Opening the source file
fhandle = open(fname)

# Initialising the sum of the numbers
total = 0

# Reading file line-by-line
for line in fhandle:
    # Finding all the numbers as strings into listOfNums
    listOfNums = re.findall('([0-9]+)', line.rstrip())
    # If there is not any number in a line go to the next loop...
    if len(listOfNums) < 1 :
        continue
    else :
        # ... else looping through the list of numbers found...
        for snum in listOfNums :
            # ... and add up the converted numbers
            total = total + int(snum)

# Printing the sum of the numbers
print(total)
