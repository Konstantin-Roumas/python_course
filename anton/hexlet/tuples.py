def sort_pair(input):
    (arg1, arg2) = input
    if arg2 < arg1:
        input = (arg2, arg1)
    return input
