# Define variables
net_income = 1000000
depr_amort = 50000
non_cash_exp = 20000
multiple = 10
net_wc = 500000
fixed_assets = 1000000

# Calculate valuation
valuation = (net_income + depr_amort + non_cash_exp) * multiple + \
            (net_wc + fixed_assets)

# Print valuation
print("The valuation of the company is:", valuation)
