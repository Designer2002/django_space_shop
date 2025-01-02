from random import sample

def get_random_two(weapons):
    randnums = sample(range(0, len(weapons)), 2)
    return [weapons[randnums[0]], weapons[randnums[1]]]

