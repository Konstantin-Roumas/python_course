def join_numbers_from_range(start, finish):
    i = start
    line = ''
    while i <= finish:
        line = line + str(i)
        i += 1
    print(line)
    return line


join_numbers_from_range(1, 3)

