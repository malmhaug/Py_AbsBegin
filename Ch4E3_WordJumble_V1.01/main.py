# Project Name: Ch4E3_WordJumble_V1.01
# Name: Jim-Kristian Malmhaug
# Date: 14 Des 2015

# Description: This program is an upgraded version of the "Word Jumble". Now with hints and scores

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create an empty variable for counting failed guesses
fail = 0

# create a sequence of words to chose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Start the game
print(
    """
            Welcome to Word Jumble!

        Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "" and fail < 4 or guess == "hint":
    if guess != "hint":
        print("Sorry, that's not it. Tip: write hint and get a hint")
        fail = fail + 1
    guess = input("Your guess: ")
    if guess == "hint":
        print("Hint: ", correct[:(len(correct)-3)])
        continue

if guess == correct:
    print("That's it! You guessed it\n")
    print("POINTS: ", (5-(fail)))
elif fail <= 5:
    print("Sorry, you guessed to many times")
    print("POINTS: 0")

print("Thanks for playing!")
input("\n\nPress Enter key to exit.")
