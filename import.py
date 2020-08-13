# Program that imports data from a CSV spreadsheet and stores it in a relational DB using SQLite

import cs50
from sys import argv
import csv

# Database name variable
db_name = "students.db"

# Open DB
open(db_name, mode='w').close()
db = cs50.SQL(f'sqlite:///{db_name}')

# Create DB table
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth TEXT)")

# Check for correct number of command line arguements
if len(argv) != 2:
    print("Error: incorrect number of arguements. Try again.")

# Open csv file
with open(argv[1], mode='r') as csv_file:

    # Create dictionary reader
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    # Iterate through rows
    for row in csv_reader:

        # Parse name into seperate strings
        temp_name = row['name'].split()

        # Check for no middle name
        if len(temp_name) == 2:

            # Add NULL for middle name
            db.execute("INSERT INTO students (first, last, house, birth) VALUES(?, ?, ?, ?)",
                       temp_name[0], temp_name[1], row['house'], row['birth'])

        else:
            # Insert names into table
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       temp_name[0], temp_name[1], temp_name[2], row['house'], row['birth'])

print(db.execute("SELECT * FROM students"))