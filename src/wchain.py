def read_file(filename_in):
    list_of_words = []
    try:
        with open(f"../resources/{filename_in}", "r", encoding="utf-8") as wchain_in:
            # Reading the first line to get the number of words
            first_line = wchain_in.readline().strip()

            if not first_line:
                # If the first line is empty (no data in the file), return empty results
                return list_of_words

            num_of_word = int(first_line)

            for _ in range(num_of_word):
                word = wchain_in.readline().strip()
                list_of_words.append(word)

    except FileNotFoundError:
        # Handling file not found error
        return list_of_words

        # Sorting the list of words by length
    list_of_words.sort(key=len)
    return list_of_words


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


def find_max_sequence_words(word_list: list[str]):
    if len(word_list) == 0:
        return 0
    else:
        # Initializing a DP table with all 1s
        dp = [1] * len(word_list)
        # Sorting the word list by length
        word_list.sort(key=len)

        for i in range(len(word_list)):
            for j in range(i):
                # If the shorter word can be formed from the longer word
                # and the sequence ending with the longer word can be extended
                if len(word_list[i]) == len(word_list[j]) + 1 and check_word_for_another_word(word_list[j], word_list[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        # The maximum sequence of words is the maximum value in the DP table
        return max(dp)


def write_output_file(filename_in, filename_out):
    list_of_words = read_file(filename_in)
    with open(f"../resources/{filename_out}", "w", encoding="utf-8") as wchain_out:
        wchain_out.write(str(find_max_sequence_words(list_of_words)))
