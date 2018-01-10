# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        snumt = line[20:]
        snum = snumt.strip()
        num = float(snum)
        total = total + num
        count = count + 1
avg = total / count
print("Average spam confidence:",avg)
