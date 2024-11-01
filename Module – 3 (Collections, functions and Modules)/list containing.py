def get_unique_elements(input_list):
    # Use a set to remove duplicates and convert it back to a list
    unique_list = list(set(input_list))
    return unique_list

# Example usage
sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_elements = get_unique_elements(sample_list)
print("Unique elements:", unique_elements)
