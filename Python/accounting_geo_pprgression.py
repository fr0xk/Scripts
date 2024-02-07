def geometric_progression_term(initial_amount, growth_rate, term):
    r = 1 + growth_rate
    return initial_amount * (r ** (term - 1))

def geometric_progression_sum(initial_amount, growth_rate, num_terms):
    r = 1 + growth_rate
    return initial_amount * ((r ** num_terms - 1) / (r - 1))

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():

    initial_amount = get_float_input("Enter the initial amount: ")
    growth_rate = get_float_input("Enter the annual growth rate (as a decimal): ")
    num_terms = get_int_input("Enter the number of terms: ")

    print("\nTerm\tValue")
    print("--------------------")

    total_sum = 0
    for term in range(1, num_terms + 1):
        term_value = geometric_progression_term(initial_amount, growth_rate, term)
        total_sum += term_value
        print(f"{term}\t{term_value:.2f}")

    print(f"\nSum of the first {num_terms} terms: {total_sum:.2f} ({round(total_sum)})")

if __name__ == "__main__":
    main()

