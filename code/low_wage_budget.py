"""
Here is a general breakdown of the allocation of expenditure by percentage for an average Indian household:

Food and Beverages: 30-40%

Housing and Utilities: 20-25%

Transport and Communication: 10-15%

Education and Health: 5-10%

Personal and Miscellaneous: 10-15%

Clothing and Footwear: 5-10%


# This is an example of a Python file with a table in a comment

# | Category | Examples |

# | --- | --- |

# | Food and Beverages | Groceries, Eating out, Alcoholic beverages |

# | Housing and Utilities | Rent/mortgage payments, Electricity, gas, and water bills, Internet and cable TV bills, Property taxes and home insurance |

# | Transport and Communication | Car payments and fuel, Public transportation fees, Telephone and mobile phone bills, Internet and cable TV bills |

# | Education and Health | Tuition fees, Health insurance premiums, Doctor visits and medical procedures, Gym or fitness club memberships |

# | Personal and Miscellaneous | Entertainment expenses, Gifts, Travel expenses, Hobbies and sports equipment |

# | Clothing and Footwear | Clothing purchases, Shoes and boots, Accessories, Laundry and dry cleaning bills |


# Below is an example of a simple function that takes in a list of expenses and returns the total amount spent

def calculate_total_expenses(expenses):

    total = 0

    for expense in expenses:

        total += expense

    return total

# Example usage

expenses = [50.00, 75.23, 125.50, 23.99]

total = calculate_total_expenses(expenses)

print("Total expenses: $" + str(total))
"""

# Define spending breakdown percentages

SPENDING_BREAKDOWN = {

    'food_and_beverages': 0.55,

    'healthcare': 0.1,

    'clothing_and_footwear': 0.05,

    'housing_and_utilities': 0.1,

    'personal_and_miscellaneous': 0.02,

    'transport_and_communication': 0.03,

    'urgent_short_term_needs': 0.1,

    'important_long_term_needs': 0.05

}

# Define function to calculate spending breakdown

def calculate_spending_breakdown(income):

    # Check if income is above 20,000

    if income > 20000:

        print("Your income is above Rs. 20,000 per month. Please consult a financial advisor for guidance on appropriate spending patterns.")

        return None

    # Calculate spending breakdown

    breakdown = {}

    for category, percentage in SPENDING_BREAKDOWN.items():

        breakdown[category] = round(income * percentage, 2)

    # Adjust spending breakdown to ensure total is 100%

    total_spending = sum(breakdown.values())

    if total_spending > income:

        excess = total_spending - income

        breakdown['food_and_beverages'] -= excess

    elif total_spending < income:

        shortfall = income - total_spending

        breakdown['urgent_short_term_needs'] += shortfall / 2

        breakdown['important_long_term_needs'] += shortfall / 2

    return breakdown

# Define function to print spending breakdown

def print_spending_breakdown(breakdown):

    if breakdown is None:

        return

    # Calculate and print spending breakdown percentages

    total_income = sum(breakdown.values())

    for category, amount in breakdown.items():

        percentage = round(amount / total_income * 100, 2)

        print(f"{category.title()}: {amount} ({percentage}%)")

# Get user's income as input

income = int(input("What is your monthly income (in Rs.)?: "))

# Calculate and print spending breakdown

breakdown = calculate_spending_breakdown(income)

print_spending_breakdown(breakdown)

