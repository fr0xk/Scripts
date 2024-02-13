# Define constants for the minimum and maximum number of entries
MIN_ENTRIES = 5
MAX_ENTRIES = 10

# Define a function to calculate the CPI adjusted EPS
cpi_adjusted_eps = lambda eps, cpi: eps * (1 + cpi / 100)

# Define a function to calculate the cumulative EPS
ceps = lambda cpi_adj_eps: sum(cpi_adj_eps)

# Define a function to calculate the average of a list
average = lambda lst: sum(lst) / len(lst)

# Define a function to display the table of results
def display_table(years, eps, cpi, cpi_adj_eps, ceps_values):
    """Prints a formatted table of the results."""
    # Define the table headers
    headers = ["Year", "EPS", "CPI (%)", "CPI Adjusted EPS", "CEPS"]
    # Define the table format
    table_format = "| {:^4} | {:^5} | {:^7} | {:^16} | {:^5} |"
    # Print the table header
    print(table_format.format(*headers))
    # Print the table separator
    print(table_format.format(*["-" * len(h) for h in headers]))
    # Print the table rows
    for i in range(len(years)):
        # Format the values to two decimal places
        values = [years[i], f"{eps[i]:.2f}", f"{cpi[i]:.2f}", f"{cpi_adj_eps[i]:.2f}", f"{ceps_values[i]:.2f}"]
        # Print the table row
        print(table_format.format(*values))

# Define a function to get the user input
def get_input(prompt, validate, error):
    """Gets the user input and validates it."""
    # Ask the user for the input
    value = input(prompt)
    # Check if the input is valid
    if validate(value):
        # Return the input
        return value
    else:
        # Print the error message
        print(error)
        # Try again
        return get_input(prompt, validate, error)

# Define a function to get the number of entries
def get_n():
    """Gets the number of entries from the user."""
    # Define the prompt, validation, and error message
    prompt = f"How many entries do you want to input? (min {MIN_ENTRIES}, max {MAX_ENTRIES}): "
    validate = lambda n: n.isdigit() and MIN_ENTRIES <= int(n) <= MAX_ENTRIES
    error = f"Invalid input. Please enter a number between {MIN_ENTRIES} and {MAX_ENTRIES}."
    # Get the input and convert it to an integer
    return int(get_input(prompt, validate, error))

# Define a function to get the year
def get_year(i, years):
    """Gets the year for the i-th entry from the user."""
    # Define the prompt, validation, and error message
    prompt = f"Enter the year for entry {i + 1}: "
    validate = lambda year: year.isdigit() and int(year) not in years
    error = "Invalid input. Year already exists."
    # Get the input and convert it to an integer
    return int(get_input(prompt, validate, error))

# Define a function to get the EPS
def get_eps(year):
    """Gets the EPS for the given year from the user."""
    # Define the prompt, validation, and error message
    prompt = f"Enter the EPS for year {year}: "
    validate = lambda eps: eps.replace(".", "", 1).isdigit()
    error = "Invalid input. Please enter a positive number."
    # Get the input and convert it to a float
    return float(get_input(prompt, validate, error))

# Define a function to get the CPI
def get_cpi(year):
    """Gets the CPI for the given year from the user."""
    # Define the prompt, validation, and error message
    prompt = f"Enter the CPI (%) for year {year}: "
    validate = lambda cpi: cpi.replace(".", "", 1).isdigit()
    error = "Invalid input. Please enter a positive number."
    # Get the input and convert it to a float
    return float(get_input(prompt, validate, error))

# Define a function to get the input data
def get_data(n, i=0, years=[], eps=[], cpi=[]):
    """Gets the input data from the user recursively."""
    # Check if the base case is reached
    if i == n:
        # Return the input data
        return years, eps, cpi
    else:
        # Get the year for the i-th entry
        year = get_year(i, years)
        # Append the year to the list
        years.append(year)
        # Get the EPS for the i-th entry
        eps_value = get_eps(year)
        # Append the EPS to the list
        eps.append(eps_value)
        # Get the CPI for the i-th entry
        cpi_value = get_cpi(year)
        # Append the CPI to the list
        cpi.append(cpi_value)
        # Recursively get the data for the next entry
        return get_data(n, i + 1, years, eps, cpi)

# Define a function to calculate the CPI adjusted EPS
def calc_cpi_adj_eps(eps, cpi):
    """Calculates the CPI adjusted EPS for each entry."""
    # Use the map function to apply the cpi_adjusted_eps function to each pair of eps and cpi values
    return list(map(cpi_adjusted_eps, eps, cpi))

# Define a function to calculate the cumulative EPS
def calc_ceps_values(cpi_adj_eps, i=0, ceps_values=[]):
    """Calculates the cumulative EPS for each entry recursively."""
    # Check if the base case is reached
    if i == len(cpi_adj_eps):
        # Return the cumulative EPS values
        return ceps_values
    else:
        # Calculate the cumulative EPS for the i-th entry
        ceps_value = ceps(cpi_adj_eps[:i + 1])
        # Append the cumulative EPS to the list
        ceps_values.append(ceps_value)
        # Recursively calculate the cumulative EPS for the next entry
        return calc_ceps_values(cpi_adj_eps, i + 1, ceps_values)

# Define a function to get the current price
def get_price():
    """Gets the current price from the user."""
    # Define the prompt, validation, and error message
    prompt = "Enter the current price: "
    validate = lambda price: price.replace(".", "", 1).isdigit()
    error = "Invalid input. Please enter a positive number."
    # Get the input and convert it to a float
    return float(get_input(prompt, validate, error))

# Define a function to calculate the ratio of price to average CPI adjusted EPS
def calc_ratio(price, avg_cpi_adj_eps):
    """Calculates the ratio of price to average CPI adjusted EPS."""
    # Use the division operator to calculate the ratio
    return price / avg_cpi_adj_eps

# Define a function to print the ratio
def print_ratio(ratio):
    """Prints the ratio with two decimal places."""
    # Use the formatted string to print the ratio
    print(f"The Price/(Average CPI adjusted EPS) ratio is: {ratio:.2f}")

# Define the main function
def main():
    """Runs the main program."""
    # Get the number of entries
    n = get_n()
    # Get the input data
    years, eps, cpi = get_data(n)
    # Calculate the CPI adjusted EPS
    cpi_adj_eps = calc_cpi_adj_eps(eps, cpi)
    # Calculate the cumulative EPS
    ceps_values = calc_ceps_values(cpi_adj_eps)
    # Display the table of results
    display_table(years, eps, cpi, cpi_adj_eps, ceps_values)
    # Get the current price
    price = get_price()
    # Calculate the average CPI adjusted EPS
    avg_cpi_adj_eps = average(cpi_adj_eps)
    # Calculate the ratio of price to average CPI adjusted EPS
    ratio = calc_ratio(price, avg_cpi_adj_eps)
    # Print the ratio
    print_ratio(ratio)

# Call the main function
main()

