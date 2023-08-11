def sort_pair(pair):
    (first, second) = pair
    if first > second:
        pair = (second, first)
    return pair


print(sort_pair((4, 5)))
