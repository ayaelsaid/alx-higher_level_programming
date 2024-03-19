#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

# code should not be executed when imported
if __name__ == '__main__':

    # make a connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    state_name = argv[4]
    # Create a cursor object
    cursor = db.cursor()
    # execute sql query
    cursor.execute("SELECT cities.name \
      FROM cities \
      INNER JOIN states ON cities.state_id = states.id \
      WHERE states.name = %s \
      ORDER BY cities.id ASC", (state_name,))
    # Fetch all rows
    allrows = cursor.fetchall()
    # display rows
    city_names = [row[0] for row in allrows]
    print(", ".join(row), end="")
    # close all
    cursor.close()
    db.close()
