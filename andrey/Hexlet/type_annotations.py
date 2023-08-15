def letter_multiply(text: str, symbol: str, reptimes: int) -> str:
    text = text.replace(symbol, symbol * reptimes)
    return text


text1 = 'python'
print(letter_multiply(text1, 'p', 2))
print(letter_multiply(text1, 'y', 3))
print(letter_multiply(text1, 'n', 4))
