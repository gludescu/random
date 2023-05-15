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
