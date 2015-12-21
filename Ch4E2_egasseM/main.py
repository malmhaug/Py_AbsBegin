# Project Name: Ch4E2_egasseM
# Name: Jim-Kristian Malmhaug
# Date: 11 Des 2015

# Description: This program take an input message from the user and prints it backwards

message = str(input("Hey! Please enter a message: "))

print("\nThe message is backwards:\n")

for letter_nr in range(len(message), 0, -1):
    print(message[letter_nr-1])

input("\nPress Enter...")