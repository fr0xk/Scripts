Imperative:

def calculate_sum():
  even_numbers = []
  for num in range(2, 101, 2):
    even_numbers.append(num)

  filtered_numbers = []
  for num in even_numbers:
    if num % 3 != 0:
      filtered_numbers.append(num)

  total_sum = 0
  for num in filtered_numbers:
    total_sum += num

  print(total_sum)

calculate_sum()

Non Imperative:

# Generate a list of even numbers from 2 to 100
# range(start, stop, step) creates a sequence of numbers
# list() converts the sequence into a list
even_numbers = list(range(2, 101, 2))

# Filter out multiples of 3 using a lambda function
# filter(function, iterable) creates an iterator yielding elements of iterable for which function(element) is True
# lambda num: num % 3 != 0 is an anonymous function that returns True if num is not divisible by 3
# list() converts the iterator into a list
filtered_numbers = list(filter(lambda num: num % 3 != 0, even_numbers))

# Calculate the sum using the built-in sum() function
# sum(iterable) calculates the sum of numbers in the iterable
total_sum = sum(filtered_numbers)

print(f"Total sum of even numbers (excluding multiples of 3): {total_sum}")
