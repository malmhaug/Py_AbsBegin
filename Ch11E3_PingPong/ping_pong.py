# File: ping_pong.py
# Version 1.0.0:
#   + Initial release
# Author: 22 July 2016 | Jim-Kristian Malmhaug

import random
from tools.livewires import games, color

width = 860  # Screen width
height = 720  # Screen height
games.init(screen_width=width, screen_height=height, fps=50)


class Ball(games.Sprite):
    """Ball object"""
    image = games.load_image("ball.bmp", transparent=True)

    def __init__(self, y=50, speed=1.5):
        super(Ball, self).__init__(image=Ball.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dy=speed)

    def update(self):
        """ Check if ball hits the edges """
        if self.left < 0:
            self.dx = -self.dx
        if self.right > games.screen.width:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
            self.dx = random.randrange(5)
        if self.bottom > games.screen.height:
            self.end_game()

    def handle_caught(self):
        """ Return ball if caught """
        self.dy = -self.dy

    def end_game(self):
        """ End the game """
        end_message = games.Message(value="GAME OVER! SCORE = {0}".format(Racket().score.value),
                                    size=70,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)

        games.screen.add(end_message)

class Racket(games.Sprite):
    """Racket object"""
    image = games.load_image("racket.bmp", transparent=False)
    score = games.Text(value=0, size=25, color=color.black,
                        top=5, right=games.screen.width - 10)
    games.screen.add(score)

    def __init__(self):
        super(Racket, self).__init__(image=Racket.image,
                                     x=games.mouse.x,
                                     bottom=games.screen.height-20)

    def update(self):
        """ Move mouse to x position """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Check if catches ball """
        for ball in self.overlapping_sprites:
           Racket.score.value += 10
           Racket.score.right = games.screen.width - 10
           ball.handle_caught()
