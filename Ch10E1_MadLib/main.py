# File: main.py
# Version: 1.0.0
# Author: 24 April 2016 | Jim-Kristian Malmhaug

from tkinter import Tk
from ui import Userinterface

root = Tk()
root.title = "MaD LiB Program"
app = Userinterface(root)
root.mainloop()
