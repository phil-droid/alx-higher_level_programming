#!/usr/bin/python3
#lists all cities in the databasse

import MySQLdb
import sys

if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    database=sys.argv[3]

    # create a connection to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, port=3306)

    # create a cursor to execute SQL queries
    cursor = db.cursor()
    
    # define the SQL query
    query = "SELECT * FROM cities ORDER BY id ASC"
    
    
    # execute the query
    cursor.execute(query)

    # fetch all the rows returned by the query
    rows = cursor.fetchall()

    # print each row
    for row in rows:
        print(row)

    # close the cursor and database connection
    cursor.close()
    db.close()
