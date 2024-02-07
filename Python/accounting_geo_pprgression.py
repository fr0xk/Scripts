from typing import List

def calculate_geometric_sum(initial_amount: float, growth_rate: float, num_years: int) -> float:
    """
    Calculate the sum of a geometric progression representing successive years.

    Parameters:
    - initial_amount (float): Initial amount or investment
    - growth_rate (float): Annual growth rate
    - num_years (int): Number of years

    Returns:
    - float: Total value after the specified number of years
    """
    total_value = initial_amount * ((1 + growth_rate)**num_years)
    return total_value

def generate_accounting_table(initial_amount: float, growth_rate: float, num_years: int) -> List[str]:
    """
    Generate an accounting-style table showing the total value for successive years.

    Parameters:
    - initial_amount (float): Initial amount or investment
    - growth_rate (float): Annual growth rate
    - num_years (int): Number of years

    Returns:
    - List[str]: List of strings representing the accounting-style table rows
    """
    table_rows = []
    table_rows.append("Year\tTotal Value")
    table_rows.append("-" * 30)

    for year in range(1, num_years + 1):
        total_value = calculate_geometric_sum(initial_amount, growth_rate, year)
        row = f"{year}\t{total_value:.2f}"
        table_rows.append(row)

    return table_rows

def main():
    # Get user input
    initial_amount = float(input("Enter the initial amount or investment: "))
    growth_rate = float(input("Enter the annual growth rate (as a decimal): "))
    num_years = int(input("Enter the number of years: "))

    # Generate and display the accounting-style table
    table = generate_accounting_table(initial_amount, growth_rate, num_years)
    for row in table:
        print(row)

if __name__ == "__main__":
    main()

