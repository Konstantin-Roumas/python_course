def trim_and_repeat(string, offset=0, repetitions=1):
    string = string.strip()[offset:]
    string = string * repetitions
    return string
