#!/usr/bin/python3
"""
This module connects to a MySQL database and
retrieves all states beginning with N
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
    cursor.execute("SELECT * FROM states WHERE
                   BINARY name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(username, password, db_name)
