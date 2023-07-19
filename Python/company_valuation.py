def geometric_sum(a, r, n):
    return a * (r ** n - 1) / (r - 1)

def get_float_input(prompt):
    return float(input(prompt))

def get_positive_integer_input(prompt):
    return int(input(prompt))

def main():
    print("Company Value Estimation Tool")
    present_eps = get_float_input("Enter the present EPS: ")
    growth_rate = get_float_input("Enter the growth rate per year (%): ")
    years = get_positive_integer_input("Enter the number of years for growth estimation: ")

    growth_rate = growth_rate / 100.0
    future_eps = present_eps * (1 + growth_rate) ** years
    total_value = geometric_sum(present_eps, 1 + growth_rate, years)

    print("\nResults:")
    print(f"Estimated future EPS after {years} years: ${future_eps:.2f}")
    print(f"Total value per share after {years} years: ${total_value:.2f}")

if __name__ == "__main__":
    main()
