#!/usr/bin/python3
#displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM `states` WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
