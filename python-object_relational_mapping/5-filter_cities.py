#!/usr/bin/python3
"""Script that lists all cities of a given state, SQL-injection safe."""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cursor.close()
    db.close()
