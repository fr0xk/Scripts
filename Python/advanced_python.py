# 1. Advanced Data Structures
def demonstrate_data_structures():
    # Dictionaries
    my_dict = {'name': 'Alice', 'age': 30}
    print(my_dict)

    # Sets
    my_set = {1, 2, 3}
    print(my_set)

    # Tuples
    my_tuple = (10, 20, 30)
    print(my_tuple)

# 2. Functional Programming
def demonstrate_functional_programming():
    # Lambda functions
    square = lambda x: x ** 2
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(square, numbers))
    print(squared_numbers)

# 3. Decorators
def my_decorator(func):
    def wrapper():
        print("Something before the function is called.")
        func()
        print("Something after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 4. Concurrency
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

def demonstrate_concurrency():
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 5. Database Interaction (using SQLite)
import sqlite3

def create_database():
    conn = sqlite3.connect('mydb.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# 6. Web Development (Flask example)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 7. Data Science (using pandas and matplotlib)
import pandas as pd
import matplotlib.pyplot as plt

def demonstrate_data_science():
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 22]}
    df = pd.DataFrame(data)
    df.plot(x='Name', y='Age', kind='bar')
    plt.show()

# Call the functions to demonstrate each topic
demonstrate_data_structures()
demonstrate_functional_programming()
say_hello()
demonstrate_concurrency()
create_database()
demonstrate_data_science()
  
