# Import requests and BeautifulSoup libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the screener website
url = "https://www.screener.in/screens/141018/micro-cap-companies/"

# Define the criteria for filtering the companies
sales_growth = 20 # Minimum sales growth over 3 years in percentage
profit_growth = 25 # Minimum profit growth over 3 years in percentage
market_cap = 1000 # Maximum market capitalization in crore rupees

# Define a function to get the table data from the website
def get_table_data(url):
    # Send a GET request to the URL and get the response
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the table element in the HTML
        table = soup.find("table")
        # Get all the table rows
        rows = table.find_all("tr")
        # Initialize an empty list to store the table data
        data = []
        # Loop through each row
        for row in rows:
            # Get all the table cells in the row
            cells = row.find_all("td")
            # Initialize an empty list to store the row data
            row_data = []
            # Loop through each cell
            for cell in cells:
                # Get the cell text and strip any whitespace
                cell_text = cell.text.strip()
                # Append the cell text to the row data list
                row_data.append(cell_text)
            # Append the row data list to the table data list
            data.append(row_data)
        # Return the table data list
        return data
    else:
        # Return None if the response status code is not 200 (OK)
        return None

# Call the function to get the table data from the URL
table_data = get_table_data(url)

# Check if the table data is not None
if table_data is not None:
    # Print a header for the output
    print("Name of companies with criteria:")
    print(f"Sales growth > {sales_growth}%")
    print(f"Profit growth > {profit_growth}%")
    print(f"Market cap < {market_cap} crore")
    print("-" * 50)
    # Loop through each row in the table data except the first one (header row)
    for row in table_data[1:]:
        # Check if the length of the row is at least 11
        if len(row) >= 11:
            try:
                # Get the name, sales growth, profit growth and market cap from the row
                name = row[1]
                sales_growth_3yrs = float(row[9])
                profit_growth_3yrs = float(row[10])
                market_cap_cr = float(row[3])
                # Check if the criteria are met
                if sales_growth_3yrs > sales_growth and profit_growth_3yrs > profit_growth and market_cap_cr < market_cap:
                    # Print the name of the company
                    print(name)
            except ValueError:
                # Skip the row if there is a ValueError while converting to float
                pass
else:
    # Print an error message if the table data is None
    print("Error: Could not fetch the table data from the website.")
