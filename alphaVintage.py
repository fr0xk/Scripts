import requests

# Step 1: Ask user for a ticker

ticker = input("Enter a ticker symbol: ")

# Step 2: Calculate 60 month average price for that ticker.

api_key = 'E7F7ZFCEPKZ3J2MT'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={ticker}&apikey={api_key}'

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    if 'Monthly Adjusted Time Series' in data:

        prices = []

        for date in sorted(data['Monthly Adjusted Time Series'].keys(), reverse=True):

            price = float(data['Monthly Adjusted Time Series'][date]['4. close'])

            prices.append(price)

            if len(prices) == 60:

                break

        ma60 = sum(prices) / 60

        # Step 3: Create a rate of change taking slope of 60 month moving average.

        roc = (ma60 - prices[-1]) / prices[-1]

        # Step 4: If the rate of change is negative, avoid buying or sell existing position

        if roc < 0:

            print("Do not buy or sell existing position. Rate of change is negative.")

        # Step 5: Else hold or add new positions

        else:

            print("Hold or add new positions. Rate of change is positive.")

    else:

        print("Error: Monthly Adjusted Time Series data not found in API response.")

else:

    print(f"Error: API request failed with status code {response.status_code}.")

