import sys
import math

class FeelsLike:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity

    def adjustment(self):
        A = 0.1
        B = 4
        C = 30.0
        adjustment_value = A * math.exp(B * self.humidity / (C + self.temp))
        return min(adjustment_value, 20)

    def feels_like(self):
        return self.temp + self.adjustment()

def safe_float(value, default):
    try:
        return float(value)
    except ValueError:
        return default

def main():
    temp_default, humidity_default = 34.0, 67.0
    args = sys.argv[1:3] + [temp_default, humidity_default]
    temp, humidity = map(lambda x: max(0, min(safe_float(x, temp_default), 100)), args[:2])
    fl = FeelsLike(temp, humidity)
    print(f"Feels like temperature: {fl.feels_like():.1f}°C")

if __name__ == "__main__":
    main()

