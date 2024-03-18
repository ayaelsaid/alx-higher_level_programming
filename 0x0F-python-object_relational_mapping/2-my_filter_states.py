#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

# code should not be executed when imported
if __name__ == '__main__':

    # make a connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # get the state_name
    state_name = argv[4]
    # Create a cursor object
    cursor = db.cursor()
    # execute sql query
    cursor.execute("SELECT * FROM states WHERE name = '{}' \
            ORDER BY states.id ASC".format(state_name))
    # Fetch all rows
    allrows = cursor.fetchall()
    # display rows
    for row in allrows:
        print(row)
    # close all
    cursor.close()
    db.close()
