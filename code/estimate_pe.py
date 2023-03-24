import locale
from typing import Tuple, Union

locale.setlocale(locale.LC_ALL, '')

def calculate_pe_ratio(inputs: Tuple[float, float, float, float, float, float, float, float, float]) -> Union[str, float]:
    eps, dps, r, g, roe, np_margin, div_yield, debt, equity = inputs
    dpr = div_yield / np_margin
    de = debt / equity
    pe_ratio = (dpr / (r - g)) + ((1 - dpr) * ((roe * (1 - de)) / (r - g)))
    return locale.currency(pe_ratio, grouping=True) if pe_ratio > 0 else "Cannot calculate suitable PE ratio with provided inputs"

if __name__ == '__main__':
    try:
        inputs = [float(input(f"Enter {var_name.replace('_', ' ')}: ")) for var_name in [
            "earnings_per_share (EPS)",
            "dividends_per_share (DPS)",
            "expected_annual_return (%)",
            "earnings_growth_rate (%)",
            "return_on_equity (%)",
            "net_profit_margin (%)",
            "dividend_yield (%)",
            "total_debt",
            "total_equity",
        ]]
        print("Suitable PE ratio:", calculate_pe_ratio(inputs))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

