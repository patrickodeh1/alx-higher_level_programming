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
        SELECT cities.name
        FROM cities
        JOIN states On cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    list_cities(username, password, db_name)
