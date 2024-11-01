# Generate a list of squares of numbers from 1 to 30
squares = [i**2 for i in range(1, 31)]

# Get the first and last 5 elements from the list
result = squares[:5] + squares[-5:]

# Print the result
print("First and last 5 elements of the list:", result)
