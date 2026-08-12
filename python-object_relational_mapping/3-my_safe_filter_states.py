#!/usr/bin/python3
"""Script that safely displays states matching a user-provided name."""
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
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
