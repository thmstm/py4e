#===============================================================================
# This application will read roster data in JSON format, parse the file, and
# then produce an SQLite database that contains a User, Course, and Member
# table and populate the tables from the data file.
#===============================================================================

# Importing libraries
import json
import sqlite3

#--- Creating and connecting to database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#--- Initialising database
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#--- Asking user to input the JSON data file name and provide 'roster_data_sample.json' as a fallback
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

#--- The structure of the JSON object is the following:
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

#--- Opening and reading the file and putting it into a JSON object
str_data = open(fname).read()
json_data = json.loads(str_data)

#--- Looping through the JSON object
for entry in json_data:

    #--- Looking up the different data fields
    name = entry[0];
    title = entry[1];
    role = entry[2];

    #--- Printing the data field of the search result JSON object for the user
    print((name, title, role))

    #--- Updating the relevant tables with the data field of the search result JSON object
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    #--- Committing the changes
    conn.commit()
