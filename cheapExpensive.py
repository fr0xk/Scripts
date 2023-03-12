import csv

table_data = [

    ["Product", "Buying Cheap", "Buying Mid-Range", "Buying Premium"],

    ["Commuter Vehicle", "Good for new drivers, low-budget buyers or city use", "Good balance between cost and features, suitable for families", "Best performance, luxury and features, for enthusiasts"],

    ["Bicycle", "Good for beginners, short commutes or occasional use", "Ideal for regular cyclists or longer commutes", "Best performance, durability, and features, for professionals"],

    ["Motorcycle", "Good for new riders, low-budget buyers or city use", "Ideal for daily use, weekend rides or touring", "Best performance, luxury and features, for enthusiasts"],

    ["Laptop", "Good for basic computing tasks or first-time buyers", "Ideal for students or office use", "Best performance, design, and features, for professionals"],

    ["Camera", "Good for hobbyists, casual photography or beginners", "Ideal for enthusiasts or professionals", "Best image quality, features and durability, for experts"],

    ["Headphones", "Good for casual use, occasional music listeners", "Ideal for frequent use or audiophiles", "Best sound quality, comfort and features, for enthusiasts"],

    ["Watch", "Good for basic functions or occasional use", "Ideal for fitness tracking, notifications or style", "Best features, durability and design, for luxury buyers"],

    ["Wine", "Good for casual drinking or low-budget events", "Ideal for social events or gifting", "Best taste, quality, and rarity, for wine enthusiasts"],

    ["Running Shoes", "Good for occasional use or beginners", "Ideal for regular runners or fitness enthusiasts", "Best performance, comfort, and durability, for athletes"],

    ["Backpack", "Good for occasional use or light items", "Ideal for regular use or heavy items", "Best comfort, durability, and features, for travelers"],

    ["Kitchen Knife", "Good for occasional use or low-budget buyers", "Ideal for home cooks or culinary students", "Best sharpness, balance, and durability, for chefs"],

    ["Mattress", "Good for temporary use or low-budget buyers", "Ideal for regular use or people with back problems", "Best comfort, support, and durability, for quality sleep"],

    ["Smartphone", "Good for basic functions or low-budget buyers", "Ideal for regular use or advanced features", "Best performance, camera, and design, for tech enthusiasts"],

    ["Golf Clubs", "Good for beginners or low-budget players", "Ideal for regular players or mid-handicap golfers", "Best performance, precision and features, for pros"],

    ["Telescope", "Good for casual stargazing or beginners", "Ideal for astronomy enthusiasts or intermediate users", "Best image quality, magnification, and features, for experts"],

    ["Guitar", "Good for beginners or low-budget players", "Ideal for regular players or intermediate musicians", "Best sound quality, playability, and features, for pros"]

]

with open('product_table.csv', mode='w', newline='') as file:

    writer = csv.writer(file)

    writer.writerows(table_data)

