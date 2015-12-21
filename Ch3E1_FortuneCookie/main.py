# Project Name: Ch3E1_FortuneCookie
# Name: Jim-Kristian Malmhaug
# Date: 19 Oct 2015

# Description: This is a fortune cookie program with five outcomes

import random

input("\n\nWelcome to the fortune cookie program! Please press enter to see into the future...")

fortune = random.randrange(5) + 1  # Creates a random number from 1 to 6

if fortune == 1:
    print("You will get rich!")
elif fortune == 2:
    print("You will become broke, poor and miserable!")
elif fortune == 3:
    print("You will become famous!")
elif fortune == 4:
    print("You will loose your home and your family!")
elif fortune == 5:
    print("You will be the best!")

input("\nPress enter...")