from typing import List, Dict

# Define a list of numbers

numbers = [1, 2, 3, 4, 5]

# Define a function that takes a list of numbers and returns their sum

def sum_numbers(numbers: List[int]) -> int:

    """Return the sum of a list of numbers."""

    return sum(numbers)

# Define a function that takes a dictionary of user data and returns their full name

def get_full_name(user_data: Dict[str, str]) -> str:

    """Return the full name of a user given their data dictionary."""

    return f"{user_data['first_name']} {user_data['last_name']}"

# Define a function that takes a list of user data and prints their full names

def print_user_names(users: List[Dict[str, str]]) -> None:

    """Print the full names of a list of users."""

    for user in users:

        print(get_full_name(user))

# Define a function that takes a list of numbers and returns the maximum value

def get_max_number(numbers: List[int]) -> int:

    """Return the maximum value in a list of numbers."""

    return max(numbers)

# Define a function that takes user data and adds them to a database

def add_user_to_database(user_data: Dict[str, str]) -> None:

    """Add a user's data to a database."""

    # TODO: Add code to insert user data into database

    pass

# Use functional programming to calculate the sum of the numbers

total = sum_numbers(numbers)

print(f"The sum is: {total}")

# Use functional programming to get the maximum number

max_number = get_max_number(numbers)

print(f"The maximum number is: {max_number}")

# Define a list of user data and print their full names

users = [

    {'first_name': 'Alice', 'last_name': 'Smith'},

    {'first_name': 'Bob', 'last_name': 'Jones'},

    {'first_name': 'Charlie', 'last_name': 'Brown'}

]

print("The users are:")

print_user_names(users)

# Add a new user to the database

new_user = {'first_name': 'David', 'last_name': 'Lee'}

add_user_to_database(new_user)

print(f"{get_full_name(new_user)} has been added to the database.")

