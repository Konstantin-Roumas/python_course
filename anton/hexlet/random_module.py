from random import randint


def choice_from_range(string, b_index, e_indiex):
    generated_index = randint(b_index, e_indiex)
    return string[generated_index]
