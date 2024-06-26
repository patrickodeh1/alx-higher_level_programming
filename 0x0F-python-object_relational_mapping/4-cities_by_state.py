#!/usr/bin/python3

"""
module that connects to database
and lists all cities.
"""
import sys
import MySQLdb


def list_cities(username, password, db_name):
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
    )
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states On cities.state_id = states.id
        ORDER BY cities.id ASC
    """

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

    list_cities(username, password, db_name)
