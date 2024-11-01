def contains_sublist(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False

main_list = [1, 2, 3, 4, 5]
sublist = [2, 3]
print("Contains sublist:", contains_sublist(main_list, sublist))
