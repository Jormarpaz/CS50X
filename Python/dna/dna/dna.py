import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python program_name.py <CSV_file> <DNA_sequence_file>")
        sys.exit(1)

    # Read database file into a variable
    csv_filename = sys.argv[1]
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            database = list(csv_reader)
    except FileNotFoundError:
        print("Error: CSV file not found.")
        sys.exit(1)

    # Read DNA sequence file into a variable
    dna_filename = sys.argv[2]
    try:
        with open(dna_filename, 'r') as dna_file:
            dna_sequence = dna_file.read()
    except FileNotFoundError:
        print("Error: DNA sequence file not found.")
        sys.exit(1)

    # Extract STR sequences from the first line of the CSV file
    str_sequences = database[0][1:]

    # Find longest match of each STR in DNA sequence
    str_counts = []
    for str_seq in str_sequences:
        str_counts.append(longest_match(dna_sequence, str_seq))

    # Check database for matching profiles
    for row in database[1:]:
        individual = row[0]
        profile = list(map(int, row[1:]))
        if profile == str_counts:
            print(individual)
            return

    # If no match is found
    print("No match.")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
