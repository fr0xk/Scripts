from typing import Tuple, List

from enum import Enum

class Material(Enum):

    Steel = 1

    Aluminum = 2

    CarbonFiber = 3

class Frame:

    def __init__(self, material: Material, size: Tuple[int, int]):

        self.material, self.size = material, size

class Wheel:

    def __init__(self, diameter: float, spokes: int):

        self.diameter, self.spokes = diameter, spokes

class BrakeType(Enum):

    Rim = 1

    Disc = 2

class BrakeLocation(Enum):

    Front = 1

    Rear = 2

class Brake:

    def __init__(self, type: BrakeType, location: BrakeLocation):

        self.type, self.location = type, location

class Bicycle:

    def __init__(self, frame: Frame, wheels: List[Wheel], brakes: List[Brake]):

        self.frame, self.wheels, self.brakes = frame, wheels, brakes

valid_materials = [Material.Steel, Material.Aluminum, Material.CarbonFiber]

valid_spoke_counts = range(4, 101, 4)

valid_brake_types = [BrakeType.Rim, BrakeType.Disc]

valid_brake_locations = [BrakeLocation.Front, BrakeLocation.Rear]

def get_frame(material: Material, size: Tuple[int, int]) -> Frame:

    return Frame(material, size)

def get_wheel(diameter: float, spokes: int) -> Wheel:

    return Wheel(diameter, spokes)

def get_brake(type: BrakeType, location: BrakeLocation) -> Brake:

    return Brake(type, location)

def build_bicycle(material: Material, frame_size: Tuple[int, int], wheel_diameter: float, spoke_count: int, brake_type: BrakeType, brake_location: BrakeLocation) -> Bicycle:

    frame = get_frame(material, frame_size)

    wheels = [get_wheel(wheel_diameter, spoke_count) for i in range(2)]

    brakes = [get_brake(brake_type, brake_location) for i in range(2)]

    return Bicycle(frame, wheels, brakes)

