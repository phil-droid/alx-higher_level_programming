#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username,passwd=password, db=database, port=3306)

    #Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM `states`")
    
    #Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    #Close the cursor and database connection
    cursor.close()
    db.close()
