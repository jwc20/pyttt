def insert_char_every_n(original_string, char_to_insert, n):
    new_string = []
    for i, char in enumerate(original_string):
        new_string.append(char)
        if (i + 1) % n == 0 and (i + 1) != len(original_string):
            new_string.append(char_to_insert)
    return "".join(new_string)