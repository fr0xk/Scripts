monthly_income = float(input("Enter your monthly income in INR: "))

annual_income = monthly_income * 12

if annual_income < 250000:

    income_class, housing, food, transportation, healthcare, education, entertainment, miscellaneous = "Low-Income Class", 0.35, 0.25, 0.15, 0.10, 0.10, 0.05, 0.05

elif annual_income < 500000:

    income_class, housing, food, transportation, healthcare, education, savings, entertainment, miscellaneous = "Lower-Middle Income Class", 0.30, 0.20, 0.15, 0.10, 0.10, 0.10, 0.05, 0.05

elif annual_income < 1000000:

    income_class, housing, food, transportation, healthcare, education, savings, entertainment, travel, miscellaneous = "Middle-Income Class", 0.25, 0.15, 0.15, 0.10, 0.10, 0.10, 0.10, 0.05, 0.05

elif annual_income < 2500000:

    income_class, housing, food, transportation, healthcare, education, savings, entertainment, travel, miscellaneous = "Upper-Middle Income Class", 0.20, 0.10, 0.10, 0.10, 0.10, 0.20, 0.10, 0.10, 0.10

else:

    income_class, housing, food, transportation, healthcare, education, savings, entertainment, travel = "High-Income Class", 0.15, 0.05, 0.05, 0.10, 0.05, 0.35, 0.10, 0.15

housing, food, transportation, healthcare, education, entertainment, miscellaneous = [round(monthly_income * percentage, 2) for percentage in (housing, food, transportation, healthcare, education, entertainment, miscellaneous)]

if 'savings' in locals():

    savings = round(monthly_income * savings, 2)

    print("\nYou belong to the", income_class, "and your budget allocation is:\nHousing and Utilities:", housing, "\nFood and Groceries:", food, "\nTransportation:", transportation, "\nHealthcare:", healthcare, "\nEducation:", education, "\nSavings and Investments:", savings, "\nEntertainment and Miscellaneous:", entertainment, "\nTravel:", travel, "\nMiscellaneous:", miscellaneous)

else:

    print("\nYou belong to the", income_class, "and your budget allocation is:\nHousing and Utilities:", housing, "\nFood and Groceries:", food, "\nTransportation:", transportation, "\nHealthcare:", healthcare, "\nEducation:", education, "\nEntertainment and Miscellaneous:", entertainment, "\nTravel:", travel, "\nMiscellaneous:", miscellaneous)

