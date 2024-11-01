tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 100
modified_list = [t[:-1] + (new_value,) for t in tuple_list]
print("Modified list of tuples:", modified_list)
