# Define a function to calculate the maintenance budget for a single bike
def calculate_bike_maintenance_budget(price, maintenance_prices):
    maintenance_budget = sum(map(lambda item: item["price_func"](price)*item["quantity"], maintenance_prices))
    return maintenance_budget

# Define a list of bike prices
bike_prices = [250, 500, 750, 1000]

# Define a list of maintenance items and their prices as lambda functions
maintenance_items = [
    {"name": "cleaning", "price_func": lambda price: (15 - 5) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 5, "quantity": 12},
    {"name": "servicing", "price_func": lambda price: (100 - 50) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 50, "quantity": 1},
    {"name": "tire", "price_func": lambda price: (50 - 20) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 20, "quantity": 2},
    {"name": "brake", "price_func": lambda price: (25 - 10) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 10, "quantity": 2},
    {"name": "lubrication", "price_func": lambda price: (15 - 5) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 5, "quantity": 12},
    {"name": "miscellaneous", "price_func": lambda price: (50 - 10) * (price - bike_prices[0]) / (bike_prices[-1] - bike_prices[0]) + 10, "quantity": 1},
]

# Define the MIT license text
mit_license = """MIT License

Copyright (c) [year] [author]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Loop through the list of bike prices and calculate the maintenance budget for each bike
for price in bike_prices:
    # Calculate the maintenance budget for this bike
    maintenance_budget = calculate_bike_maintenance_budget(price, maintenance_items)

    # Print the maintenance budget for this bike
    print(f"For a bike that costs ${price}, the maintenance budget is ${maintenance_budget} per year.")

# Print the MIT license text
print(mit_license)
