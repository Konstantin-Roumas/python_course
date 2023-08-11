def get_age_difference(birthyear1: int, birthyear2: int):
    difference = abs(birthyear2 - birthyear1)
    result: str = f'The age difference is {abs(difference)}'
    return result


get_age_difference(2001, 2018)
