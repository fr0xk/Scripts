# Ask user for monthly income

monthly_income = float(input("Enter your monthly income in INR: "))

# Calculate annual income

annual_income = monthly_income * 12

# Determine income class

if annual_income < 250000:

    income_class = "Low-Income Class"

    housing = 0.35 * monthly_income

    food = 0.25 * monthly_income

    transportation = 0.15 * monthly_income

    healthcare = 0.10 * monthly_income

    education = 0.10 * monthly_income

    entertainment = 0.05 * monthly_income

    miscellaneous = 0.05 * monthly_income

elif annual_income >= 250000 and annual_income < 500000:

    income_class = "Lower-Middle Income Class"

    housing = 0.30 * monthly_income

    food = 0.20 * monthly_income

    transportation = 0.15 * monthly_income

    healthcare = 0.10 * monthly_income

    education = 0.10 * monthly_income

    savings = 0.10 * monthly_income

    entertainment = 0.05 * monthly_income

    miscellaneous = 0.05 * monthly_income

elif annual_income >= 500000 and annual_income < 1000000:

    income_class = "Middle-Income Class"

    housing = 0.25 * monthly_income

    food = 0.15 * monthly_income

    transportation = 0.15 * monthly_income

    healthcare = 0.10 * monthly_income

    education = 0.10 * monthly_income

    savings = 0.10 * monthly_income

    entertainment = 0.10 * monthly_income

    travel = 0.05 * monthly_income

    miscellaneous = 0.05 * monthly_income

elif annual_income >= 1000000 and annual_income < 2500000:

    income_class = "Upper-Middle Income Class"

    housing = 0.20 * monthly_income

    food = 0.10 * monthly_income

    transportation = 0.10 * monthly_income

    healthcare = 0.10 * monthly_income

    education = 0.10 * monthly_income

    savings = 0.20 * monthly_income

    entertainment = 0.10 * monthly_income

    travel = 0.10 * monthly_income

    miscellaneous = 0.10 * monthly_income

else:

    income_class = "High-Income Class"

    housing = 0.15 * monthly_income

    food = 0.05 * monthly_income

    transportation = 0.05 * monthly_income

    healthcare = 0.10 * monthly_income

    education = 0.05 * monthly_income

    savings = 0.35 * monthly_income

    entertainment = 0.10 * monthly_income

    travel = 0.15 * monthly_income

# Display budget allocation

print("\nYou belong to the", income_class)

print("Here's your budget allocation:")

print("Housing and Utilities:", round(housing, 2))

print("Food and Groceries:", round(food, 2))

print("Transportation:", round(transportation, 2))

print("Healthcare:", round(healthcare, 2))

print("Education:", round(education, 2))

if 'savings' in locals():

    print("Savings and Investments:", round(savings, 2))

print("Entertainment and Miscellaneous:", round(entertainment, 2))

if 'travel' in locals():
    print("Travel:", round(travel, 2))
print("Miscellaneous:", round(miscellaneous, 2))
 
