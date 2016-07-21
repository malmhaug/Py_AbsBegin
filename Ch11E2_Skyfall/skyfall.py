# File: arrow.py
# Version 1.0.0:
#   + Initial release
# Author: 21 July 2016 | Jim-Kristian Malmhaug

import random
from tools.livewires import games, color

width = 960
height = 750
games.init(screen_width=width, screen_height=height, fps=50)


class Arrow(games.Sprite):
    """Arrow object"""
    image = games.load_image("arrow.bmp")
    speed = 1
    nr_arrows = 0

    def __init__(self, x=300, y =90):
        '''Initialize Arrow object'''
        super(Arrow, self).__init__(image=Arrow.image, x=x, y=y, dy=Arrow.speed)

    def update(self):
        '''Destroy object if fallen to ground'''
        if self.bottom > games.screen.height:
            self.destroy()
            new_arrow = Arrow(random.randrange(width))
            games.screen.add(new_arrow)
            Arrow.speed += 0.3
            if Arrow.speed > 4:
                new_arrow = Arrow(random.randrange(width))
                games.screen.add(new_arrow)
                Arrow.speed = 1

    def caught(self):
        '''Destroy object if hitting player'''
        self.destroy()

    def end_game(self):
        """ End the game. """
        end_message = games.Message(value="THINGS ARE NOT GOING YOUR WAY!",
                                    size=60,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Player(games.Sprite):
    """The Player object"""
    image = games.load_image("player.bmp")

    def __init__(self):
        '''Initialize Player object'''
        super(Player, self).__init__(image=Player.image, x=games.mouse.x, bottom=games.screen.height)

    def update(self):
        """ Move to mouse x position. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Check if catch pizzas. """
        for arrow in self.overlapping_sprites:
            arrow.caught()
            arrow.end_game()
