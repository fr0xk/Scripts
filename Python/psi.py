import math

from tabulate import tabulate

def calculate_pressure(weight, bike_weight, tire_radius, tire_width, rolling_resistance, road_grade):

    # Convert tire dimensions to meters

    tire_radius = tire_radius / 1000

    tire_width = tire_width / 1000

    

    # Convert road grade to decimal

    road_grade = road_grade / 100

    

    # Calculate gradient resistance

    gradient_resistance = weight * road_grade

    

    # Calculate pressure

    numerator = weight + bike_weight

    denominator = 2 * math.pi * tire_radius * tire_width

    rolling_resistance_factor = 9.81 * rolling_resistance

    pressure = (numerator / denominator) * (rolling_resistance_factor + gradient_resistance)

    

    # Convert pressure to PSI

    pressure_psi = pressure * 0.145038

    

    return round(pressure_psi, 1)

def main():

    print("Welcome to the Tyre Pressure Calculator!")

    print("Please enter the following information:")

    weight = float(input("Rider weight (kg): "))

    bike_weight = float(input("Bike weight (kg): "))

    tire_radius = float(input("Tire radius (mm): "))

    tire_width = float(input("Tire width (mm): "))

    

    # Display options for choosing rolling resistance coefficient

    rr_options = {1: 0.002, 2: 0.004, 3: 0.006}

    print("\nSelect the coefficient of rolling resistance:")

    print(tabulate([[key, value] for key, value in rr_options.items()], headers=["Option", "Coefficient of Rolling Resistance"], tablefmt="grid"))

    rr_choice = int(input("Enter your choice: "))

    rolling_resistance = rr_options.get(rr_choice, None)

    if rolling_resistance is None:

        print("Invalid choice for rolling resistance.")

        return

    

    # Display options for choosing road grade

    rg_options = {1: 0, 2: 0.04, 3: 0.07, 4: 0.1, 5: -0.01, 6: -0.03, 7: -0.05}

    print("\nSelect the road grade:")

    print(tabulate([[key, value] for key, value in rg_options.items()], headers=["Option", "Road Grade"], tablefmt="grid"))

    rg_choice = int(input("Enter your choice: "))

    road_grade = rg_options.get(rg_choice, None)

    if road_grade is None:

        print("Invalid choice for road grade.")

        return

    

    recommended_pressure_psi = calculate_pressure(weight, bike_weight, tire_radius, tire_width, rolling_resistance, road_grade)

    print(f"The recommended tire pressure is {recommended_pressure_psi} PSI.")

