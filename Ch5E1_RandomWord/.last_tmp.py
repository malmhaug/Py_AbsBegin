# Project: Ch5E1_RandomWord
# Author: Jim-Kristian Malmhaug
# Date: 19 Des 2015

import random

random_list = []
WORDS = ["Smooth","Run","Little","Dady","Hunter","Pog","Art","Question"]
print("\n\nOriginal list of words:", WORDS)

while WORDS:
   word = random.choice(WORDS)
   random_list.append(word)
   WORDS.remove(word)

print("\n", random_list)