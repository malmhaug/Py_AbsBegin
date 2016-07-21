# File: main.py
# Version 1.0.0:
#   + Initial release
# Author: 21 July 2016 | Jim-Kristian Malmhaug

from tools.livewires import games
from skyfall import Arrow, Player

wall_image = games.load_image("background.bmp", transparent=False)
games.screen.background = wall_image

the_arrow = Arrow()
games.screen.add(the_arrow)

the_player = Player()
games.screen.add(the_player)

games.mouse.is_visible = False

games.screen.event_grab = True
games.screen.mainloop()
