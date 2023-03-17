# Define a function to get earnings per share for each year

def get_earnings_per_share(start_year, end_year):

    earnings = []

    for year in range(start_year, end_year + 1):

        eps = float(input(f"Enter earnings per share for year {year}: "))

        earnings.append(eps)

    return earnings

# Define a function to format numbers as currency

format_currency = lambda num: f"${num:,.2f}"

# Get company name

company_name = input("Enter company name: ")

# Get earnings year start and ending

start_year = int(input("Enter earnings year start: "))

end_year = int(input("Enter earnings year end: "))

# Get earnings per share for each year

earnings = get_earnings_per_share(start_year, end_year)

# Calculate average earnings per share

average_eps = sum(earnings) / len(earnings)

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

print(f"Earnings Per Share: {', '.join(map(format_currency, earnings))}")

print(f"Average Earnings Per Share: {formatted_average_eps}")

print(f"Current Price Per Share: {formatted_current_price}")

print(f"Price to Earnings Ratio: {formatted_ratio}")

