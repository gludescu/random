"""
This script reads a text file, sorts its lines alphabetically (ignoring case), removes duplicates, and writes the result to a new output file.

Usage:
1. Replace 'input.txt' in the input_file variable with the path to the file you want to process.
2. Replace 'output.txt' in the output_file variable with the path to the file you want to write the sorted, unique content to.
3. Run the script.

The script will read the contents of the input file, sort the lines alphabetically without distinguishing between uppercase and lowercase letters, remove any duplicate lines, and then write the sorted, unique lines to the output file.

Example:
Input file content:
    Apple
    orange
    Banana
    apple
    Orange

Output file content:
    Apple
    apple
    Banana
    Orange
    orange
"""


def sort_and_remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Sort lines alphabetically without considering case and remove duplicates
    sorted_unique_lines = sorted(set(lines), key=lambda x: x.strip().lower())

    # Write the sorted unique lines to the output file
    with open(output_file, 'w') as f:
        f.writelines(sorted_unique_lines)


if __name__ == "__main__":
    input_file = 'input.txt'  # Replace with the path to your input file
    output_file = 'output.txt'  # Replace with the path to your output file

    sort_and_remove_duplicates(input_file, output_file)
