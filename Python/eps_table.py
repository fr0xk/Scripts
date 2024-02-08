#!/usr/bin/env python3

"""
This script generates a table of earnings per share (EPS) and growth rate for a given number of years, initial EPS, and initial growth rate.

The script takes three arguments from the user: the number of years, the initial EPS, and the initial growth rate in percentage.

The script prints the table to the standard output, with the following format:

|    | Year |  EPS  | Growth Rate |
|----|------|-------|-------------|
|  0 |   1  |  1.05 |     5.0000% |
|  1 |   2  |  1.10 |     4.5000% |
|  2 |   3  |  1.14 |     4.0500% |
|  3 |Total |  3.29 |             |

The script assumes that the growth rate decreases by 10% each year and never becomes negative.
"""

def generate_table(years, initial_eps, growth_rate):
    # Initialize an empty table with headers
    table = "|    | Year |  EPS  | Growth Rate |\n" + "|----|------|-------|-------------|\n"

    # Initialize a variable to store the total EPS
    total_eps = 0

    # Loop through the number of years
    for i in range(years):
        # Calculate the EPS for the current year using the CAGR formula
        eps = initial_eps * (1 + growth_rate / 100) ** (i + 1)
        # Add the EPS to the total EPS
        total_eps += eps
        # Format and append the row to the table
        table += "|  {} |   {}  |  {:.2f}  |     {:.2f}%    |\n".format(i, i + 1, eps, growth_rate)
        # Decrease the growth rate by 10% each year if it is positive
        if growth_rate > 0:
            growth_rate *= 0.9

    # Format and append the total row to the table
    table += "| {} |Total | {:.2f} |             |".format(years, total_eps)
    # Return the table
    return table

def get_float_input(message):
    # Get user input as a float
    while True:
        try:
            user_input = float(input(message))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    try:
        # Get the user arguments
        years = int(get_float_input("Enter the number of years: "))
        initial_eps = get_float_input("Enter the initial EPS: ")
        growth_rate = get_float_input("Enter the initial growth rate in percentage: ")

        # Generate the table
        table = generate_table(years, initial_eps, growth_rate)
        # Print the table
        print(table)
    except KeyboardInterrupt:
        print("\nScript interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the main function
    main()

