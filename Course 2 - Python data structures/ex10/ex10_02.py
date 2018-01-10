# Asking user to enter the source file
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
# Opening the source file
fhandle = open(fname)

# Creating a dictionary for the hours
hours = dict()

# Reading file line-by-line
for line in fhandle:
    line.rstrip()
    # Looking for lines starting with 'From'
    if line.startswith('From ') :
        # Splitting lines starting with 'From'
        ls = line.split()
        # Taking the split with the time
        time = ls[5]
        # Splitting the time
        tm = time.split(':')
        # Taking the split with the hour
        hour = tm[0]
        # Adding the hour in the dictionary and counting
        hours[hour] = hours.get(hour, 0) + 1

# Printing the hours and their counts in ascending order by hours
for k,v in sorted(hours.items()):
    print(k,v)