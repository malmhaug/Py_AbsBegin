# File: main.py
# About: Main program for the Critter farm
# Date: 5 March 2016 | Jim-Kristian Malmhaug

import random

from critter_caretaker import Critter

def main():
    crit_name = []
    crit = []
    choice = None

    critter_numbers = int(input("Enter how many critters you want\n---> "))

    for i in range(critter_numbers):
        crit_name.append(input("What do you want to name your critter number {0}?: ".format(i+1)))
        crit.append(Critter(crit_name[i], hunger=random.randint(0, 10)))

    while choice != "0":
        print("""
        Critter Farm

        0 - Quit
        1 - Listen to all your critters
        2 - Feed all your critters
        3 - Play with your critters
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to all critters
        elif choice == "1":
            for i in range(critter_numbers):
                crit[i].talk()

        # feed your critters
        elif choice == "2":
            food = 0
            print("1. Lollipop\n2. Snack\n3. Pizza\n4. Big Feast")
            food_choice = int(input("\nChoose food ---> "))
            if food_choice is 1:
                food = 1
            if food_choice is 2:
                food = 2
            if food_choice is 3:
                food = 4
            if food_choice is 4:
                food = 10
            for i in range(critter_numbers):
                crit[i].eat(food)

        # play with your critters
        elif choice == "3":
            fun = 0
            print("1. 10 min\n2. 30 min\n3. 1 hour\n4. 3 hour")
            play_time = int(input("\nChoose play time ---> "))
            if play_time is 1:
                fun = 1
            if play_time is 2:
                fun = 2
            if play_time is 3:
                fun = 4
            if play_time is 4:
                fun = 10
            for i in range(critter_numbers):
                crit[i].play(fun)

        elif choice == "99":
            for i in range(critter_numbers):
                print(crit[i])

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()

input("\n\nPress the enter key to exit.")