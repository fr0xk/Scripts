# Importing standard libraries
import math

# Prompting user for input
start_year = int(input("Enter beginning year: "))
end_year = int(input("Enter ending year: "))

# Collecting the earnings for each year as a list
earnings = [float(input(f"Enter earnings for {year}: ")) for year in range(start_year, end_year + 1)]

# Prompting user for inflation rate and current market price
inflation_rate = float(input("Enter inflation rate (in percentage): "))
current_market_price = float(input("Enter current market price: "))

# Calculating the average inflation rate for each year
inflation_rates = [(1 + inflation_rate / 100) ** (year - start_year) for year in range(start_year, end_year + 1)]
average_inflation_rate = math.prod(inflation_rates) ** (1 / len(inflation_rates)) - 1

# Calculating the earnings adjusted for inflation
inflation_adjusted_earnings = [earning / inflation_rate for earning, inflation_rate in zip(earnings, inflation_rates)]

# Calculating the Shiller PE Ratio
shiller_pe = current_market_price / (sum(inflation_adjusted_earnings) / len(inflation_adjusted_earnings))

# Printing the result
print(f"The Shiller PE Ratio is {shiller_pe:.2f}")

