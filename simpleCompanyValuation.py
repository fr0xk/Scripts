#!/usr/bin/env python3

# MIT License
# Copyright (c) [year] [author]

import sys

def get_input(prompt, expected_type):
    while True:
        user_input = input(prompt)
        try:
            return expected_type(user_input)
        except ValueError:
            print(f"Error: input must be a {expected_type.__name__}. Please try again.")

def get_float_input(prompt):
    return get_input(prompt, float)

def get_int_input(prompt):
    return get_input(prompt, int)

def calculate_inflation_adjusted_earnings(earnings, inflation_rates):
    inflation_adjusted_earnings = []
    for i, earnings_year in enumerate(earnings):
        inflation_adjusted_earnings.append(earnings_year / (1 + inflation_rates[i]) ** (i + 1))
    return inflation_adjusted_earnings

def calculate_average_earnings(earnings):
    return sum(earnings) / len(earnings)

def calculate_earnings_growth_rate(start_earnings, end_earnings, num_years):
    return ((end_earnings / start_earnings) ** (1 / num_years)) - 1

def calculate_price_to_earnings(share_price, average_earnings):
    return share_price / average_earnings

def main():
    print("Welcome to the stock analysis tool!")
    company_name = input("Please enter the name of the publicly traded company: ")
    start_year = get_int_input("Please enter the beginning year of the earnings data: ")
    end_year = get_int_input("Please enter the ending year of the earnings data: ")
    inflation_rate = get_float_input("Please enter the estimated inflation rate (as a decimal): ")
    
    # Collect earnings data
    earnings = []
    for year in range(start_year, end_year + 1):
        earnings.append(get_float_input(f"Please enter the earnings per share for {year}: "))
    
    # Calculate inflation-adjusted earnings and average earnings
    inflation_adjusted_earnings = calculate_inflation_adjusted_earnings(earnings, [inflation_rate] * len(earnings))
    average_earnings = calculate_average_earnings(inflation_adjusted_earnings)
    
    # Calculate earnings growth rate
    num_years = end_year - start_year + 1
    earnings_growth_rate = calculate_earnings_growth_rate(inflation_adjusted_earnings[0], inflation_adjusted_earnings[-1], num_years)
    
    # Get current share price
    share_price = get_float_input("Please enter the current price per share: ")
    
    # Calculate price-to-earnings ratio
    price_to_earnings = calculate_price_to_earnings(share_price, average_earnings)
    
    # Output results
    print(f"\n{company_name} Stock Analysis\n")
    print(f"Average Inflation-Adjusted Earnings Per Share: {average_earnings:.2f}")
    print(f"Earnings Growth Rate (CAGR): {earnings_growth_rate:.2%}")
    print(f"Price-to-Earnings Ratio: {price_to_earnings:.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(1)
