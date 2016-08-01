# File: app.py
# Version 1.0.0:
#   + Initial release | Date: 01.08.2016 | Author: Jim-Kristian Malmhaug
# About: VICTORY!

from tkinter import *


class Application(Tk):
    speed = 1

    """ The Application object """
    def __init__(self):
        super(Application, self).__init__()
        self.grid()
        self.create_multiplier()
        self.wm_title('VICTORY!')
        self.wm_iconbitmap('victory_icon.ico')

    def create_multiplier(self):
        Label(self, text='Speed + 1').grid(row=0, column=0, sticky=W)
        Button(self, text="+", command=self.increase_speed).grid(row=0, column=1, sticky=W)
        Label(self, text='Speed - 1').grid(row=1, column=0, sticky=W)
        Button(self, text="-", command=self.decrease_speed).grid(row=1, column=1, sticky=W)

    def increase_speed(self):
        Application.speed += 1
        if Application.speed > 5:
            Application.speed = 5
        print(Application.speed)

    def decrease_speed(self):
        Application.speed -= 1
        if Application.speed < 1:
            Application.speed = 1
        print(Application.speed)
