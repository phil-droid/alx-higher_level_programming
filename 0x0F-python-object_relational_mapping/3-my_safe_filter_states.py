#!/usr/bin/python3
#displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

import MySQLdb
import sys

# take in 4 arguments: username, password, database name, and state name to search
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# create a connection to the MySQL server running on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# create a cursor to execute SQL queries
cursor = db.cursor()

# define the SQL query
query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

# execute the query with the state name parameter (safe from MySQL injection)
cursor.execute(query, (state_name,))

# fetch all the rows returned by the query
rows = cursor.fetchall()

# print each row
for row in rows:
    print(row)

# close the cursor and database connection
cursor.close()
db.close()
