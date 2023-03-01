import math

INCOME_RANGES = {

    'Lower Income': (0, 25000),

    'Middle Income': (25000, 50000),

    'Upper Income': (50000, float('inf'))

}

BUDGET_ALLOCATIONS = {

    'Lower Income': {'Housing': 0.25, 'Food': 0.3, 'Transportation': 0.1, 'Utilities': 0.1, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.05, 'Debt Repayment': 0.05, 'Entertainment': 0.05},

    'Middle Income': {'Housing': 0.3, 'Food': 0.25, 'Transportation': 0.1, 'Utilities': 0.1, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.05, 'Debt Repayment': 0.05, 'Entertainment': 0.05},

    'Upper Income': {'Housing': 0.35, 'Food': 0.2, 'Transportation': 0.05, 'Utilities': 0.05, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.15, 'Debt Repayment': 0.05, 'Entertainment': 0.05}

}

def get_income_class(income):

    for income_class, (lower, upper) in INCOME_RANGES.items():

        if lower <= income < upper:

            return income_class

    return None

def get_budget(income, income_class, budget_allocations):

    total_budget = min(income, 50000)

    budget = {category: math.floor(allocation * total_budget) for category, allocation in budget_allocations[income_class].items()}

    return budget, total_budget

def print_budget(budget):

    for category, amount in budget.items():

        print(f"{category}: Rs.{amount}")

        

income = float(input("Enter your monthly income: "))

income_class = get_income_class(income)

if income_class is None:

    print("Invalid income entered. Please try again.")

else:

    budget, total_budget = get_budget(income, income_class, BUDGET_ALLOCATIONS)

    print(f"\nBudget for the month for {income_class}:\nTotal budget: Rs.{total_budget}")

    print_budget(budget)

