# File: main.py
# Version 1.0.0:
#   + Initial release | Date: 01.08.2016 | Author: Jim-Kristian Malmhaug
# About: VICTORY!

from victory import *

# Add background image to game window
background_image = games.load_image("background.bmp", transparent=False)
games.screen.background = background_image

# Insert victory object in screen
victory = Victory()
games.screen.add(victory)

games.screen.mainloop()
