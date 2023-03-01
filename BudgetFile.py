import math

# Define income brackets and their corresponding allocation percentages

INCOME_BRACKETS = [

    {"name": "Low Income", "income_max": 25000, "allocations": {"Housing": 0.3, "Food": 0.15, "Transportation": 0.12, "Utilities": 0.1, "Insurance": 0.05, "Healthcare": 0.08, "Savings": 0.2, "Debt Repayment": 0.0, "Entertainment": 0.0}},

    {"name": "Middle Income", "income_max": 50000, "allocations": {"Housing": 0.25, "Food": 0.12, "Transportation": 0.1, "Utilities": 0.08, "Insurance": 0.05, "Healthcare": 0.05, "Savings": 0.15, "Debt Repayment": 0.1, "Entertainment": 0.1}},

    {"name": "High Income", "income_max": math.inf, "allocations": {"Housing": 0.2, "Food": 0.1, "Transportation": 0.08, "Utilities": 0.05, "Insurance": 0.03, "Healthcare": 0.02, "Savings": 0.3, "Debt Repayment": 0.1, "Entertainment": 0.12}}

]

# Prompt user for monthly income

monthly_income = float(input("Enter your monthly income: "))

# Determine income bracket based on monthly income

income_bracket = next((ib for ib in INCOME_BRACKETS if monthly_income <= ib["income_max"]), INCOME_BRACKETS[-1])

# Calculate allocation based on income bracket and ensure that it never exceeds 100% or the monthly income

total_allocation = sum(income_bracket["allocations"].values())

if total_allocation > 1:

    print("Error: Total allocation exceeds 100%")

    exit()

budget = {category: math.floor(allocation * monthly_income) for category, allocation in income_bracket["allocations"].items()}

total_budget = sum(budget.values())

if total_budget > monthly_income:

    print("Error: Total allocation exceeds monthly income")

    exit()

# Print budget breakdown

print(f"\nBudget for {income_bracket['name']} ({monthly_income}):")

for category, amount in budget.items():

    print(f"{category}: Rs.{amount}")

print(f"Total budget: Rs.{total_budget}")

