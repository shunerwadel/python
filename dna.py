# Program to determine who DNA sample belongs to in a known database

from sys import argv
import csv


def main():

    # Check for correct number of command line arguements
    if len(argv) != 3:
        print("Error: incorrect number of arguements. Try again.")
        return(1)

    # Open database csv file
    with open(argv[1], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Get STR list
        STR = next(csv_reader)
        STR.pop(0)

        # Create temp database
        temp_db = []
        for row in csv_reader:
            temp_db.append(row)

        # Create variable lists
        seq = [0] * len(STR)
        seq_max = [0] * len(STR)

        # Open sequence file and read
        f = open(argv[2], 'r')
        sequence = f.read()

        # Declare variables
        i = 0

        # Check for sequences and consecutive repeats
        while i < len(sequence):
            j = 0
            while j < len(STR):
                seq_max[j] = seq_check(sequence, STR[j], i, seq[j], seq_max[j])
                j += 1
            i += 1

        # Check for match in database
        for entry in temp_db:

            # Create temp entry and convert to int
            temp_entry = list(map(int, entry[1:len(entry)]))
            ctr = 0

            # Check if first entry matches
            if temp_entry[0] == seq_max[0]:
                ctr += 1
                i = 1

                # Check subsequent entries
                while i < len(temp_entry):
                    if temp_entry[i] == seq_max[i]:
                        ctr += 1
                    i += 1

                # Print name of match
                if ctr == len(STR):
                    print(entry[0])
                    exit()

        # If no match
        print('No match.')


# Define function to check for STR sequences


def seq_check(sequence, check, i, seq, seq_max):
    j = i + len(check)

    # Check for initial STR match
    if sequence[i:j] == check:
        seq = 1

        # Check for repeating matches
        while j < len(sequence):
            i = j
            j = i + len(check)
            if sequence[i:j] == check:
                seq += 1
            else:
                break

        # Assign new repeating matches if greater
        if seq >= seq_max:
            seq_max = seq

    return seq_max


main()