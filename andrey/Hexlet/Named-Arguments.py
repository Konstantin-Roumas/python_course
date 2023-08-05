def trim_and_repeat(text, offset=0, repetitions=1):
    text = text[offset:]
    text = text * repetitions
    print(text)
    return text


text1 = 'python'
trim_and_repeat(text1, offset=3, repetitions=2)
trim_and_repeat(text1, repetitions=3)
trim_and_repeat(text1)
