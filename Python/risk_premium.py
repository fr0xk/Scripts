def get_float_input(prompt):
    """Get float input from the user."""
    while True:
        value = input(prompt)
        try:
            value = float(value)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calc_avg_annual_return(growth_rate, psr_future, psr_today, time_period, avg_dividend_yield):
    """Calculate the average annual return."""
    psr_ratio = psr_future / psr_today
    avg_annual_return = (1 + growth_rate) * (psr_ratio ** (1 / time_period)) - 1 + avg_dividend_yield
    return avg_annual_return

if __name__ == "__main__":
    print("This program calculates the average annual return based on user inputs.")
    print("Please enter the following values:")
    growth_rate = get_float_input("Growth rate: ")
    psr_future = get_float_input("Future price-to-sales ratio: ")
    psr_today = get_float_input("Today's price-to-sales ratio: ")
    time_period = get_float_input("Time period (in years): ")
    avg_dividend_yield = get_float_input("Average dividend yield: ")
    
    avg_annual_return = calc_avg_annual_return(growth_rate, psr_future, psr_today, time_period, avg_dividend_yield)
    print("The average annual return is: {:.2%}".format(avg_annual_return))

