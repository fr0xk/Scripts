import math

BUDGET_ALLOCATIONS = {'Lower Income': {'Housing': 0.35, 'Food': 0.25, 'Transportation': 0.15, 'Utilities': 0.05, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.05, 'Debt Repayment': 0.05, 'Entertainment': 0.05},
                      'Middle Income': {'Housing': 0.3, 'Food': 0.20, 'Transportation': 0.15, 'Utilities': 0.10, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.10, 'Debt Repayment': 0.05, 'Entertainment': 0.10},
                      'Upper Income': {'Housing': 0.25, 'Food': 0.15, 'Transportation': 0.10, 'Utilities': 0.10, 'Insurance': 0.05, 'Healthcare': 0.05, 'Savings': 0.15, 'Debt Repayment': 0.05, 'Entertainment': 0.10}}

get_income_class = lambda income: 'Lower Income' if income <= 25000 else 'Middle Income' if income <= 50000 else 'Upper Income'

income = float(input("Enter your monthly income: "))
income_class = get_income_class(income)

get_budget = lambda income_class, budget_allocations: {category: math.floor(allocation * income) for category, allocation in budget_allocations[income_class].items()}
budget = get_budget(income_class, BUDGET_ALLOCATIONS)

list_categories = lambda budget: [print(f"{category}: Rs.{amount}") for category, amount in budget.items()]
list_categories(budget)

total_budget = sum(budget.values())
savings = budget['Savings']

warning = "\nWarning: Your savings are negative. Consider reducing expenses or increasing income." if savings <= 0 else f"\nWarning: Your savings are low. Consider reducing expenses or increasing income." if savings < budget['Food'] else ""

print(f"\nBudget for the month for {income_class}:\nTotal budget: Rs.{total_budget}{warning}")

