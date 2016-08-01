# File: zapman.py
# Version 1.0.0:
#   + Initial release | Date: 01.08.2016 | Author: Jim-Kristian Malmhaug
# About: Collect the coins and get away from enemies. Press SPACE button to zap away.

import math, random
from tools.livewires import games, color
import time

games.init(screen_width = 640, screen_height = 480, fps = 50)


class Wrapper(games.Sprite):
    """ A sprite that wraps around the screen. """
    def update(self):
        """ Wrap sprite around screen. """
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self. """
        self.destroy()


class Collider(Wrapper):
    """ A Wrapper that can collide with another object. """
    def update(self):
        """ Check for overlapping sprites. """
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy self """
        self.destroy()


class Enemy(Wrapper):
    """ An enemy which follows player across the screen. """
    images = games.load_image("enemy.bmp")

    SPEED = 1
    SPAWN = 1

    total =  0

    def __init__(self, game, x, y):
        """ Initialize enemy sprite. """
        Enemy.total += 1

        super(Enemy, self).__init__(
            image = Enemy.images,
            x = x, y = y,
            dx = random.choice([1, -1]) * Enemy.SPEED * random.random(),
            dy = random.choice([1, -1]) * Enemy.SPEED * random.random())

        self.game = game

    def die(self):
        super(Enemy,self).update()
        for sprite in self.overlapping_sprites:
            Coins.score -= 1
            sprite.die()


class ZapMan(Wrapper):
    """ The player's ZapMan. """
    image = games.load_image("zapman_90.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    VELOCITY_MAX = 3
    MISSILE_DELAY = 25

    def __init__(self, game, x, y):
        """ Initialize ZapMan sprite. """
        super(ZapMan, self).__init__(image = ZapMan.image, x = x, y = y)
        self.game = game

    def update(self):
        """ Rotate and thrust based on keys pressed. """
        super(ZapMan, self).update()

        # rotate based on left and right arrow keys
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= ZapMan.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += ZapMan.ROTATION_STEP

        # apply thrust based on up arrow key
        if games.keyboard.is_pressed(games.K_UP):
            # change velocity components based on ZapMan's angle
            angle = self.angle * math.pi / 180  # convert to radians
            self.dx += ZapMan.VELOCITY_STEP * math.sin(angle)
            self.dy += ZapMan.VELOCITY_STEP * -math.cos(angle)

            # cap velocity in each direction
            self.dx = min(max(self.dx, -ZapMan.VELOCITY_MAX), ZapMan.VELOCITY_MAX)
            self.dy = min(max(self.dy, -ZapMan.VELOCITY_MAX), ZapMan.VELOCITY_MAX)

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()

        # zap away if SPACE button is pressed
        if games.keyboard.is_pressed(games.K_SPACE):
            self.zap()

    def die(self):
        """ Destroy ZapMan and end the game. """
        self.game.end()
        super(ZapMan, self).die()

    def zap(self):
        # The zap text
        self.zap_message = games.Message(value="ZAP!",
                                         size=30,
                                         color=color.black,
                                         x=self.x,
                                         y=self.y,
                                         is_collideable=False,
                                         lifetime=2 * games.screen.fps)
        games.screen.add(self.zap_message)
        self.x = random.randrange(50,600)
        self.y = random.randrange(50,400)
        self.dx = 0
        self. dy = 0
        time.sleep(2)


class Coins(games.Sprite):
    """ The coin object """
    image = games.load_image("coin.bmp")
    score = 0
    number_coins = 0

    def __init__(self, game):
        """ Initialize coin object """
        super(Coins, self).__init__(image=Coins.image,
                                    x=random.randrange(20, 600),
                                    y=random.randrange(20, 400))
        self.game = game
        Coins.number_coins += 1

    def update(self):
        if Coins.number_coins <= 0:
            self.game.advance()

    def die(self):
        Coins.score += 1
        self.game.score.value = Coins.score
        Coins.number_coins -= 1
        games.screen.remove(self)


class Game(object):
    """ The game itself. """
    def __init__(self):
        """ Initialize Game object. """
        # set level
        self.level = 0

        # create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        # create player's ZapMan
        self.zapman = ZapMan(game = self,
                             x = games.screen.width/2,
                             y = games.screen.height/2)
        games.screen.add(self.zapman)

    def play(self):
        """ Play the game. """
        # Run game music
        games.music.load("background_music.mp3")
        games.music.play(loop=-1)

        # advance to level 1
        self.advance()

        # start play
        games.screen.mainloop()

    def advance(self):
        """ Advance to the next game level. """
        self.level += 1

        # amount of space around ZapMan to preserve when creating enemies
        BUFFER = 150

        # create new enemies and
        for i in range(self.level):
            # calculate an x and y at least BUFFER distance from ZapMan

            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # choose distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # calculate location based on distance
            x = self.zapman.x + x_distance
            y = self.zapman.y + y_distance

            # wrap around screen, if necessary
            x %= games.screen.width
            y %= games.screen.height

            # create the enemies for every 2nd time
            if i % 5 == 0:
                new_enemy = Enemy(game = self,
                              x = x, y = y)
                games.screen.add(new_enemy)

            # create the coins
            new_coin = Coins(game = self)
            games.screen.add(new_coin)

        # display level number
        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

    def end(self):
        """ End the game. """
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)
