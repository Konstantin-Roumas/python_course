import random


def choice_from_range(text, start_index, end_index):
    if start_index < end_index < len(text):
        random_index = random.randint(start_index, end_index)
        result = text[random_index]
        return result
    else:
        print('incorrect indexes')


print(choice_from_range('abcdefghijk', 1, 10))
