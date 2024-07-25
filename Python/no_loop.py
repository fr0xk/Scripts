# Generate a list of even numbers from 2 to 100
even_numbers = list(range(2, 101, 2))

# Filter out multiples of 3 using a lambda function
filtered_numbers = list(filter(lambda num: num % 3 != 0, even_numbers))

# Calculate the sum using the built-in sum() function
total_sum = sum(filtered_numbers)

print(f"Total sum of even numbers (excluding multiples of 3): {total_sum}")
