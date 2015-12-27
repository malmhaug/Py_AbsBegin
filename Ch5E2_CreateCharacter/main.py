# Project: Ch5E2_CreateCharacter
# Author: Jim-Kristian Malmhaug
# Date: 19 Des 2015

# About: This program lets the user build skills for a character in a RPG

print("""
	
	            ***The RPG character building program***
	            	
	               Add from a pool of points to four
	               different skills set for your hero
	            
	""")

pool = 30  # pool of points
skill_1 = 0  # skill set 1
skill_2 = 0  # skill set 2
skill_3 = 0  # skill set 3
skill_4 = 0  # skill set 4

while choice != 0:
   
   print("""
	
	         Choose an option:
	         
	               0. Exit
	               1. View skill points
	               2. Reduce skill points
	               3. Add skill points
	
	   """)
	   
   choice = input("Option: ")
   
   if choice == 0:
      break
   elsif choice == 1:
      print("""
      	
      	Skills:
      	
      	      skill 1 is {0}
      	      skill 2 is {1}
      	      skill 3 is {2}
      	      skill 4 is {3}
      	
      	""".format(skill_1, skill_2, skill_3, skill_4))
   elsif choice == 2:
      print("""
      	
      	Choose skill to reduce:
      	      
      	      0. Exit
      	      1. skill 1
      	      2. skill 2
      	      3. skill 3
      	      4. skill 4
      	   
      	""")
      	
      reduce_choice = input("Choice: ")
      # Code here!
      