def get_hidden_card(cardnumber, hiddensymbolscount=4):
    cardnumber = "*" * hiddensymbolscount + cardnumber[-4:]
    return cardnumber


print(get_hidden_card('1234563452353451', 5))
