# File: user_interface.py
# Version: 1.0.0
# Author: 16 May 2016 | Jim-Kristian Malmhaug

from tkinter import *
import random


class UserInterface(Frame):
    def __init__(self, master):
        super(UserInterface, self).__init__(master)
        self.grid()  # Use grid manager
        self.create_submit_button()
        self.create_guess_text_field()
        self.create_info_text_field()
        self.welcome_text_label()
        self.tries = 10
        self.correct_number = random.randint(1, 100)
        #print("Number is: " + str(self.correct_number))

    def welcome_text_label(self):
        Label(self, text='Welcome to Guess My Number \n\nEnter number in field and press submit!\n')\
            .grid(row=0, column=0, columnspan=2, sticky=W)

    def create_submit_button(self):
        Button(self, text="SUBMIT", command=self.guess).grid(row=2, column=1, sticky=W)

    def create_guess_text_field(self):
        self.guess_entry = Entry(self)
        self.guess_entry.grid(row=1, column=1, sticky=W)

    def create_info_text_field(self):
        self.info = Entry(self)
        self.info.grid(row=2, column=2, columnspan=2, sticky=W)
        self.info.insert(0, "Enter number!")
        self.info.config(state=DISABLED)

    def update_info_field(self):
        pass
        self.info.config(state=NORMAL)
        self.info.delete(0, END)
        self.info.insert(0, self.feedback)
        self.info.config(state=DISABLED)

    def guess(self):
        self.guess_number = self.guess_entry.get()
        print(self.guess_number)
        if int(self.tries) <= int(0):
            self.feedback = "Game Over"
        elif int(self.guess_number) == int(self.correct_number):
            self.feedback = "Correct"
        elif int(self.guess_number) < int(self.correct_number):
            self.tries -= 1
            self.feedback = "Higher, tries = {0}".format(self.tries)
        elif int(self.guess_number) > int(self.correct_number):
            self.tries -= 1
            self.feedback = "Lower, tries = {0}".format(self.tries)
        print(self.feedback)
        self.update_info_field()
