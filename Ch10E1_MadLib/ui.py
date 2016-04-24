# File: ui.py
# Version: 1.0.0
# Author: 24 April 2016 | Jim-Kristian Malmhaug

from tkinter import *

"""A class for the user interface"""


class Userinterface(Frame):
    def __init__(self, master):
        super(Userinterface, self).__init__(master)
        self.grid()  # Use grid manager
        self.create_button()
        self.create_label()
        self.create_textentry()
        self.create_checkbutton()
        self.create_radiobutton()
        self.create_submit_button()
        self.create_story_txt()
        self.create_frame()
        self.create_textbox()

    def create_button(self):
        pass

    def create_label(self):
        # Instruction label
        Label(self, text="Enter information for new story...").grid(row=0, column=0, columnspan=2, sticky=W)
        # Name label
        Label(self, text="Person name:").grid(row=1, column=0, sticky=W)
        # Plural noun label
        Label(self, text="Plural noun:").grid(row=2, column=0, sticky=W)
        # Verb label
        Label(self, text="Verb:").grid(row=3, column=0, sticky=W)
        # Check buttons label
        Label(self, text="Adjectives:").grid(row=0, column=3, sticky=W)
        # Radio buttons label
        Label(self, text="Body part:").grid(row=2, column=3, sticky=W)

    def create_textentry(self):
        # Name entry
        self.name_entry = Entry(self)
        self.name_entry.grid(row=1, column=1, sticky=W)
        # Plural noun entry
        self.noun_entry = Entry(self)
        self.noun_entry.grid(row=2, column=1, sticky=W)
        # Verb entry
        self.verb_entry = Entry(self)
        self.verb_entry.grid(row=3, column=1, sticky=W)

    def create_checkbutton(self):
        # Itchy check button
        self.is_itchy = BooleanVar()
        Checkbutton(self, text="itchy", variable=self.is_itchy).grid(row=1, column=2, sticky=W)
        # Joyous check button
        self.is_joyous = BooleanVar()
        Checkbutton(self, text="joyous", variable=self.is_joyous).grid(row=1, column=3, sticky=W)
        # Electric check button
        self.is_electric = BooleanVar()
        Checkbutton(self, text="electric", variable=self.is_electric).grid(row=1, column=4, sticky=W)

    def create_radiobutton(self):
        # Single body part variable
        self.body_part = StringVar()
        self.body_part.set(None)
        # Body part for radio buttons
        body_parts = ["bellybutton", "big toe", "medulla oblongata"]
        column = 2
        for part in body_parts:
            Radiobutton(self, text=part, variable=self.body_part, value=part).grid(row=3, column=column, sticky=W)
            column += 1

    def create_submit_button(self):
        Button(self, text="Click for story", command=self.tell_story).grid(row=8, column=0, sticky=W)

    def create_story_txt(self):
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self):
        # Get GUI values
        person = self.name_entry.get()
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "itchy, "
        if self.is_joyous.get():
            adjectives += "joyous, "
        if self.is_electric.get():
            adjectives += "electric, "
        body_part = self.body_part.get()

        # Create story
        story = "Aperson called "
        story += person
        story += " was interesting in finding the "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + ". "
        story += "A insane, "
        story += adjectives
        story += "peculiar feeling overwhelmed our hero. "
        story += "After all this time, the mission was finally over. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + ". "
        story += "The moral of the story? Look out what you "
        story += verb
        story += " for."

        # Display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

    def create_frame(self):
        pass

    def create_textbox(self):
        pass
