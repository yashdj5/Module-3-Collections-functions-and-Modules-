# Sample dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sort in ascending order
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_asc)

# Sort in descending order
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
