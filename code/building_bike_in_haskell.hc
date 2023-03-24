-- Define some types for the bike components

data Frame = Frame { material :: String, size :: Int }

data Fork = Fork { travel :: Int }

data Wheel = Wheel { diameter :: Int, rimWidth :: Int }

data Tire = Tire { width :: Int, aspectRatio :: Int }

data Brake = Brake { type :: String }

-- Define some values for the bike components

frame :: Frame

frame = Frame { material = "Carbon Fiber", size = 18 }

fork :: Fork

fork = Fork { travel = 140 }

frontWheel :: Wheel

frontWheel = Wheel { diameter = 29, rimWidth = 30 }

rearWheel :: Wheel

rearWheel = Wheel { diameter = 29, rimWidth = 30 }

frontTire :: Tire

frontTire = Tire { width = 2.3, aspectRatio = 29 }

rearTire :: Tire

rearTire = Tire { width = 2.3, aspectRatio = 29 }

frontBrake :: Brake

frontBrake = Brake { type = "Hydraulic Disc" }

rearBrake :: Brake

rearBrake = Brake { type = "Hydraulic Disc" }

-- Define a function to build the bike using the components

buildBike :: Frame -> Fork -> Wheel -> Wheel -> Tire -> Tire -> Brake -> Brake -> String

buildBike frame fork frontWheel rearWheel frontTire rearTire frontBrake rearBrake =

  "Congratulations, you have built a Specialized Stumpjumper with the following components:\n" ++

  "- Frame: " ++ (show $ material frame) ++ ", size " ++ (show $ size frame) ++ " inches\n" ++

  "- Fork: " ++ (show $ travel fork) ++ " mm of travel\n" ++

  "- Front Wheel: " ++ (show $ diameter frontWheel) ++ " inch diameter, " ++ (show $ rimWidth frontWheel) ++ " mm rim width, with a " ++ (show $ width frontTire) ++ "/" ++ (show $ aspectRatio frontTire) ++ " front tire and " ++ (show $ type frontBrake) ++ " brake\n" ++

  "- Rear Wheel: " ++ (show $ diameter rearWheel) ++ " inch diameter, " ++ (show $ rimWidth rearWheel) ++ " mm rim width, with a " ++ (show $ width rearTire) ++ "/" ++ (show $ aspectRatio rearTire) ++ " rear tire and " ++ (show $ type rearBrake) ++ " brake"

-- Call the buildBike function with the components

main :: IO ()

main = do

  putStrLn $ buildBike frame fork frontWheel rearWheel frontTire rearTire frontBrake rearBrake

