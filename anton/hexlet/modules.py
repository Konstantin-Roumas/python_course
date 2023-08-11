from symbols import is_vowel


def count_vowels(string):
    counter = 0
    for symbol in string:
        if is_vowel(symbol) == True: #linter asks to use is but tests with is not working idk
            counter += 1
        else:
            continue
    return counter
