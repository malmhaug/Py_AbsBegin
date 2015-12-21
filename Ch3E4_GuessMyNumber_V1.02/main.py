# Project Name: Ch3E4_GuessMyNumber_V1.02
# Name: Jim-Kristian Malmhaug
# Date: 25 Oct 2015

# Description: This program is a modified version of the
# Guess My Number program from the book, with computer versus player

# Guess My Number - Computer guesser
#
# The user picks a random number between 1 and 100
# The computer tries to guess it.

# Tries = 10

# ---------------------------------------------------------------------------------
#                                   PSEUDO CODE
# ---------------------------------------------------------------------------------
# 1.  Welcome user and tell him/her what to do
# 2.  Store user input in the_number
# 3.  Set guess to 0
# 4.  Set tries to 1
# 5.  set low_guess to 1
# 6.  Set high_guess to 100
# 7.  Import random library
# 8.  While the computer has not guessed the number and tries are below 10
    # 8.1  Computer guess a number between low_guess value and high_guess value
    # 8.2  Print the guess
    # 8.3  If the guess is higher than the the_number
        # 8.3.1  Print lower text and inform of tries left
        # 8.3.2  Set high_guess to last guessed number minus one
    # 8.4  Else
        # 8.4.1  Print higher text and inform of tries left
        # 8.4.2  Set low_guess to las guessed number plus one
    # 8.5  Increment tries
# 9.  If tries is above or equal to 10
    # 9.1  Print failure text
# 10. If tries is below 10
    # 10.1 Print winner text and winner number
    # 10.2 Print tries
# 11. Print exit text, and ask for user enter input
# ---------------------------------------------------------------------------------

print("\tWelcome to 'Guess My Number'!")
print("\nThinking of a number between 1 and 100.")
print("The computer will try to guess your number in 10 tries.")

# set the initial values
the_number = int(input("Enter the number here: "))
guess = 0
tries = 1
low_guess = 1
high_guess = 100

import random

# guessing loop
while (guess != the_number) and (tries < 10):
    guess = random.randint(low_guess, high_guess)
    print(guess)
    if guess > the_number:
        print("Lower... Computer has " + str(10 - tries) + " left!")
        high_guess = guess - 1
    else:
        print("Higher... Computer has " + str(10 - tries) + " left!")
        low_guess = guess + 1
    tries += 1

if tries >= 10:
    print("\nThe computer failed insanely!")
else:
    print("\nThe computer guessed it! The number was", the_number)
    print("And it only took", tries, "tries!\n")

input("\n\nPress the enter key to exit.")