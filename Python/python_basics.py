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

# In programming, data types refer to the different kinds of data that a program can work with. For example, a string

# is a data type that represents text, and an integer is a data type that represents a whole number. New programmers

# may sometimes mistake one data type for another, or may not understand the differences between them. For example,

# they may try to perform arithmetic on a string, or they may treat a boolean value as if it were an integer.

# Variables are used to store data in a program. For example, we might store a user's name in a variable called

# "username". New programmers may sometimes forget to declare a variable before using it, or may overwrite the value

# of a variable accidentally. For example, they might forget to initialize a variable before using it, or they might

# accidentally assign a new value to a variable that they meant to keep the original value of.

# Operators are used to perform operations on data. For example, we might use the "+" operator to add two numbers

# together. New programmers may sometimes use the wrong operator for a specific task, or may not understand the order

# of operations. For example, they might use the "+" operator to concatenate two strings instead of adding two numbers,

# or they might not realize that multiplication takes precedence over addition.

# Control structures are used to control the flow of a program. For example, an "if" statement might be used to execute

# some code only if a certain condition is true. New programmers may sometimes forget to include a necessary control

# structure, or may include unnecessary control structures that make the program more complicated than it needs to be.

# For example, they might forget to include an "else" statement to handle a case where the condition is false, or they

# might include a nested "if" statement when a simpler solution would suffice.

# Data structures are used to store and organize data in different ways. For example, a list is a data structure that

# can store multiple values in a single variable. New programmers may sometimes use the wrong data structure for a

# specific task, or may not understand how to access and manipulate data within a data structure. For example, they

# might use a list when a dictionary would be more appropriate, or they might not understand how to add or remove

# elements from a list.

# Sorting and searching are common algorithms used in programming. For example, we might use the "sorted()" function

# to sort a list of numbers in ascending order. New programmers may sometimes write inefficient sorting or searching

# algorithms, or may not understand how to optimize their code for performance. For example, they might use a bubble

# sort algorithm instead of a more efficient algorithm like quicksort, or they might not understand how to use binary

# search to find an element in a sorted list.

# Recursion is a programming technique where a function calls itself to solve a problem. For example, we might use

# recursion to compute the factorial of a number. New programmers may sometimes write recursive functions that never

# terminate, or may not understand how to properly manage the call stack. For example, they might forget to include a

# base case that will stop the recursion, or they might use too much memory by creating too many function calls on the

# call stack.

# Concurrency is the ability of a program to perform multiple tasks at the same time. For example, we might use

# threading to run two functions simultaneously. New programmers may sometimes write code that is not thread-safe,

# or may not understand how to manage shared resources. For example, they might create a race condition by

# accessing a shared variable from multiple threads without proper synchronization.

# Networking is the ability of a program to communicate with other programs over a network. For example, we might

# use sockets to send and receive data over the internet. New programmers may sometimes forget to handle errors

# that can occur during network communication, or may not understand how to properly format and parse data. For

# example, they might not handle network timeouts or connection errors, or they might not encode and decode data

# properly when sending and receiving it over the network.

# Data science is the application of programming and statistics to analyze and interpret data. For example, we

# might use pandas and numpy to manipulate and analyze data in Python. New programmers may sometimes struggle

# with data science concepts like statistics and machine learning, or may not understand how to use data science

# libraries effectively. For example, they might not understand how to perform basic statistical operations like

# mean and standard deviation, or they might not understand how to train and evaluate machine learning models.

# Overall, it's important for new programmers to have a solid understanding of these fundamental programming

# concepts in Python, and to take care to avoid common mistakes that can arise from misunderstandings or lack of

# experience. With practice and perseverance, however, anyone can become a skilled Python programmer!



# Importing necessary libraries

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


