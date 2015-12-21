# Project: Ch4E4_WordGuess
# Author: Jim-Kristian Malmhaug
# Date: 16 Des 2015

import random

word_count = 0

print("""
	
	              ***Welcome to the Word Guess Game***
	              	
	              	Guess the word by first asking the
	              	program for letters. You got five
	              	chances.
	
	""")

WORDS = ("Fantastic","Floor","Dance","Operation","Clean","Dirty","Smooth","Lovely","Run","Dog","Disco","Perks","Activate","Bus")

correct_word = random.choice(WORDS)

print("The word you have to guess has", len(correct_word), "letters. Type a letter to check the word for")

while (word_count < 5):
   letter = input("Letter ---> ")
   if letter.lower() in correct_word.lower():
      print("Yes!")
   else:
      print("No!")
   word_count = word_count + 1

answer = input("Now, guess the word ---> ")

if answer.lower() == correct_word.lower():
   print("CORRECT!")
else:
   print("WRONG! Too bad!\nThe word was", correct_word)