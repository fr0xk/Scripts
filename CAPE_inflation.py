# Define a function to get earnings per share for each year

def get_earnings_per_share(start_year, end_year):

    earnings = []

    for year in range(start_year, end_year + 1):

        eps = float(input(f"Enter earnings per share for year {year}: "))

        earnings.append(eps)

    return earnings

# Define a function to format numbers as currency

format_currency = lambda num: f"${num:,.2f}"

# Define a function to adjust earnings for inflation

def adjust_earnings_for_inflation(earnings, inflation_rate):

    adjusted_earnings = []

    for i in range(len(earnings)):

        eps = earnings[i]

        adj_eps = eps * ((1 + inflation_rate) ** (-(i + 1)))

        adjusted_earnings.append(adj_eps)

    return adjusted_earnings

# Get company name

company_name = input("Enter company name: ")

# Get earnings year start and ending

start_year = int(input("Enter earnings year start: "))

end_year = int(input("Enter earnings year end: "))

# Get inflation rate

inflation_rate = float(input("Enter inflation rate as a decimal: "))

# Get earnings per share for each year

earnings = get_earnings_per_share(start_year, end_year)

# Adjust earnings for inflation

adjusted_earnings = adjust_earnings_for_inflation(earnings, inflation_rate)

# Calculate average earnings per share

average_eps = sum(adjusted_earnings) / len(adjusted_earnings)

# Get current price per share

current_price = float(input("Enter current price per share: "))

# Calculate price to earnings ratio

pe_ratio = lambda price, eps: price / eps

price_to_eps_ratio = pe_ratio(current_price, average_eps)

# Format output as currency and decimal

formatted_current_price = format_currency(current_price)

formatted_average_eps = format_currency(average_eps)

formatted_ratio = f"{price_to_eps_ratio:.2f}"

# Print results

print(f"\n{company_name} - Financial Summary")

print(f"Earnings Year: {start_year} - {end_year}")

print(f"Inflation Rate: {inflation_rate:.2%}")

print(f"Earnings Per Share: {', '.join(map(format_currency, earnings))}")

print(f"Adjusted Earnings Per Share: {', '.join(map(format_currency, adjusted_earnings))}")

print(f"Average Adjusted Earnings Per Share: {formatted_average_eps}")

print(f"Current Price Per Share: {formatted_current_price}")

print(f"Price to Earnings Ratio: {formatted_ratio}")

