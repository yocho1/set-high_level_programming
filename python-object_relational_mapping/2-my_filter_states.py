#!/usr/bin/python3
"""Script that displays states matching a user-provided name."""
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
    query = ("SELECT * FROM states WHERE name = BINARY '{}' "
             "ORDER BY states.id ASC")
    cursor.execute(query.format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
