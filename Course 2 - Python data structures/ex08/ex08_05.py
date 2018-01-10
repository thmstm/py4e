fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

# Reading file line-by-line
for line in fh:
    line.rstrip()
    # Looking for lines starting with 'From'
    if line.startswith('From ') :
        # Splitting lines starting with 'From'
        ls = line.split()
        # Printing the second item (e-mail address) of the split
        print(ls[1])
        count = count + 1

# Printing the count of e-mail addresses
print("There were", count, "lines in the file with From as the first word")