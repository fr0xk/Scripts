# 1. Introduction to Python
print("Welcome to the Python programming course!")

# 2. Functions and Variables
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 3. Conditionals and Loops
def check_age(age):
    if age >= 18:
        print("You're an adult.")
    else:
        print("You're a minor.")

check_age(20)

# 4. Exceptions and Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# 5. Unit Testing
def add(a, b):
    return a + b

assert add(2, 3) == 5

# 6. Libraries and Modules
import random
print(f"Random number: {random.randint(1, 10)}")

# 7. File I/O
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")

# 8. Regular Expressions
import re
pattern = r"\b\w{5}\b"
text = "Python is amazing"
matches = re.findall(pattern, text)
print(matches)

# 9. Classes and Objects
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}!")

alice = Person("Alice")
alice.greet()

# 10. Conclusion
print("Congratulations! You've covered essential Python topics.")

# Additional exercises and challenges: Encourage students to build small projects!
