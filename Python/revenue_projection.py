import math
from tabulate import tabulate

def get_valid_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Input value should be greater than 0")
            else:
                return value
        except ValueError:
            print("Error: Invalid input value. Please enter a valid number.")

# Get user inputs with input validation
current_revenue = get_valid_float_input("Enter current revenue: ")
valuation_multiple = get_valid_float_input("Enter valuation multiple: ")
risk_premium = get_valid_float_input("Enter risk premium (%): ")

# Calculate expected growth rate
expected_growth_rate = math.pow(valuation_multiple, 1/10) - 1

# Calculate adjusted growth rate based on risk premium
risk_adjusted_growth_rate = expected_growth_rate - (risk_premium / 100)

# Calculate projected revenue for each year over the next 10 years
revenue_data = []
growth_rate = risk_adjusted_growth_rate
for year in range(1, 11):
    projected_revenue = current_revenue * math.pow(1 + growth_rate, year)
    revenue_data.append([f"Year {year}", f"${projected_revenue:.2f}"])
    growth_rate *= 0.9  # assume the growth rate declines by 10% each year

# Print table of projected revenue
headers = ["Year", "Projected Revenue"]
table = tabulate(revenue_data, headers, tablefmt="pipe")
print(table)

# Check for security vulnerabilities
if valuation_multiple < 1 or risk_premium < 0:
    print("Warning: Valuation multiple or risk premium input values are suspiciously low. Please double-check the inputs.")

