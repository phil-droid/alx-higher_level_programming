#!/usr/bin/python3

import MySQLdb
import sys

if __name__ "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    database=sys.argv[3]
    state_name=sys.argv[4]

    #connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database, port=3306)

    #create cursor to execute sql queries
    cursor=db.cursoror()

    #define the SQL query with a parameter for state name (safe from SQL injection)
    query = "SELECT cities.id, cities.name, states.name FROM cities \
         JOIN states ON cities.state_id = states.id \
         WHERE states.name = %s \
         ORDER BY cities.id ASC"
    #execute the query with the state name parameter (safe from SQL injection)
    cursor.execute(query, (state_name,))

    #fetch all the rows returned by the query
    rows=cursor.fetchall()

    cursor.close()
    db.close()
