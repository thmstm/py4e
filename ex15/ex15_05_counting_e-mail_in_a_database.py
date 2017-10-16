#===============================================================================
# This programme reads an offline txt file and counts the number of email
# messages per organization (i.e. domain name of the email address) using
# a database to maintain the counts.
#===============================================================================

# Importing libraries
import sqlite3

#--- Creating and connecting to database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#--- Initialising database
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
 
#--- Asking user to input the data file name and provide 'mbox.txt' as a fallback
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
 
#--- Opening and reading the file
fh = open(fname)
for line in fh:
    #--- Skipping the irrelevant lines
    if not line.startswith('From: '): continue
    #--- Splitting the lines, taking the split with the e-mail, then splitting the e-mail to get the domain
    email = line.split()[1]
    domain = email.split('@')[1]
    #--- Getting the current count value from the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    #--- If the e-mail is not yet in the database, then add it...
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    #--- ... else update the count value in the database
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
#--- Commit changes to the database
conn.commit()
 
#--- Querying the results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#--- Closing connection with the database
cur.close()
