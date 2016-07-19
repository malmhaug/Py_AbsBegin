# File: main.py
# Version 1.1.0:
#   + Added difficulty, pizzas speed up after 100 points
#   + Add new face on chef
# Author: 19 July 2016 | Jim-Kristian Malmhaug

from tools.livewires import games, color
from pizza_panic import Chef, Pan

""" Play the game. """
wall_image = games.load_image("wall.jpg", transparent = False)
games.screen.background = wall_image

the_chef = Chef()
games.screen.add(the_chef)

the_pan = Pan()
games.screen.add(the_pan)

games.mouse.is_visible = False

games.screen.event_grab = True
games.screen.mainloop()
