tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*tuple_list)
print("List 1:", list(list1))
print("List 2:", list(list2))
