# Project Name: Ch3E2_100HeadsOrTails
# Name: Jim-Kristian Malmhaug
# Date: 19 Oct 2015

# Description: This is a program that simulate 100 times flipping a coin

import random

iteration = 0
coin = 0
head = 0
tail = 0

input("\n\nPress enter to flip the coin 100 times...")

while (iteration < 100):
    coin = random.randrange(2)  # Simulates that the coin is flipped
    if coin is 0:  # Coin is flipped to head
        head += 1
    elif coin is 1:  # Coin is slipped to tail
        tail += 1
    iteration += 1  # Count the iterations

print("\nYou got " + str(head) + " heads and " + str(tail) + " tails!")

input("\nPress enter...")
