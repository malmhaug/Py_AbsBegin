# File: simon.py
# Version 1.0.0:
#   + Initial release | Date: 31.07.2016 | Author: Jim-Kristian Malmhaug
# About: A Simon says game.

from tools.livewires import games, color
import time
import random

games.init(screen_width=640, screen_height=480, fps=50)


class RedButton(games.Sprite):
    """ Red push button """
    image = games.load_image("red_button.bmp")

    red_message = games.Message(value=0,
                                size=50,
                                color=color.red,
                                x=games.screen.width/3 - 20,
                                y=games.screen.height/2 - 60,
                                lifetime=500 * games.screen.fps,
                                is_collideable=False)

    games.screen.add(red_message)

    def __init__(self):
        super(RedButton, self).__init__(image=RedButton.image,
                                        x=games.screen.width/3 - 20,
                                        y=games.screen.height/2)

    def update(self):
        # Get mouse position
        mouse_x, mouse_y = games.mouse.position

        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom and Simon().STATE:
            if games.mouse.is_pressed(0):
                RedButton().red_message.value += 1
                time.sleep(0.5)
            if games.mouse.is_pressed(2):
                RedButton().red_message.value -= 1
                if RedButton().red_message.value < 0:
                    RedButton().red_message.value = 0
                time.sleep(0.5)


class GreenButton(games.Sprite):
    """ Green push button """
    image = games.load_image("green_button.bmp")
    green_message = games.Message(value=0,
                                  size=50,
                                  color=color.green,
                                  x=games.screen.width/2,
                                  y=games.screen.height/2 - 60,
                                  lifetime=500 * games.screen.fps,
                                  is_collideable=False)

    games.screen.add(green_message)

    def __init__(self):
        super(GreenButton, self).__init__(image=GreenButton.image,
                                          x=games.screen.width/2,
                                          y=games.screen.height/2)

    def update(self):
        # Get mouse position
        mouse_x, mouse_y = games.mouse.position

        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom and Simon().STATE:
            if games.mouse.is_pressed(0):
                GreenButton().green_message.value += 1
                time.sleep(0.5)
            if games.mouse.is_pressed(2):
                GreenButton().green_message.value -= 1
                if GreenButton().green_message.value < 0:
                    GreenButton().green_message.value = 0
                time.sleep(0.5)


class BlueButton(games.Sprite):
    """ Blue push button """
    image = games.load_image("blue_button.bmp")

    blue_message = games.Message(value=0,
                                 size=50,
                                 color=color.blue,
                                 x=games.screen.width/3 + games.screen.width / 3 + 20,
                                 y=games.screen.height/2 - 60,
                                 lifetime=500 * games.screen.fps,
                                 is_collideable=False)

    games.screen.add(blue_message)

    def __init__(self):
        super(BlueButton, self).__init__(image=BlueButton.image,
                                         x=games.screen.width/3 + games.screen.width / 3 + 20,
                                         y=games.screen.height/2)

    def update(self):
        # Get mouse position
        mouse_x, mouse_y = games.mouse.position

        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom and Simon().STATE:
            if games.mouse.is_pressed(0):
                BlueButton().blue_message.value += 1
                time.sleep(0.5)
            if games.mouse.is_pressed(2):
                BlueButton().blue_message.value -= 1
                if BlueButton().blue_message.value < 0:
                    BlueButton().blue_message.value = 0
                time.sleep(0.5)


class StartButton(games.Sprite):
    """ Start push button """
    image = games.load_image("start_button.bmp")
    button_pressed = False

    def __init__(self):
        super(StartButton, self).__init__(image=StartButton.image,
                                         x=games.screen.width / 2,
                                         y=50)

    def update(self):
        # Get mouse position
        mouse_x, mouse_y = games.mouse.position

        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom:
            if games.mouse.is_pressed(0):
                StartButton.button_pressed = True
                Simon().advance()
                Simon.STATE = True


class SendButton(games.Sprite):
    """ Send answer button """
    image = games.load_image("send_button.bmp")
    button_pressed = False

    def __init__(self):
        super(SendButton, self).__init__(image=SendButton.image,
                                         x=games.screen.width / 2,
                                         y=games.screen.height - games.screen.height / 4)

    def update(self):
        # Get mouse position
        mouse_x, mouse_y = games.mouse.position

        if self.left < mouse_x < self.right and self.top < mouse_y < self.bottom and Simon().STATE:
            if games.mouse.is_pressed(0):
                answer = [BlueButton.blue_message.value, RedButton.red_message.value, GreenButton.green_message.value]
                Simon().check_answer(answer)


class Simon(object):
    """ Game object for Simon """
    color_array = [0,0,0]
    STATE = False
    level = 0

    def __init__(self):
        """ Initiate game object """
        self.blue_sound = games.load_sound("blue_sound.wav")
        self.red_sound = games.load_sound("red_sound.wav")
        self.green_sound = games.load_sound("green_sound.wav")
        self.sound_array = [self.blue_sound, self.red_sound, self.green_sound]

    def advance(self):
        """ Continue to the next level """
        Simon.level += 1

        for number in range(self.level):
            color_number = random.randrange(3)
            new_bckgrnd = ["blue.bmp","red.bmp","green.bmp"][color_number]
            self.sound_array[color_number].play()
            games.screen.background = games.load_image(new_bckgrnd, transparent=False)
            Simon.color_array[color_number] += 1
            time.sleep(2.5)

        new_bckgrnd = games.load_image("background.bmp", transparent=False)
        games.screen.background = new_bckgrnd

    def check_answer(self, answer):
        if answer == Simon.color_array:
            self.correct()
            #print("Answer -> {0}\nCorrect -> {1}".format(answer,Simon.color_array))
        else:
            #print("Failed")
            self.failed()
        BlueButton.blue_message.value = 0
        GreenButton.green_message.value = 0
        RedButton.red_message.value = 0
        Simon.color_array = [0, 0, 0]
        Simon.STATE = False

    def correct(self):
        """ User entered correct colors """
        correct_message = games.Message(value="CORRECT!",
                                        size=30,
                                        color=color.black,
                                        x=150,
                                        y=350,
                                        lifetime=5 * games.screen.fps,
                                        is_collideable=False)

        games.screen.add(correct_message)

    def failed(self):
        """ User entered wrong colors """
        wrong_message = games.Message(value="GAME OVER! SCORE = {0}".format(Simon.level * 100 - 100),
                                      size=20,
                                      color=color.black,
                                      x=150,
                                      y=350,
                                      lifetime=7 * games.screen.fps,
                                      is_collideable=False,
                                      after_death=games.screen.quit)

        games.screen.add(wrong_message)
