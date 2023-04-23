import math

def validate_input(prompt, value_type=float, min_value=None):

    while True:

        try:

            value = value_type(input(prompt))

            if min_value is not None and value < min_value:

                raise ValueError(f"{prompt.capitalize()} must be greater than or equal to {min_value}.")

            return value

        except ValueError as e:

            print(f"Invalid input: {e}")

def calculate_altman_score_plus(total_assets, working_capital, retained_earnings, earnings_before_interest_and_tax,

                                market_value_of_equity, sales, number_of_employees):

    # calculate the Altman Z-score Plus score

    A = 1.2 * (working_capital / total_assets)

    B = 1.4 * (retained_earnings / total_assets)

    C = 3.3 * (earnings_before_interest_and_tax / total_assets)

    D = 0.6 * (market_value_of_equity / total_assets)

    E = 1.0 * (sales / total_assets)

    F = 0.99 * (number_of_employees / math.log(total_assets))

    altman_score_plus = A + B + C + D + E + F

    return altman_score_plus

def suggest_action(altman_score_plus):

    # suggest whether to buy, hold, or sell the company

    if altman_score_plus > 2.6:

        return "BUY"

    elif altman_score_plus >= 1.1 and altman_score_plus <= 2.6:

        return "HOLD"

    else:

        return "SELL"

def main():

    # ask user for inputs and validate them

    total_assets = validate_input("Enter the total assets of the company (in millions): ", min_value=0)

    working_capital = validate_input("Enter the working capital of the company (in millions): ", min_value=0)

    retained_earnings = validate_input("Enter the retained earnings of the company (in millions): ", min_value=0)

    earnings_before_interest_and_tax = validate_input("Enter the earnings before interest and taxes of the company (in millions): ", min_value=0)

    market_value_of_equity = validate_input("Enter the market value of equity of the company (in millions): ", min_value=0)

    sales = validate_input("Enter the sales of the company (in millions): ", min_value=0)

    number_of_employees = validate_input("Enter the number of employees of the company: ", min_value=0)

    # calculate the Altman Z-score Plus score

    altman_score_plus = calculate_altman_score_plus(total_assets, working_capital, retained_earnings, earnings_before_interest_and_tax,

                                market_value_of_equity, sales, number_of_employees)

    # display the Altman Z-score Plus score and suggested action

    print("Altman Z-score Plus score:", altman_score_plus)

    print("Suggested action:", suggest_action(altman_score_plus))

if __name__ == '__main__':

    main()

