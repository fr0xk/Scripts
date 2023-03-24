**Using the context of bike building, showing how three programming languages - Haskell, Python and C++ works**

## Python

```
class Bike:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def describe(self):
        print(f"{self.color} {self.brand} {self.model} Bike:")
        print("Parts:")
        for part in self.parts:
            print(f"- {part}")

class BikePart:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"

bike = Bike("Specialized", "Stumpjumper", "Red")
frame = BikePart("Frame", 1500)
fork = BikePart("Fork", 700)
wheelset = BikePart("Wheelset", 1200)

bike.add_part(frame)
bike.add_part(fork)
bike.add_part(wheelset)

bike.describe()
```

## C++

```
#include <iostream>
#include <string>

using namespace std;

class Bike {
    private:
        string frame;
        string wheels;
        string handlebars;

    public:
        void setFrame(string frame) {
            this->frame = frame;
        }

        string getFrame() {
            return frame;
        }

        void setWheels(string wheels) {
            this->wheels = wheels;
        }

        string getWheels() {
            return wheels;
        }

        void setHandlebars(string handlebars) {
            this->handlebars = handlebars;
        }

        string getHandlebars() {
            return handlebars;
        }

        void printBike() {
            cout << "Frame: " << frame << endl;
            cout << "Wheels: " << wheels << endl;
            cout << "Handlebars: " << handlebars << endl;
        }
};

int main() {
    Bike stumpjumper;
    stumpjumper.setFrame("Specialized Stumpjumper Frame");
    stumpjumper.setWheels("Specialized Stumpjumper Wheels");
    stumpjumper.setHandlebars("Specialized Stumpjumper Handlebars");
    stumpjumper.printBike();

    return 0;
}
```

## Haskell

```
data Wheel = Wheel { hubDiameter :: Double, spokeLength :: Double, rimSize :: Double }

data Frame = Frame { frameSize :: Double, frameMaterial :: String }

data Bike = Bike { frontWheel :: Wheel, rearWheel :: Wheel, frame :: Frame }

buildWheel :: Double -> Double -> Double -> Wheel
buildWheel hubDiameter spokeLength rimSize = Wheel hubDiameter spokeLength rimSize

buildFrame :: Double -> String -> Frame
buildFrame frameSize frameMaterial = Frame frameSize frameMaterial

buildBike :: Wheel -> Wheel -> Frame -> Bike
buildBike frontWheel rearWheel frame = Bike frontWheel rearWheel frame

main :: IO ()
main = do
  let frontWheel = buildWheel 27 260 29 -- front wheel with hub diameter 27cm, spoke length 260cm, and rim size 29cm
  let rearWheel = buildWheel 27 260 29 -- rear wheel with the same specs as front wheel
  let frame = buildFrame 18 "aluminum" -- frame with size 18 inches and made of aluminum
  let bike = buildBike frontWheel rearWheel frame -- build the bike with the above parts
  putStrLn $ "Built a bike with front wheel hub diameter " ++ show (hubDiameter $ frontWheel bike) ++ "cm and frame size " ++ show (frameSize $ frame bike) ++ " inches"
```

## idris

```
module BikeBuilding

data Frame = Frame { model : String, size : Int, color : String }

data Wheel = Wheel { diameter : Double, spokeCount : Int, rimWidth : Double }

data Bike = Bike { frame : Frame, frontWheel : Wheel, rearWheel : Wheel }

buildBike : IO Bike
buildBike = do
    putStrLn "Building bike..."
    frame <- buildFrame
    frontWheel <- buildWheel
    rearWheel <- buildWheel
    let bike = Bike { frame = frame, frontWheel = frontWheel, rearWheel = rearWheel }
    putStrLn "Bike built!"
    return bike

buildFrame : IO Frame
buildFrame = do
    putStrLn "Building frame..."
    let frame = Frame { model = "Specialized Stumpjumper", size = 18, color = "red" }
    putStrLn "Frame built!"
    return frame

buildWheel : IO Wheel
buildWheel = do
    putStrLn "Building wheel..."
    let wheel = Wheel { diameter = 29.0, spokeCount = 32, rimWidth = 25.0 }
    putStrLn "Wheel built!"
    return wheel
```

# Shell Script

```
#!/bin/bash

# Define variables for the different parts of the bike
FRAME="Specialized Stumpjumper frame"
FORK="Fox Float 36 fork"
WHEELS="Specialized Roval Traverse carbon wheels"
DRIVETRAIN="SRAM GX Eagle drivetrain"
BRAKES="SRAM Guide RSC brakes"
HANDLEBAR="Specialized Trail handlebar"
STEM="Specialized Trail stem"
SEATPOST="Command Post IRcc dropper post"
SADDLE="Specialized Power saddle"
PEDALS="Shimano XT pedals"

# Assemble the bike
echo "Building a Specialized Stumpjumper mountain bike:"
echo "Step 1: Install the $FRAME"
echo "Step 2: Install the $FORK"
echo "Step 3: Install the $WHEELS"
echo "Step 4: Install the $DRIVETRAIN"
echo "Step 5: Install the $BRAKES"
echo "Step 6: Install the $HANDLEBAR and $STEM"
echo "Step 7: Install the $SEATPOST and $SADDLE"
echo "Step 8: Install the $PEDALS"
echo "Done! Your Specialized Stumpjumper mountain bike is ready to ride!"
```




