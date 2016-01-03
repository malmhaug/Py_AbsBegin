# Project: Ch5E4_WhoIsDaddyV2
# Author: Jim-Kristian Malmhaug
# Date: 01 Jan 2016

# About: This program lets the user build a son-father database
#        V2.00 - Added grandfather function

fatherDict = {"ole": ["donald", "Scrooge"]} # Father dictonary
choice = None

while choice != 0:   
 
    # The menu
    print(""" 
    	            *** Menu ***
    	            	
    	      Option:
    	              0. Exit
    	              1. Who's the daddy
    	              2. Who's the grandfather
    	              3. Remove son-father-grandfather pair
    	              4. Add son-father-grandfather pair
    	              5. Replace father
    	              6. Replace grandfather
	        """)

    choice = int(input("Enter choice: "))

    if choice is 1:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            print("\nYour father is", fatherDict[son][0])
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 2:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            print("\nYour grandfather is", fatherDict[son][1])
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 3:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            del fatherDict[son]
            print("\nSon, father and grandfather is gone")
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 4:
        son = (input("Enter name of son: ")).lower()
        father = (input("Enter name of father: ")).lower()
        grandfather = (input("Enter name of grandfather: ")).lower()
        if not(son) in fatherDict:
            fatherDict[son] = [father, grandfather]
            print("\nSon, father and grandfather is added")
        else:
            print("\nSon exist in the dictionary")
    if choice is 5:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            father = (input("Enter name of father: ")).lower()
            fatherDict[son][0] = father
            print("\nSon and father is united")
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 6:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            grandfather = (input("Enter name of grandfather: ")).lower()
            fatherDict[son][1] = grandfather
            print("\nSon and grandfather is united")
        else:
            print("\nSon does not exist in the dictionary")