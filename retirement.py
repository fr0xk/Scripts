# Financial and Life Planning Script


import numpy as np

age = 28

income = 12000

max_savings_rate = 0.3

retirement_age = 65

life_expectancy = 80

annual_inflation_rate = 0.04

def calculate_projection(years):

    projection = []

    for i in range(1, years + 1):

        projected_income = income * 12 * i

        projected_expenses = projected_income * (1 - max_savings_rate) ** i

        projected_savings = projected_income - projected_expenses

        projection.append([i, projected_income, projected_savings, projected_expenses])

    return projection

def calculate_retirement_goal():

    retirement_years = life_expectancy - retirement_age

    monthly_inflation_rate = (1 + annual_inflation_rate) ** (1/12) - 1

    retirement_goal = (income * max_savings_rate * 12) * ((1 + monthly_inflation_rate) ** (12 * retirement_years) - 1) / monthly_inflation_rate

    monthly_savings_needed = (retirement_goal * monthly_inflation_rate) / ((1 + monthly_inflation_rate) ** (12 * (retirement_age - age)))

    return retirement_goal, monthly_savings_needed

projection = calculate_projection(5)

retirement_goal, monthly_savings_needed = calculate_retirement_goal()

print("Projected income and expenses for the next 5 years:")

print("Year | Projected Income | Projected Savings | Projected Expenses")

for row in projection:

    print("{:4d} | {:15,.2f} | {:15,.2f} | {:15,.2f}".format(row[0], row[1], row[2], row[3]))

print("Retirement savings needed:")

print("{:,.2f} at retirement age {} to support life expectancy of {}".format(retirement_goal, retirement_age, life_expectancy))

print("Monthly savings needed to reach retirement goal:")

print("{:,.2f} for {} years at an annual inflation rate of {:.1%}".format(monthly_savings_needed, retirement_age - age, annual_inflation_rate))

