#!/usr/bin/python3

"""I mistakenly ran the sql command multiple times, so i had like 20 entries
so i came up with this script to remove from 6 to 20, was cool
so i thought I leave it"""

import MySQLdb
import sys

# Make sure to provide the correct database credentials
db_config = {
    "host": "localhost",
    "user": sys.argv[1],  # Username
    "passwd": sys.argv[2],  # Password
    "db": sys.argv[3],  # Database name
    "port": 3306  # MySQL port (you can change it if needed)
}

try:
    # Connect to the database
    db = MySQLdb.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Define the range of IDs to delete (from 6 to 20)
    start_id = 6
    end_id = 20

    # Construct and execute the DELETE statement
    delete_query = f"DELETE FROM states WHERE id BETWEEN {start_id} AND {end_id}"
    cursor.execute(delete_query)

    # Commit the changes to the database
    db.commit()

    print(f"Deleted rows with id between {start_id} and {end_id}")

except MySQLdb.Error as e:
    print("MySQL Error:", e)

finally:
    # Close the database connection
    db.close()

