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
