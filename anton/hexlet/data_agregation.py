def join_numbers_from_range(first, second):
    output = str(first)
    while first < second:
        first += 1
        output += str(first)
    return output
