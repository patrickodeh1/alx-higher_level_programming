#!/usr/bin/python3
"""
This module connects to a MySQL database
"""
import sys
import MySQLdb


def list_states(username, password, db_name):
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}%'".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    list_states(username, password, db_name)
