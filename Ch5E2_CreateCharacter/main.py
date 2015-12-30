# Project: Ch5E2_CreateCharacter
# Author: Jim-Kristian Malmhaug
# Date: 29 Des 2015

# About: This program lets the user build skills for a character in a RPG
print("""
	
	            ***The RPG character building program***
	            	
	               Add from a pool of points to four
	               different skills set for your hero
	            
	""")
	
pool = 30  # pool of points
strength = 0  # skill set strength
health = 0  # skill set health
wisdom = 0  # skill set wisdom
dexterity = 0  # skill set dexterity
choice = None  # the menu choice

while choice != 0:
   print("""
	
	         Choose an option:
	         
	               0. Exit
	               1. View skill points
	               2. Reduce skill points
	               3. Add skill points
	
	   """)
	   
   choice = int(input("Option: "))
   if choice == 0:
      print("Exited")
   elif choice == 1:
      print("""
      	
      	Skills:
      	
      	      Strength is {0}
      	      Health is {1}
      	      Wisdom is {2}
      	      Dexterity is {3}
      	      
      	      Skill pool is {4}
      	
      	""".format(strength, health, wisdom, dexterity, pool))
      	
   elif choice == 2:
      print("""
      	
      	Choose skill to reduce:
      	      
      	      0. Exit
      	      1. Strength
      	      2. Health
      	      3. Wisdom
      	      4. Dexterity
      	   
      	""")	
      reduce_choice = int(input("Choice: "))
      if reduce_choice is 0:
          print("Exited")
      elif reduce_choice is 1 and strength > 0:
          reduce_value = int(input("Reduce strength to -> "))
          if reduce_value < strength and reduce_value >= 0:
             pool = pool + (strength - reduce_value)
             strength = reduce_value
          else:
             print("Not valid entry")
      elif reduce_choice is 2 and health > 0:
          reduce_value = int(input("Reduce health to -> "))
          if reduce_value < health and reduce_value >= 0:
             pool = pool + (health - reduce_value)
             health = reduce_value
          else:
             print("Not valid entry")
      elif reduce_choice is 3 and wisdom > 0:
          reduce_value = int(input("Reduce wisdom to -> "))
          if reduce_value < wisdom and reduce_value >= 0:
             pool = pool + (wisdom - reduce_value)
             wisdom = reduce_value
          else:
             print("Not valid entry")
      elif reduce_choice is 4 and dexterity > 0:
          reduce_value = int(input("Reduce dexterity to -> "))
          if reduce_value < dexterity and reduce_value >= 0:
             pool = pool + (dexterity - reduce_value)
             dexterity = reduce_value
          else:
             print("Not valid entry")
      else:
          print("Not valid entry")
   
   elif choice == 3 and pool > 0:
      print("""
      	
      	Choose skill to add to:
      	      
      	      0. Exit
      	      1. Strength
      	      2. Health
       	      3. Wisdom
      	      4. Dexterity
      	   
      	""")	
      add_choice = int(input("Choice: "))
      if add_choice is 0:
          print("Exited")
      elif add_choice is 1 and strength < 30:
          add_value = int(input("Put strength to -> "))
          if add_value > strength and add_value <= 30:
             pool = pool - (add_value - strength)
             strength = add_value
          else:
             print("Not valid entry")
      elif add_choice is 2 and health < 30:
          add_value = int(input("Put health to -> "))
          if add_value > health and add_value <= 30:
             pool = pool - (add_value - health)
             health = add_value
          else:
             print("Not valid entry")
      elif add_choice is 3 and wisdom < 30:
          add_value = int(input("Put wisdom to -> "))
          if add_value > wisdom and add_value <= 30:
             pool = pool - (add_value - wisdom)
             wisdom = add_value
          else:
             print("Not valid entry")
      elif add_choice is 4 and dexterity < 30:
          add_value = int(input("Put dexterity to -> "))
          if add_value > dexterity and add_value <= 30:
             pool = pool - (add_value - dexterity)
             dexterity = add_value
          else:
             print("Not valid entry")
      else:
          print("Not valid entry")
