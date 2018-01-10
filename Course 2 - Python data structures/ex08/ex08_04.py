# Opening the file
fname = input("Enter file name: ")
fh = open(fname)

# Defining the list to be built
lst = list()

# Reading the file line-by-line
for line in fh:
    # For each line, splitting the line into words
    line.rstrip()
    ls = line.split()
    # For each word checking if already being on the list and appending to it if not
    for word in ls:
        if word not in lst: lst.append(word)

# Sorting the list and printing
lst.sort()
print(lst)