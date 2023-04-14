import math
from tabulate import tabulate

# Get user inputs
current_cashflow = float(input("Enter current cashflow: "))
valuation_multiple = float(input("Enter valuation multiple: "))
risk_premium = float(input("Enter risk premium (%): "))

# Calculate expected growth rate
expected_growth_rate = math.pow(valuation_multiple, 1/10) - 1

# Calculate adjusted growth rate based on risk premium
risk_adjusted_growth_rate = expected_growth_rate - (risk_premium / 100)

# Calculate projected cashflow for each year over the next 10 years
cashflow_data = []
growth_rate = risk_adjusted_growth_rate
for year in range(1, 11):
    projected_cashflow = current_cashflow * math.pow(1 + growth_rate, year)
    cashflow_data.append([f"Year {year}", f"${projected_cashflow:.2f}"])
    growth_rate *= 0.9  # assume the growth rate declines by 10% each year

# Print table of projected cashflow
headers = ["Year", "Projected Revenue"]
table = tabulate(cashflow_data, headers, tablefmt="pipe")
print(table)

