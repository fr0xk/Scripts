# Define variables

MULTIPLE = 10

# Define function to get user input

def get_input(prompt):

    while True:

        try:

            value = float(input(prompt))

            return value

        except ValueError:

            print("Invalid input. Please enter a number.")

# Get user input

net_income = get_input("Enter net income: ")

depr_amort = get_input("Enter depreciation and amortization: ")

non_cash_exp = get_input("Enter non-cash expenses: ")

net_wc = get_input("Enter net working capital: ")

fixed_assets = get_input("Enter fixed assets: ")

# Calculate valuation

valuation = (net_income + depr_amort + non_cash_exp) * MULTIPLE + \

            (net_wc + fixed_assets)

# Print valuation

print("The valuation of the company is:", valuation)

