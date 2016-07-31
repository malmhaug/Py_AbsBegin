# File: main.py
# Version 1.0.0:
#   + Initial release | Date: 31.07.2016 | Author: Jim-Kristian Malmhaug
# About: A Simon says game.

from simon import *

if __name__ == '__main__':

    # Set the background
    bck_image = games.load_image("background.bmp", transparent=False)
    games.screen.background = bck_image

    games.screen.add(StartButton())
    games.screen.add(BlueButton())
    games.screen.add(GreenButton())
    games.screen.add(RedButton())
    games.screen.add(SendButton())

    # Catch the mouse pointer in the screen
    games.screen.event_grab = True

    games.screen.mainloop()