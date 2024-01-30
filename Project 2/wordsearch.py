"""
CPE101
Spring 2021
Author: Jack Forrester
"""

def reverse_string(string: str) -> str:
    """reverses a given string
    Args:
        string (str): the string to be reversed
    Returns:
        r_str: the string with its characters reversed
    """

    str_len = len(string)
    i = 0
    r_str = ''
    while i < str_len:
        char = string[str_len - 1 - i]
        r_str += char
        i += 1
    return r_str


def transpose_string(string: str, row_len: int) -> str:
    """Transposes the characters of a given string
    Args:
        string (str): the string to be transposed
        row_len: the length of a row in the wordsearch puzzle
    Returns:
        tsp_str: a new string with the string's characters transposed
    """

    str_len = len(string)
    column = 0
    tsp_str = ''
    while column < row_len:
        row = 0
        c_str = ''
        while row < str_len:
            char = string[column + row]
            c_str += char
            row += row_len
        column += 1
        tsp_str += c_str
    return tsp_str


def find_word_forward(puzzle: str, word: str, row_len: int) -> str:
    """Checks for and finds a word oriented forwards in given wordsearch string
    Args:
        puzzle (str): the wordsearch puzzle string
        word (str): the word to be found oriented forwards in the puzzle
        row_len (int): the length of a row
    Returns:
        the row number and column number of the first character of the word
        when oriented forwards
    """

    puz_len = len(puzzle)
    i = 0
    while i < puz_len:
        puz = puzzle[i:i + row_len]
        if puz.find(word) != -1:
            break
        i += row_len
    if puz.find(word) != -1:
        row = round(i / row_len)
        column = puz.find(word)
        return f"{word}: (FORWARD) row: {row} column: {column}"


def find_word_backward(puzzle: str, word: str, row_len: int) -> str:
    """Checks for and finds a word oriented backwards in given wordsearch
    string
    Args:
        puzzle (str): the wordsearch puzzle string
        word (str): the word to be found oriented backwards in the puzzle
        row_len (int): the length of a row
    Returns:
        the row number and column number of the first character of the word
        when oriented backwards
    """

    puz_len = len(puzzle)
    r_puz = reverse_string(puzzle)
    i = 0
    while i < puz_len:
        puz = r_puz[puz_len - row_len - i:puz_len - i]
        if puz.find(word) != -1:
            break
        i += row_len
    if puz.find(word) != -1:
        row = round(i / row_len)
        column = row_len - 1 - puz.find(word)
        return f"{word}: (BACKWARD) row: {row} column: {column}"


def find_word_down(puzzle: str, word: str, row_len: int) -> str:
    """Checks for and finds a word oriented downwards in given wordsearch
    string
    Args:
        puzzle (str): the wordsearch puzzle string
        word (str): the word to be found oriented downwards in the puzzle
        row_len (int): the length of a row
    Returns:
        the row number and column number of the first character of the word
        when oriented downwards
    """

    puz_len = len(puzzle)
    tsp_puz = transpose_string(puzzle, row_len)
    col_num = puz_len // row_len
    i = 0
    while i < row_len:
        puz = tsp_puz[(col_num * i):col_num + (col_num * i)]
        if puz.find(word) != -1:
            break
        i += 1
    if puz.find(word) != -1:
        row = puz.find(word)
        column = i
        return f"{word}: (DOWN) row: {row} column: {column}"


def find_word_up(puzzle: str, word: str, row_len: int) -> str:
    """Checks for and finds a word oriented upwards in given wordsearch string
    Args:
        puzzle (str): the wordsearch puzzle string
        word (str): the word to be found oriented upwards in the puzzle
        row_len (int): the length of a row
    Returns:
        the row number and column number of the first character of the word
        when oriented upwards
    """

    puz_len = len(puzzle)
    col_num = puz_len // row_len
    tsp_puz = transpose_string(puzzle, row_len)
    rnt_puz = reverse_string(tsp_puz)
    i = 0
    while i < row_len:
        puz = rnt_puz[puz_len - col_num - (i * col_num):puz_len - (i * col_num)]
        if puz.find(word) != -1:
            break
        i += 1
    if puz.find(word) != -1:
        row = col_num - 1 - puz.find(word)
        column = i
        return f"{word}: (UP) row: {row} column: {column}"


def find_word(puzzle: str, word: str, row_len: int) -> str:
    """Finds all index locations and orientations of a given word in the
    wordsearch puzzle
    Args:
        puzzle (str): the wordsearch puzzle string
        word (str): the word to be found in the puzzle
        row_len (int): the length of a row
    Returns:
        the row number and column number of the first character of the word and
        its orientation
    """

    if find_word_forward(puzzle, word, row_len) is not None:
        return find_word_forward(puzzle, word, row_len)
    if find_word_backward(puzzle, word, row_len) is not None:
        return find_word_backward(puzzle, word, row_len)
    if find_word_down(puzzle, word, row_len) is not None:
        return find_word_down(puzzle, word, row_len)
    if find_word_up(puzzle, word, row_len) is not None:
        return find_word_up(puzzle, word, row_len)
    return f"{word}: word not found"


def display_puzzle(puzzle: str, row_len: int) -> str:
    """Displays the wordsearch puzzle
    Args:
        puzzle (str): the string of letters in the wordsearch puzzle
        row_len (int): the length of a row
    Returns:
        display: a display of the wordsearch string oriented so that a new row
        is created after the amount of characters specified
    """

    puz_len = len(puzzle)
    i = 0
    display = ''
    while i < puz_len:
        puz = puzzle[i:i + row_len]
        i += row_len
        display += puz
        if i == puz_len:
            break
        display += '\n'
    return display


def find_nth(string, word, nth):
    """Finds the nth occurance of a substring in a given string
    Args:
        string (str): the entire string
        word (str): the substring
        nth (int): the ocurrance number
    Returns:
        start: the index number of the first character in the nth occurance of
        the substring
    """

    start = string.find(word)
    word_len = len(word)
    while start >= 0 and nth > 1:
        start = string.find(word, start + word_len)
        nth -= 1
    return start


def main():
    """Executes a wordsearch for the given string and words to find
    """

    puzzle_i = input("Enter a puzzle line: ")
    puzzle = puzzle_i.strip()
    row_len = 10
    word_i = input("Enter words to search: ")
    word = word_i.strip()
    print(display_puzzle(puzzle, row_len))
    num = word.count(' ')
    if word.find(' ') != -1:
        space1 = word.find(' ')
        print(find_word(puzzle, word[:space1], row_len))
        i = 2
        if num == 1:
            print(find_word(puzzle, word[space1 + 1:], row_len))
        else:
            while i <= num:
                space = find_nth(word, ' ', i)
                prev_space = find_nth(word, ' ', i-1)
                next_word = word[prev_space + 1:space]
                print(find_word(puzzle, next_word, row_len))
                i += 1
            final_space = find_nth(word, ' ', num)
            print(find_word(puzzle, word[final_space + 1:], row_len))
    else:
        print(find_word(puzzle, word, row_len))


if __name__ == "__main__":
    main()
