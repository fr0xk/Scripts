def calculate_evi(external_debt, foreign_exchange_reserves, exports, imports, current_account_balance, short_term_debt):
    """
    Calculate the Economic Vulnerability Index (EVI) for a country based on its external debt, foreign exchange reserves,
    exports, imports, current account balance, and short-term debt.

    Args:
        external_debt (float): Total external debt of the country in billion USD.
        foreign_exchange_reserves (float): Total foreign exchange reserves of the country in billion USD.
        exports (float): Total value of exports of the country in billion USD.
        imports (float): Total value of imports of the country in billion USD.
        current_account_balance (float): Current account balance of the country in billion USD.
        short_term_debt (float): Total short-term external debt of the country in billion USD.

    Returns:
        float: The calculated EVI.

    Raises:
        ValueError: If any of the input parameters are negative or zero.
        ZeroDivisionError: If exports or foreign exchange reserves are zero.
    """
    if any(x <= 0 for x in [external_debt, foreign_exchange_reserves, exports, imports, current_account_balance, short_term_debt]):
        raise ValueError("Input parameters must be positive and non-zero.")
    if foreign_exchange_reserves == 0 or exports == 0:
        raise ZeroDivisionError("Foreign exchange reserves and exports cannot be zero.")

    evi = 0.1*(external_debt/exports) + 0.1*(short_term_debt/foreign_exchange_reserves) + 0.1*(current_account_balance/exports)

    return evi

# Get user input
external_debt = float(input("Enter total external debt (in billion USD): "))
foreign_exchange_reserves = float(input("Enter total foreign exchange reserves (in billion USD): "))
exports = float(input("Enter total value of exports (in billion USD): "))
imports = float(input("Enter total value of imports (in billion USD): "))
current_account_balance = float(input("Enter current account balance (in billion USD): "))
short_term_debt = float(input("Enter total short-term external debt (in billion USD): "))

# Calculate EVI
evi = calculate_evi(external_debt, foreign_exchange_reserves, exports, imports, current_account_balance, short_term_debt)

# Compare with EVI thresholds
if evi < 0.3:
    print(f"EVI is {evi:.2f}, which is considered low.")
elif evi >= 0.3 and evi < 0.5:
    print(f"EVI is {evi:.2f}, which is considered moderate.")
else:
    print(f"EVI is {evi:.2f}, which is considered high.")
