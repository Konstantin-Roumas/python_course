def filter_string(text, char):
    result = ''
    for current_char in text:
        if current_char.upper() != char.upper():
            result += current_char
    return result.strip()


print(filter_string('I look back if you are lost', 'i'))
