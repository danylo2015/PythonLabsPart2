def read_file(filename_in):
    dict_of_words = {}
    list_of_words = []
    try:
        with open(f"E:\\PythonLabsPart2\\tests\\resources\\{filename_in}", "r", encoding="utf-8") as wchain_in:
            # Read the first line to get the number of words
            first_line = wchain_in.readline().strip()

            if not first_line:
                # If the first line is empty (no data in the file), return empty results
                return dict_of_words, list_of_words

            num_of_word = int(first_line)

            for _ in range(num_of_word):
                word = wchain_in.readline().strip()
                dict_of_words[word] = 1
                list_of_words.append(word)

    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{filename_in}' not found.")
        return dict_of_words, list_of_words

        # Sort the list of words by length
    list_of_words.sort(key=len)
    return dict_of_words, list_of_words


def check_word_for_another_word(shorter_word: str, longer_word: str):
    longer_word_idx = 0
    for i in range(len(shorter_word)):
        if longer_word_idx == i - 1 and i != 0:
            longer_word_idx = i
        if shorter_word[i] != longer_word[longer_word_idx]:
            longer_word_idx += 1
            if shorter_word[i] != longer_word[longer_word_idx]:
                return False
    return True


def find_max_sequence_words(words_dict: dict[str:int], word_list: list[str]):
    if len(word_list) == 0:
        return 0
    else:
        for short_word in word_list:
            for long_word in word_list:
                if len(long_word) >= len(short_word) + 1:
                    if check_word_for_another_word(short_word, long_word):
                        words_dict[long_word] = words_dict[short_word] + 1
        print(words_dict)
        return max(words_dict.values())


def write_output_file(filename_in, filename_out):
    dict_of_words, list_of_words = read_file(filename_in)
    with open(f"E:\\PythonLabsPart2\\tests\\resources\\{filename_out}", "w", encoding="utf-8") as wchain_out:
        wchain_out.write(str(find_max_sequence_words(dict_of_words, list_of_words)))
