# File: main.py
# Version: 1.0.0
# Author: 16 May 2016 | Jim-Kristian Malmhaug

from tkinter import Tk
from user_interface import UserInterface

root = Tk()
root.title = "Guess My Number"
app = UserInterface(root)
print("User Interface initialized")
root.mainloop()
