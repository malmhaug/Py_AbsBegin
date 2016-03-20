# File: main.py
# About: This is the main file for the adventure game
# Version: 1.0.0 | Initial release
# Date: 20 March 2016 | Jim-Kristian Malmhaug

from character import Player
from locations import Locations

def main():
    print("Welcome to the adventure game\nWhat will you do now?")

    option = -1
    walker = Player('Outside the house')
    area = Locations()
    while option != 4:
        print("""
                1.  Walk to the mountain
                2.  Walk to the sea
                3.  Walk to the forest
                4.  Walk home and quit the adventure
                99. Where am I?
              """)
        try:
            option = int(input("---> "))
        except ValueError as e:
            print("Error: ", e)

        if option == 1:
            walker.location = area.walk_to_mountain()
        if option == 2:
            walker.location = area.walk_to_sea()
        if option == 3:
            walker.location = area.walk_to_forest()
        if option == 4:
            walker.location = area.walk_home()
        if option == 99:
            print(walker)

if __name__ == '__main__':
    main()
