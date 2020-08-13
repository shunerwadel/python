# Program to print list of students from relational DB given command line argument criteria

from sys import argv
import cs50

db_name = "students.db"

# Open DB
open(db_name, mode='r').close()
db = cs50.SQL(f'sqlite:///{db_name}')

# Check for correct number of command line arguements
if len(argv) != 2:
    print("Error: incorrect number of arguements. Try again.")
    exit()

# Define dictionary
matching_students = {}

# Check if student in house and extract name and birth year
matching_students = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house = '{argv[1]}' ORDER BY last, first")

# Print in correct format
for entry in matching_students:

    # Handle no middle name
    if entry['middle'] == None:
        print(entry['first'] + " " + entry['last'] + "," + " born " + entry['birth'])

    # Handle middle name
    else:
        print(entry['first'] + " " + entry['middle'] + " " + entry['last'] + "," + " born " + entry['birth'])
