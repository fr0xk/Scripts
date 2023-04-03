- Object-oriented programming:

```python
# defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

# creating an object of the class
person1 = Person("John", 30)

# accessing object attributes and methods
print(person1.get_name())  # output: John
print(person1.get_age())  # output: 30
```

- Recursion:

```python
# defining a recursive function to calculate factorial

def factorial(n):

    if n == 0:

        return 1

    else:

        return n * factorial(n-1)

# calling the recursive function

print(factorial(5))  # output: 120
```

- Multithreading and multiprocessing:

```python
# using the threading module to run two tasks concurrently

import threading

def task1():

    print("Task 1 started")

    # do some work

    print("Task 1 completed")

def task2():

    print("Task 2 started")

    # do some work

    print("Task 2 completed")

# creating two threads to run the tasks concurrently

thread1 = threading.Thread(target=task1)

thread2 = threading.Thread(target=task2)

# starting the threads

thread1.start()

thread2.start()

# waiting for the threads to finish

thread1.join()

thread2.join()
```

- Decorators:

```python
# defining a decorator to measure the execution time of a function

import time

def measure_time(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Execution time: {end_time - start_time} seconds")

        return result

    return wrapper

# using the decorator to measure the execution time of a function

@measure_time

def fibonacci(n):

    if n < 2:

        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)

# calling the decorated function

print(fibonacci(10))
```

- Generator and iterators:

```python
# using a generator to generate even numbers

def even_numbers(n):

    for i in range(n):

        if i % 2 == 0:

            yield i

# iterating over the generator

for number in even_numbers(10):

    print(number)

# using an iterator to iterate over a list

my_list = [1, 2, 3, 4, 5]

my_iterator = iter(my_list)

print(next(my_iterator))  # output: 1

print(next(my_iterator))  #
```
