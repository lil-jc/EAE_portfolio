import csv
from sys import argv, exit


def main():

    # TODO: Check for command-line usage
    if (len(argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # TODO: Read database file into a variable
    csv_path = argv[1]
    csv_file = open(csv_path)
    reader = csv.reader(csv_file)
    # store sequences in viarable
    all_sequences = next(reader)[1:]

    # TODO: Read DNA sequence file into a variable
    txt_path = argv[2]
    with open(txt_path) as txt_file:
        s = txt_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    actual = []
    for sub_seq in all_sequences:
        num = longest_match(s, sub_seq)
        actual.append(num)

    # TODO: Check database for matching profiles
    print_match(reader, actual)


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


# funtion to print matched person
def print_match(reader, actual):
    for line in reader:
        person = line[0]
        # store dna repeat sequence of a person in viarable
        values = []
        for val in line[1:]:
            values.append(int(val))
        # compare dna repeat sequence to argv[2]'s dna repeat sequence
        if values == actual:
            print(person)
            return
    print("No match")


main()
