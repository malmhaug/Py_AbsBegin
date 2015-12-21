# Project Name: Ch3E3_GuessMyNumber_V1.01
# Name: Jim-Kristian Malmhaug
# Date: 19 Oct 2015

# Description: This program is a modified version of the Guess My Number program from the book

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

# Tries = 10

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it under 10 attempts.\n")

# set the initial values
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while (guess != the_number) and (tries < 10):
    if guess > the_number:
        print("Lower... You have " + str(10 - tries) + " left!")
    else:
        print("Higher... You have " + str(10 - tries) + " left!")

    guess = int(input("Take a guess: "))
    tries += 1

if tries >= 10:
    print("\nYou failed insanely!")
else:
    print("\nYou guessed it! The number was", the_number)
    print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
