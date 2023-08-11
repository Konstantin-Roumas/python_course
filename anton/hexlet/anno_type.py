def letter_multiply(string: str, symbol: str, inte: int) -> str:
    return string.strip().replace(symbol, symbol * inte)
