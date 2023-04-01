def calculate_profit(current_revenue, profit_margin, revenue_growth_rate, expense_growth_rate, num_years):

    revenue = current_revenue

    expenses = current_revenue / (1 + profit_margin)

    profits = revenue * profit_margin

    results = [(1, revenue, expenses, profits)]

    for i in range(2, num_years+1):

        revenue = revenue * (1 + revenue_growth_rate)

        expenses = expenses * (1 + expense_growth_rate)

        profits = revenue * profit_margin

        results.append((i, revenue, expenses, profits))

    return results

try:

    current_revenue = float(input("Enter the current revenue: "))

    profit_margin = float(input("Enter the profit margin as a decimal: "))

    revenue_growth_rate = float(input("Enter the revenue growth rate as a decimal: "))

    expense_growth_rate = float(input("Enter the expense growth rate as a decimal: "))

    num_years = int(input("Enter the number of years: "))

    results = calculate_profit(current_revenue, profit_margin, revenue_growth_rate, expense_growth_rate, num_years)

    # Determine the maximum length of each column to adjust spacing accordingly

    max_lengths = [max(len(str(result[i])) for result in results) + 2 for i in range(4)]

    header = [f"Year".ljust(max_lengths[0]), f"Revenue".ljust(max_lengths[1]), f"Expenses".ljust(max_lengths[2]), "Profit"]

    # Print the table header

    print("  ".join(header))

    # Print each row of the table

    for result in results:

        row = [str(result[0]).ljust(max_lengths[0]), f"{result[1]:.2f}".ljust(max_lengths[1]), f"{result[2]:.2f}".ljust(max_lengths[2]), f"{result[3]:.2f}"]

        print("  ".join(row))

except ValueError:

    print("Error: Invalid input. Please enter a valid number.") 

except ZeroDivisionError:

    print("Error: Profit margin cannot be zero.") 

except:

    print("Error: An unexpected error occurred.")

