# File: victory.py
# Version 1.0.0:
#   + Initial release | Date: 01.08.2016 | Author: Jim-Kristian Malmhaug
# About: VICTORY!

from tools.livewires import games
from app import *

games.init(screen_width=1024, screen_height= 840, fps=50)
import random


class Victory(games.Sprite):
    """ The Victory object """
    image = games.load_image("victory.bmp", transparent=True)

    def __init__(self, speed=1):
        super(Victory, self).__init__(image=Victory.image,
                                      x=games.screen.width/2,
                                      y=games.screen.height/2,
                                      dy=speed)

        # Initialize application window
        self.app = Application()

    def update(self):
        """ Check if object hits the edges """
        if self.left < 0:
            self.dx = -self.dx
        if self.right > games.screen.width:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
            self.dx = random.randrange(Application.speed)
        if self.bottom > games.screen.height:
            self.dy = -self.dy

        # Update the application window
        self.app.update()
