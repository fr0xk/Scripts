```python
import math

def calculate_exposure_value(aperture, shutter_speed, iso, reflectivity):
    return round(math.log2((aperture**2) / shutter_speed) + math.log2((iso / 100) / reflectivity), 2)

def calculate_illuminance(ev, reflectivity):
    return round(2**ev * reflectivity, 2)

def print_camera_settings(sensor_size_width_mm, sensor_size_height_mm, equivalent_aperture,
                           base_iso, shutter_speed, scene_reflectivity, dynamic_range):
    print("Sensor Size (35mm equivalent): {:.2f} x {:.2f} mm".format(sensor_size_width_mm, sensor_size_height_mm))
    print("Equivalent Aperture: f/{:.2f}".format(equivalent_aperture))
    print("Assumed ISO: {}".format(base_iso))
    print("Assumed Shutter Speed: {:.2f} s".format(shutter_speed))
    print("Assumed Scene Reflectivity: {:.2f}".format(scene_reflectivity))
    print("Assumed Dynamic Range: {} stops".format(dynamic_range))

# Assumptions for Camera
sensor_size_width_mm = 5.22
sensor_size_height_mm = 3.93
crop_factor = 6.6
aperture = 1.8
base_iso = 100
shutter_speed = 1/30
scene_reflectivity = 0.30  # 30%
dynamic_range = 12

# Calculate derived camera settings
sensor_size_35mm_width_mm = sensor_size_width_mm * crop_factor
sensor_size_35mm_height_mm = sensor_size_height_mm * crop_factor
equivalent_aperture = aperture * crop_factor

# Display the calculated values
print_camera_settings(sensor_size_35mm_width_mm, sensor_size_35mm_height_mm, equivalent_aperture,
                       base_iso, shutter_speed, scene_reflectivity, dynamic_range)

# Calculate exposure value
ev = calculate_exposure_value(aperture, shutter_speed, base_iso, scene_reflectivity)

# Calculate illuminance
resulting_illuminance = calculate_illuminance(ev, scene_reflectivity)

print("\nCalculated Illuminance: {:.2f} lux".format(resulting_illuminance))
```
