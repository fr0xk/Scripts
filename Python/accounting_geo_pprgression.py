# This script calculates the total value over successive years in an accounting scenario
# The user inputs the initial amount, expected annual growth rate, and the number of years
# The script generates an accounting-style table showing the total value for each successive year

# MIT License
# Copyright (c) [Year] [Author]

def total_value(initial_amount, growth_rate, year):
    """
    Calculate the total value for a given year using geometric progression formula.

    Parameters:
    - initial_amount (float): The initial amount of the investment.
    - growth_rate (float): The annual growth rate as a decimal.
    - year (int): The number of years.

    Returns:
    - float: The total value for the specified year.
    """
    return initial_amount * (growth_rate + 1) ** (year - 1)

def get_float_input(prompt):
    """
    Get a valid float input from the user.

    Parameters:
    - prompt (str): The input prompt.

    Returns:
    - float: The user-provided float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    """
    Get a valid integer input from the user.

    Parameters:
    - prompt (str): The input prompt.

    Returns:
    - int: The user-provided integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Ask the user for the initial amount, growth rate, and number of years
    initial_amount = get_float_input("Enter the initial amount: ")
    growth_rate = get_float_input("Enter the annual growth rate (as a decimal): ")
    years = get_int_input("Enter the number of years: ")

    # Print the header of the table
    print("Year\tTotal Value")
    print("--------------------")

    total_values = []
    
    # Loop through the years and print the total value for each year
    for year in range(1, years + 1):
        # Call the total_value function and format the output to two decimal places
        total = total_value(initial_amount, growth_rate, year)
        total_values.append(total)
        print(f"{year}\t{total:.2f}")

    # Calculate and print the sum of all total values
    total_sum = sum(total_values)
    print(f"\nSum of all above {years} terms: {total_sum:.2f} ({round(total_sum)})")

if __name__ == "__main__":
    main()

