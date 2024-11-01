def second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None

sample_list = [5, 1, 3, 2, 4, 1, 5]
print("Second smallest number:", second_smallest(sample_list))
