from typing import List, Tuple

# Define custom types for safety

class Frame:

    def __init__(self, material: str, size: Tuple[int, int]):

        assert isinstance(material, str) and material in ["steel", "aluminum", "carbon fiber"], "Invalid material"

        assert isinstance(size, tuple) and len(size) == 2 and all(isinstance(i, int) for i in size), "Invalid size"

        self.material = material

        self.size = size

class Wheel:

    def __init__(self, diameter: float, spokes: int):

        assert isinstance(diameter, float) and diameter > 0, "Invalid diameter"

        assert isinstance(spokes, int) and spokes > 0 and spokes % 4 == 0, "Invalid number of spokes"

        self.diameter = diameter

        self.spokes = spokes

class Bicycle:

    def __init__(self, frame: Frame, wheels: List[Wheel]):

        assert isinstance(frame, Frame), "Invalid frame"

        assert isinstance(wheels, list) and all(isinstance(wheel, Wheel) for wheel in wheels), "Invalid wheels"

        self.frame = frame

        self.wheels = wheels

# Define functions for building the bicycle

def build_frame(material: str, size: Tuple[int, int]) -> Frame:

    assert isinstance(material, str) and material in ["steel", "aluminum", "carbon fiber"], "Invalid material"

    assert isinstance(size, tuple) and len(size) == 2 and all(isinstance(i, int) for i in size), "Invalid size"

    return Frame(material, size)

def build_wheel(diameter: float, spokes: int) -> Wheel:

    assert isinstance(diameter, float) and diameter > 0, "Invalid diameter"

    assert isinstance(spokes, int) and spokes > 0 and spokes % 4 == 0, "Invalid number of spokes"

    return Wheel(diameter, spokes)

def build_bicycle(frame_material: str, frame_size: Tuple[int, int], wheel_specs: List[Tuple[float, int]]) -> Bicycle:

    assert isinstance(frame_material, str), "Invalid frame material"

    assert isinstance(frame_size, tuple) and len(frame_size) == 2 and all(isinstance(i, int) for i in frame_size), "Invalid frame size"

    assert isinstance(wheel_specs, list) and all(isinstance(spec, tuple) for spec in wheel_specs) and all(len(spec) == 2 for spec in wheel_specs), "Invalid wheel specs"

    # Build the frame

    frame = build_frame(frame_material, frame_size)

    # Build the wheels

    wheels = [build_wheel(diameter, spokes) for diameter, spokes in wheel_specs]

    return Bicycle(frame, wheels)

