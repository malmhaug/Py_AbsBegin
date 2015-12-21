# Project Name: Ch4E1_CountMyNumber_V1.02
# Name: Jim-Kristian Malmhaug
# Date: 10 Des 2015

# Description: This program is a counting program. User inputs start, stop and amount to count.

number = 0

start = int(input("Welcome to the counter!\n\nPlease enter the number to start counting from: "))
stop = int(input("Please enter the number to stop counting: "))
amount = int(input("Please enter the amount for each counting: "))

print("\n\nCounting:")

for number in range(start, stop+1, amount):
    print(number)

input("\n\nThank you for counting! Press Enter")
