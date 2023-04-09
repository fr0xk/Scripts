import math
from tabulate import tabulate

# Get user inputs
current_revenue = float(input("Enter current revenue: "))
ps_ratio = float(input("Enter P/S ratio: "))
risk_premium = float(input("Enter risk premium (%): "))

# Calculate expected growth rate
expected_growth_rate = math.pow(ps_ratio, 1/10) - 1

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

