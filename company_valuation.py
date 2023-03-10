# Define variables
MULTIPLE = 10

# Get user input
while True:
    try:
        net_income = float(input("Enter net income: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        depr_amort = float(input("Enter depreciation and amortization: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        non_cash_exp = float(input("Enter non-cash expenses: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        net_wc = float(input("Enter net working capital: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        fixed_assets = float(input("Enter fixed assets: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate valuation
valuation = (net_income + depr_amort + non_cash_exp) * MULTIPLE + \
            (net_wc + fixed_assets)

# Print valuation
print("The valuation of the company is:", valuation)
