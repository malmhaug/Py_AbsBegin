# File: character.py
# About: This is the file for the different characters in the game adventure game
# Version: 1.0.0 | Initial release
# Date: 20 March 2016 | Jim-Kristian Malmhaug


class Player(object):
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return self.location


if __name__ == '__main__':
    print("You're not supposed to run this file")
