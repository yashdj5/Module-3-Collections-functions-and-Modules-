from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [''.join(combo) for combo in product(*data.values())]
print("Combinations:", combinations)
