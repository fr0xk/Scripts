# Define budget allocation percentages for each income class

LOW_INCOME_CLASS = {"housing": 0.35, "food": 0.25, "transportation": 0.15, "healthcare": 0.10, "education": 0.10, "entertainment": 0.05, "miscellaneous": 0.05}

LOWER_MIDDLE_INCOME_CLASS = {"housing": 0.30, "food": 0.20, "transportation": 0.15, "healthcare": 0.10, "education": 0.10, "savings": 0.10, "entertainment": 0.05, "miscellaneous": 0.05}

MIDDLE_INCOME_CLASS = {"housing": 0.25, "food": 0.15, "transportation": 0.15, "healthcare": 0.10, "education": 0.10, "savings": 0.10, "entertainment": 0.10, "travel": 0.05, "miscellaneous": 0.05}

UPPER_MIDDLE_INCOME_CLASS = {"housing": 0.20, "food": 0.10, "transportation": 0.10, "healthcare": 0.10, "education": 0.10, "savings": 0.20, "entertainment": 0.10, "travel": 0.10, "miscellaneous": 0.10}

HIGH_INCOME_CLASS = {"housing": 0.15, "food": 0.05, "transportation": 0.05, "healthcare": 0.10, "education": 0.05, "savings": 0.35, "entertainment": 0.10, "travel": 0.15}

# Ask user for monthly income

monthly_income = float(input("Enter your monthly income in INR: "))

# Calculate annual income

annual_income = monthly_income * 12

# Determine the user's income class based on their annual income

if annual_income < 250000:

    income_class = "Low-Income Class"

    budget_allocation = LOW_INCOME_CLASS

elif annual_income < 500000:

    income_class = "Lower-Middle Income Class"

    budget_allocation = LOWER_MIDDLE_INCOME_CLASS

elif annual_income < 1000000:

    income_class = "Middle-Income Class"

    budget_allocation = MIDDLE_INCOME_CLASS

elif annual_income < 2500000:

    income_class = "Upper-Middle Income Class"

    budget_allocation = UPPER_MIDDLE_INCOME_CLASS

else:

    income_class = "High-Income Class"

    budget_allocation = HIGH_INCOME_CLASS

# Calculate the budget allocation for each expense category

budget_allocation_result = {}

for category, percentage in budget_allocation.items():

    budget_allocation_result[category] = round(percentage * monthly_income, 2)

# Add savings to the budget allocation if it's defined for the income class

if 'savings' in budget_allocation:

    budget_allocation_result['savings'] = round(budget_allocation['savings'] * monthly_income, 2)

# Print the budget allocation for the user's income class

print("\nYou belong to the", income_class, "and your budget allocation is:")

for category, amount in budget_allocation_result.items():

    print(f"{category.capitalize()}: {amount}")

