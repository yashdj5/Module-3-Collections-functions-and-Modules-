my_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 2)
repeated_items = set([item for item in my_tuple if my_tuple.count(item) > 1])
print("Repeated items:", repeated_items)
