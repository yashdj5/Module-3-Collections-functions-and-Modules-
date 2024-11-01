def check_key_exists(dictionary, key):
    return key in dictionary

my_dict = {'a': 1, 'b': 2}
key_to_check = 'a'
print("Key exists:", check_key_exists(my_dict, key_to_check))
