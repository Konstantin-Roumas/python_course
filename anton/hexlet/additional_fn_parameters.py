def get_hidden_card(number, stars=4):
    star_number = "*" * stars
    return star_number + number.strip()[12:]
