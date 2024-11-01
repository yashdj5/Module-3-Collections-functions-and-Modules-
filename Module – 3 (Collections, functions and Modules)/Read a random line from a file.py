def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

# Replace 'sample.txt' with your filename
# print("Random line from file:", read_random_line('sample.txt'))
