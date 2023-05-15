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
