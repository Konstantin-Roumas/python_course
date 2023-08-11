def has_char(string, letter_to_contain):
    index = 0
    output = False
    while index <= len(string) - 1:
        if string.strip()[index] == letter_to_contain.strip().lower() \
                or string.strip()[index] == letter_to_contain.strip().upper():
            output = True
            break
        else:
            index += 1
            continue
        break
    return output
