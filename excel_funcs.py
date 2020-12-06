from string import ascii_lowercase

def excel_col_to_number(col):
    """
    Converts a column name (in letter form) to a number

    :param col: a column name like "A", "Y", "DBZ", etc.
    :return: the number corresponding to the column
    """

    num_equivalents = list()
    answer = 0

    # "ABC" => [1, 2, 3]
    for letter in col:
        num_equivalents.append((ascii_lowercase.index(letter.lower()) + 1))

    answer = 0

    for i, p in enumerate(reversed(num_equivalents)):
        if i == 0:
            answer += p
            continue

        answer += ((26 ** i) * p)

    return answer

if __name__ == '__main__':

    assert excel_col_to_number("XFD") == 16384, "Column XFD should be 16,384"