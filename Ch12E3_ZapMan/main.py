# File: main.py
# Version 1.0.0:
#   + Initial release | Date: 01.08.2016 | Author: Jim-Kristian Malmhaug
# About: A ZapMan game. Collect coins and stay away from enemies. Press SPACE button to zap away.

from zapman import *

if __name__ == '__main__':

    # Set the background
    background_image = games.load_image("background.bmp", transparent=False)
    games.screen.background = background_image

    # Kick of the game
    Game().play()

    # Catch the mouse pointer in screen
    games.screen.event_grab = True

    # Run continuously
    games.screen.mainloop()
