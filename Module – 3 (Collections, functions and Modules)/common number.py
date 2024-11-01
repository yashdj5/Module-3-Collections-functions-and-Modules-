def have_common_member(list1, list2):
    return any(item in list1 for item in list2)

# Example usage
if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    list_b = [4, 5, 6]
    list_c = [7, 8, 9]

    print("List A and List B have common members:", have_common_member(list_a, list_b))  # True
    print("List A and List C have common members:", have_common_member(list_a, list_c))  # False
    
