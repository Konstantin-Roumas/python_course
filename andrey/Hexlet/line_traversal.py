def my_substr(string, numb):
    i = 0
    result = ''
    while i < numb:
        result += string[i]
        i += 1
    print(result)


my_substr('dddeeeaaattthhh', 6)
