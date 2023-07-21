def calculate_projected_prices(initial_price, annual_return, years):
    projected_prices = [initial_price]

    for year in range(1, years + 1):
        projected_price = projected_prices[-1] * (1 + annual_return)
        projected_prices.append(projected_price)

    return projected_prices


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")


def get_user_input():
    initial_stock_price = get_float_input("Enter the initial stock price: ")
    expected_annual_return = get_float_input("Enter the expected annual return (as a decimal, e.g., 0.05 for 5%): ")
    return initial_stock_price, expected_annual_return


def print_projected_prices(projected_prices):
    print("\nProjected Stock Prices for the Next 10 Years:")
    print("Year\tProjected Price")
    for year, price in enumerate(projected_prices):
        print(f"{year + 1}\t${price:.2f}")


def main():
    num_years = 10

    try:
        initial_stock_price, expected_annual_return = get_user_input()

        projected_prices = calculate_projected_prices(initial_stock_price, expected_annual_return, num_years)
        print_projected_prices(projected_prices)

    except KeyboardInterrupt:
        print("\nOperation aborted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

