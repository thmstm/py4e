# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
ftext = fh.read()
ftext = ftext.strip()
print(ftext.upper())