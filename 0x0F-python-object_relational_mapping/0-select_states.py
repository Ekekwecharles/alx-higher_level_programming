#!/usr/bin/python3
"""
lists all states from the
database `hbtn_0e_0_usa`. order_by id in ASC
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connect and retrieve from a database.
    """
    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
