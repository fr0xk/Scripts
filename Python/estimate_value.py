# Define a function to get the user input
def get_input():
  # Use a try-except block to catch errors
  try:
    # Prompt the user to enter the initial EPS, growth rate, and years
    eps = float(input("Enter the initial earning per share in rupees: "))
    growth_rate = float(input("Enter the growth rate for first 5 years (in percentage): "))
    years = int(input("Enter the total number of years: "))
    # Convert the growth rate to decimal if it is greater than 1
    if growth_rate > 1:
      growth_rate = growth_rate / 100
    # Return the input values as a tuple
    return (eps, growth_rate, years)
  # Handle the ValueError if the input is not valid
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    # Call the function again
    return get_input()

# Define a function to create the table and calculate the total
def create_table(eps, growth_rate, years):
  # Initialize the table and total variables
  table = []
  total = 0
  # Loop through the years
  for year in range(1, years + 1):
    # Append the year and EPS to the table
    table.append([year, eps])
    # Add the EPS to the total
    total += eps
    # Update the EPS with the growth rate
    eps = eps * (1 + growth_rate)
    # Check if the growth rate needs to be halved
    if year == 5:
      growth_rate = growth_rate / 2
  # Return the table and total as a tuple
  return (table, total)

# Define a function to print the table and total
def print_table(table, total):
  # Print the table header
  print("Earning per share (EPS) table")
  # Print a horizontal line
  print("-" * 20)
  # Print the table rows
  for row in table:
    print(f"Year {row[0]}: {row[1]:.2f} rupees")
  # Print a horizontal line
  print("-" * 20)
  # Print the total
  print(f"Sum of EPS: {total:.2f} rupees")

# Call the get_input function and unpack the values
eps, growth_rate, years = get_input()
# Call the create_table function and unpack the values
table, total = create_table(eps, growth_rate, years)
# Call the print_table function
print_table(table, total)

