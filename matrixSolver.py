import numpy as np

# Define lambda function for getting input from user

get_input = lambda message: list(map(float, input(message).split()))

# Prompt user to enter matrix dimensions

m = int(input("Enter the number of rows: "))

n = int(input("Enter the number of columns: "))

# Prompt user to enter matrix coefficients

print("Enter the coefficients of the matrix:")

matrix = [get_input("") for _ in range(m)]

# Convert matrix to numpy array for easier manipulation

matrix = np.array(matrix)

# Display original matrix

print("\nOriginal Matrix:\n", matrix, "\n")

# Perform elementary row operations to obtain row echelon form

for i in range(min(m, n)):

    # Find the pivot element in the current column

    pivot_row = i + np.argmax(np.abs(matrix[i:, i]))

    if matrix[pivot_row][i] == 0:

        print("No unique solution exists.")

        exit()

    matrix[[i, pivot_row]] = matrix[[pivot_row, i]]

    print(f"\nStep {i+1}: Swapping rows {i+1} and {pivot_row+1}")

    print(matrix)

    matrix[i] /= matrix[i][i]

    print(f"\nStep {i+1}: Scaling row {i+1} by 1/{matrix[i][i]}")

    print(matrix)

    matrix[i+1:] -= matrix[i+1:, i, np.newaxis] * matrix[i, np.newaxis, :]

    print(f"\nStep {i+1}: Using row {i+1} to eliminate column {i+1}")

    print(matrix)

# Display row echelon form

print("Row Echelon Form:\n", matrix, "\n")

# Back-substitution to find the solutions

solutions = np.zeros(n)

for i in range(min(m, n)-1, -1, -1):

    solutions[i] = matrix[i][n-1]

    for j in range(i+1, min(m, n)):

        solutions[i] -= matrix[i][j] * solutions[j]

# Display solutions

print("Solutions:")

for i in range(min(m, n)):

    print(f"x{i+1} = {solutions[i]}")

