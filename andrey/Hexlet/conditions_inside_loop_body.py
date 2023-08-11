def has_char(string, char):
    i = 0
    while i < len(string):
        if string[i].lower() == char.lower():
            return True
        else:
            i += 1
    return False


print(has_char('Hexlet', 'H'))  # => True
print(has_char('Hexlet', 'h'))  # => True
print(has_char('Awesomeness', 'd'))  # => False
