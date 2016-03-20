# File: locations.py
# About: This is the file for the different locations in the adventure game
# Version: 1.0.0 | Initial release
# Date: 20 March 2016 | Jim-Kristian Malmhaug

import sys


class Locations(object):
    def __init__(self):
        self.local_area = None

    def walk_to_mountain(self):
        self.local_area = "The mountain"
        return self.local_area

    def walk_to_sea(self):
        self.local_area = "The sea"
        return self.local_area

    def walk_to_forest(self):
        self. local_area = "The forest"
        return self.local_area

    def walk_home(self):
        self.local_area = "Home"
        print("You're now home. Thank you for the trip :-)")
        sys.exit()


if __name__ == '__main__':
    print("You're not supposed to run this file")
