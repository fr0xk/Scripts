"""
This script includes a simple 
example of concurrency using threading to 
count up and down simultaneously, 
a networking example that fetches the status 
code of Google's homepage using the 
requests library, and a data science 
example that fits a linear regression model 
to a set of data using the numpy, pandas, 
matplotlib, and scikit-learn libraries.
"""

import threading

import requests

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


# Data types and variables

x = 5

y = 3.14

z = "Hello, world!"

is_true = True

# Arithmetic operators

sum = x + y

difference = x - y

product = x * y

quotient = x / y

remainder = x % y

# Comparison operators

is_equal = x == y

is_greater = x > y

is_less_than_or_equal = x <= y

# If-else statement

if x > 10:

  print("x is greater than 10")

else:

  print("x is less than or equal to 10")

# Loops

for i in range(5):

  print(i)

i = 0

while i < 5:

  print(i)

  i += 1

# Functions

def add_numbers(a, b):

  return a + b

result = add_numbers(3, 4)

print(result)

# Lists, Tuples, and Sets

my_list = [1, 2, 3, 4]

my_tuple = (5, 6, 7, 8)

my_set = {9, 10, 11, 12}

# Dictionaries

my_dict = {"name": "John", "age": 30, "city": "New York"}

# Sorting

my_list.sort()

print(my_list)

# Searching

if 3 in my_list:

  print("3 is in the list")

# Recursion

def factorial(n):

  if n == 0:

    return 1

  else:

    return n * factorial(n-1)

result = factorial(5)

print(result)

# Concurrency

def count_up():

  for i in range(5):

    print("Counting up:", i)

def count_down():

  for i in range(5, 0, -1):

    print("Counting down:", i)

t1 = threading.Thread(target=count_up)

t2 = threading.Thread(target=count_down)

t1.start()

t2.start()

t1.join()

t2.join()

# Networking

response = requests.get("https://www.google.com")

print(response.status_code)

# Data Science

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

y = np.array([2, 4, 6, 8, 10])

reg = LinearRegression().fit(x, y)

print("Slope:", reg.coef_[0])

print("Intercept:", reg.intercept_)

plt.scatter(x, y)

plt.plot(x, reg.predict(x))

plt.show()

