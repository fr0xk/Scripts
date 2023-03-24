from enum import Enum

from typing import List, Tuple

class BicycleType(Enum):

    MOUNTAIN_BIKE = "Mountain Bike"

    ROAD_BIKE = "Road Bike"

    BMX = "BMX"

    CRUISER = "Cruiser"

class Bicycle:

    def __init__(self, name: str, price: float, bicycle_type: BicycleType, components: List[str], dimensions: Tuple[float, float, float]):

        self.name = name

        self.price = price

        self.bicycle_type = bicycle_type

        self.components = components

        self.dimensions = dimensions

    def display_information(self):

        print(f"Name: {self.name}")

        print(f"Price: ${self.price}")

        print(f"Bicycle Type: {self.bicycle_type.value}")

        print(f"Components: {', '.join(self.components)}")

        print(f"Dimensions: {self.dimensions[0]} x {self.dimensions[1]} x {self.dimensions[2]} inches")

if __name__ == "__main__":

    bike = Bicycle("Mountain Bike 1", 1000.0, BicycleType.MOUNTAIN_BIKE, ["Shimano XT derailleur", "RockShox suspension fork"], (28.0, 18.0, 10.0))

    bike.display_information()

