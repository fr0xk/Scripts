# Import tabulate library for printing tables
from tabulate import tabulate

# Define function to handle user input for a float value
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Define function to handle user input for an integer value
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Ask the user to enter the initial values
revenue = get_float_input("Enter the initial revenue: $") # Initial revenue
net_margin = get_float_input("Enter the net profit margin (as a percentage): ") / 100 # Net profit margin
growth_rate = get_float_input("Enter the revenue growth rate (as a percentage): ") / 100 # Revenue growth rate
years = get_int_input("Enter the number of years: ") # Number of years
discount_rate = get_float_input("Enter the discount rate (as a percentage): ") / 100 # Discount rate

# Create an empty list to store the results
results = []

# Loop through each year and calculate the values
for year in range(years + 1):
    # Calculate the net profit for the current year
    net_profit = revenue * net_margin

    # Append the values to the results list as a tuple
    results.append((year, revenue, growth_rate, net_margin, net_profit))

    # Update the revenue for the next year
    revenue = revenue * (1 + growth_rate)

# Calculate the total net profit by summing up the net profits
total_net_profit = sum([result[4] / ((1 + discount_rate) ** result[0]) for result in results])

# Print the results using tabulate library
print(tabulate(results, headers=["Year", "Revenue", "Growth rate", "Net profit margin", "Net profit"], floatfmt=".2f"))
print(f"Total discounted net profit in {years} years at a discount rate of {discount_rate:.2%}: ${total_net_profit:.2f}")

