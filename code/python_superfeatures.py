# Example script to replace iterative tasks with Python features

# Original code with loop and if-else conditionals

numbers = [1, 2, 3, 4, 5]

sum = 0

for num in numbers:

    if num % 2 == 0:

        sum += num

print(sum)  # Output: 6

# Replaced with Python's built-in features

numbers = [1, 2, 3, 4, 5]

sum = sum(filter(lambda x: x % 2 == 0, numbers))

print(sum)  # Output: 6

# Using list comprehension to create a new list

numbers = [1, 2, 3, 4, 5]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)  # Output: [2, 4]

# Using ternary operator to assign value to a variable

num = 5

result = "even" if num % 2 == 0 else "odd"

print(result)  # Output: odd

# Using dictionary comprehension to create a new dictionary

old_dict = {'a': 1, 'b': 2, 'c': 3}

new_dict = {key: value*2 for key, value in old_dict.items()}

print(new_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

# Using set comprehension to create a new set

numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

unique_numbers = {num for num in numbers}

print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Using generators to generate a sequence of values

def fibonacci():

    a, b = 0, 1

    while True:

        yield a

        a, b = b, a + b

fib = fibonacci()

for i in range(10):

    print(next(fib))

# Output:

# 0

# 1

# 1

# 2

# 3

# 5

# 8

# 13

# 21

# 34

# Using lambda functions with map()

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using decorators to modify function behavior

def uppercase_decorator(function):

    def wrapper():

        func = function()

        make_uppercase = func.upper()

        return make_uppercase

    return wrapper

@uppercase_decorator

def hello():

    return "hello world"

print(hello())  # Output: HELLO WORLD

