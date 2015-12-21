# Project Name: Ch2E4_CarSale
# Name: Jim-Kristian Malmhaug
# Date: 14 Oct 2015

# Description: Program which calculates the total price for a car, based on the car base price

base_price = float(input("\nEnter the base price for the car:  "))

tax = base_price * 0.30
car_license = base_price * 0.10
dealer_prep = 15000
destination_charge = 10000
total_price = base_price + tax + car_license + dealer_prep + destination_charge

print("Base Price : " + str(base_price))
print("Tax: " + str(tax))
print("Car License : " + str(car_license))
print("Dealer Preparation: " + str(dealer_prep))
print("Destination Charge: " + str(destination_charge))
print("\nTotal Price: " + str(total_price))