# File: games.py
# Version: 1.2.0 | Betting added
# About: Demonstrates module creation
# Modified: 20 March 2016 | Jim-Kristian Malmhaug

import sys

class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(question):
    """Ask a yes or no question."""
    try:
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response
    except ValueError as e:
        print("Value Error: {0}\nProgram ends".format(e))
        sys.exit(-1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def ask_number(question, low, high):
    """Ask for a number within a range."""
    try:
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response
    except ValueError as e:
        print("Value Error: {0}\nProgram ends".format(e))
        sys.exit(-1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

  
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
