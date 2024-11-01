def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)

print("Sum of divisors of 12:", sum_of_divisors(12))
