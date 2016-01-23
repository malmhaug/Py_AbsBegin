import random
from ask_number import ask_number

def guess_function():
    print("\tWelcome to 'GUESS MY NUMBER v1.03'!")
    print("\nI'm thinking about a number between 1 and 100.")
    print("Try to guess it in a few attempts as possible.\n")

# Set initial values
    the_number = random.randint(1, 100)
    tries = 1
    guess = None

# Guessing loop
    while guess != the_number:
        guess_number = int(input("Guess the number: "))
        guess = ask_number(guess_number, the_number)
        tries += 1

    print("\nYou guessed it! And it took you", tries, "tries\n")
    input("\n\nPress enter...")