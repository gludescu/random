"""
This script compares two text files and outputs the matching and non-matching lines into separate files.

The compare_files function takes four arguments:
- file1: The first input file to be compared
- file2: The second input file to be compared
- output_match: The output file where matching lines will be written
- output_no_match: The output file where non-matching lines will be written

The function works as follows:

1. Opens both input files and reads their content into two sets, set1 and set2, while stripping any leading/trailing whitespace.
2. Calculates the intersection of the two sets (i.e., the matching lines) and stores it in matching_lines.
3. Calculates the symmetric difference of the two sets (i.e., the non-matching lines) and stores it in no_match_lines.
4. Opens the output_match file and writes the matching lines to it, one line at a time.
5. Opens the output_no_match file and writes the non-matching lines to it, one line at a time.

The if __name__ == '__main__': block sets the names of the input files and the output files, then calls the compare_files function with those file names.

Note: This script assumes that each line in the input files is unique. If there are duplicate lines within a file, they will be treated as a single entry when creating the sets.
"""

def compare_files(file1, file2, output_match, output_no_match):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        set1 = set(line.strip() for line in f1)
        set2 = set(line.strip() for line in f2)

    matching_lines = set1.intersection(set2)
    no_match_lines = set1.symmetric_difference(set2)

    with open(output_match, 'w') as match_file:
        for line in matching_lines:
            match_file.write(line + '\n')

    with open(output_no_match, 'w') as no_match_file:
        for line in no_match_lines:
            no_match_file.write(line + '\n')


if __name__ == '__main__':
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    output_match = 'matching_lines.txt'
    output_no_match = 'non_matching_lines.txt'

    compare_files(file1, file2, output_match, output_no_match)
