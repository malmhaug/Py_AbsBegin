# File: main.py
# Version 1.0.0:
#   + Initial release
# Author: 22 July 2016 | Jim-Kristian Malmhaug

from tools.livewires import games
from ping_pong import Racket, Ball

# Add background image to game window
bckgrnd = games.load_image("background.bmp", transparent=False)
games.screen.background = bckgrnd

# Add ball object
the_ball = Ball()
games.screen.add(the_ball)

# Add racket object
the_racket = Racket()
games.screen.add(the_racket)

# Hide mouse pointer
games.mouse.is_visible = False

# Lock mouse to game window
games.screen.event_grab = True

games.screen.mainloop()
