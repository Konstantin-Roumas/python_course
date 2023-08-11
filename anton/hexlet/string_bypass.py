def my_substr(string, nmbr):
    index = 0
    output = ""
    while index <= nmbr - 1:
        output += string[index]
        index += 1
    return output
