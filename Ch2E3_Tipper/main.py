# Project Name: Ch2E3_Tipper
# Name: Jim-Kristian Malmhaug
# Date: 14 Oct 2015

# Description: Ask the user for the sum from the restaurant bill

bill = float(input("\nWhat is the total restaurant bill:  "))  # Converts user input value to a float data type

tip_15 = bill * 0.15  # Calculates 15 % tip
tip_20 = bill * 0.2  # Calculates 20 % tip

print("15 % tip is " + str(tip_15))  # Prints 15 % tip where tip_15 variable is converted to string
print("20 % tip is " + str(tip_20))  # Prints 20 % tip where tip_20 variable is converted to string
