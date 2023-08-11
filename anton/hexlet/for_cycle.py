def filter_string(string, char):
    output = ""
    for item in string:
        if item != char.upper() and item != char.lower():
            output += item
    return output.strip()
