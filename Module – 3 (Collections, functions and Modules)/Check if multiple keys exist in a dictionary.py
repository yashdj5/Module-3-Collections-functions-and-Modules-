def check_multiple_keys(dictionary, keys):
    return all(key in dictionary for key in keys)

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'c']
print("All keys exist:", check_multiple_keys(my_dict, keys_to_check))
