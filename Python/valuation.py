#!/usr/bin/env python
#
# A python script for valuing companies based on earnings per share, fair PE and expected growth rate

# Import the decimal module to handle precision
import decimal

# Define a custom function to get user input and check for errors
def get_input(prompt, type):
    while True:
        try:
            value = type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid", type.__name__)

# Define a custom function to print the results with two decimal places and dollar sign
def print_result(label, value):
    print(label, "$", round(value, 2))

# Welcome the user and explain the purpose of the script
print("Welcome to the company valuation calculator!")
print("This script will help you estimate the intrinsic value and fair price of a company based on its earnings per share, fair PE ratio and expected growth rate.")

# Ask the user for the current year and the beginning year
current_year = get_input("Enter the current year (e.g. 2021): ", int)
beginning_year = get_input("Enter the beginning year (e.g. 2016): ", int)

# Ask the user for the earnings per share for the current and beginning year
current_eps = get_input("Enter the earnings per share for the current year (e.g. 2.50): ", decimal.Decimal)
beginning_eps = get_input("Enter the earnings per share for the beginning year (e.g. 1.50): ", decimal.Decimal)

# Calculate the expected growth rate as the average annual growth rate of earnings per share
expected_growth_rate = ((current_eps / beginning_eps) ** (decimal.Decimal(1) / (current_year - beginning_year)) - 1) * 100

# Ask the user for the fair PE ratio
fair_pe = get_input("Enter the fair PE ratio (e.g. 15): ", decimal.Decimal)

# Calculate the intrinsic value by multiplying the current EPS by the sum of the fair PE and twice the expected growth rate
intrinsic_value = current_eps * (fair_pe + 2 * expected_growth_rate)

# Calculate a fair price by dividing the intrinsic value by 2
fair_price = intrinsic_value / 2

# Print a blank line for readability
print()

# Print the results using the custom function
print_result("The intrinsic value of the company is", intrinsic_value)
print_result("A fair price to pay for the company is", fair_price)
