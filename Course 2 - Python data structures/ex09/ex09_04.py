# Asking user to enter the source file
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
# Opening the source file
fhandle = open(fname)

# Creating a dictionary for the senders' e-mail addresses
sender = dict()

# Reading file line-by-line
for line in fhandle:
    line.rstrip()
    # Looking for lines starting with 'From'
    if line.startswith('From ') :
        # Splitting lines starting with 'From'
        ls = line.split()
        # Adding the second item (e-mail address) of the split if not yet in the dictionary and counting
        sender[ls[1]] = sender.get(ls[1], 0) + 1

# Selecting the most frequently occuring e-mail address and its count   
most_email = None
most_count = None
for email,count in sender.items():
    if most_count is None or count > most_count :
        most_email = email
        most_count = count

# Printing the most frequent e-mail address and its number of occurence
print(most_email, most_count)