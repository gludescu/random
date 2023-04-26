"""
This Python script reads an input text file, counts the occurrences of each word, and outputs the results in a new text file, sorted by count in descending order.

To use this script, follow the steps below:

1. Ensure you have a valid input text file. Each word in the input text file should be separated by a space. Punctuation and capitalization may affect the word count, so consider preprocessing the text if necessary.
2. Replace the `input_file_name` variable in the `main()` function with the name (including the path, if necessary) of your input text file. For example: "path/to/your/input.txt".
3. Replace the `output_file_name` variable in the `main()` function with the desired name (including the path, if necessary) for the output text file. For example: "path/to/your/output.txt".
4. Run the script. The script will read the input text file, count the occurrences of each word, and write the sorted results to the specified output text file. The output will be formatted as follows:

    count1 word1
    count2 word2
    ...
    countN wordN

Example:

Suppose your input file ("input.txt") contains the following text:

    apple
    banana
    apple
    orange
    banana

The script will generate an output file ("output.txt") containing the following sorted word count:

    2 apple
    2 banana
    1 orange

Note that this script does not remove punctuation or handle capitalization, so preprocess the input text if necessary to ensure accurate word counts.
"""


def read_input_file(file_name):
    with open(file_name, "r") as input_file:
        content = input_file.read()
    return content.splitlines()


def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def sort_word_count(word_count):
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)


def write_output_file(file_name, sorted_word_count):
    with open(file_name, "w") as output_file:
        for word, count in sorted_word_count:
            output_file.write(f"{count} {word}\n")


def main():
    input_file_name = "input.txt"
    output_file_name = "output.txt"

    words = read_input_file(input_file_name)
    word_count = count_words(words)
    sorted_word_count = sort_word_count(word_count)
    write_output_file(output_file_name, sorted_word_count)


if __name__ == "__main__":
    main()
