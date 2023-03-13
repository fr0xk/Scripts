import numpy as np

import os

# Define the financial ratios to be used in the strategy

def filter(data):

    ratios = [

        ('PE', data[:, 1], lambda x: x < 15),

        ('PS', data[:, 2], lambda x: x < 2),

        ('DE', data[:, 3], lambda x: x < 1),

        ('ROE', data[:, 4], lambda x: x > 15),

        ('DY', data[:, 5], lambda x: x > 0.02),

        ('SG', data[:, 6], lambda x: x > 0.1)

    ]

    # Apply filters based on financial ratios

    mask = np.ones(data.shape[0], dtype=bool)

    for ratio, value, condition in ratios:

        mask = mask & condition(value)

    # Apply risk handling strategy for microcap companies

    if data.shape[0] < 50:

        mask = mask & (data[:, 4] > 20)

    # Return the filtered data

    return data[mask]

# Define the main function for the script

def main():

    try:

        # Check if the input file exists

        if not os.path.exists('microcap_stocks.csv'):

            raise FileNotFoundError("Input file not found.")

        # Load the data from the CSV file

        data = np.genfromtxt('microcap_stocks.csv', delimiter=',', skip_header=1)

        # Filter the stocks based on the financial ratios and risk handling strategy

        filtered_data = filter(data)

        # Check if any stocks were found

        if filtered_data.size == 0:

            print("No stocks met the criteria.")

        else:

            # Print the filtered data

            print(filtered_data)

    except (FileNotFoundError, ValueError) as e:

        print(e)

    except Exception as e:

        print("An error occurred:", e)

if __name__ == '__main__':

    main()

