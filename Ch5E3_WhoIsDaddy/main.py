# Project: Ch5E3_WhoIsDaddy
# Author: Jim-Kristian Malmhaug
# Date: 30 Des 2015 

# About: This program lets the user build a son-father database

fatherDict = {"ole": "donald"} # Father dictonary
choice = None

while choice != 5:   
 
    # The menu
    print("\n*** Menu ***\n\nOption: \n\t1. Who's the daddy\n\t2. Remove son-father pair\
	        \n\t3. Add father-son pair\n\t4. Replace father\n\t5. Exit")

    choice = int(input("Enter choice: "))

    if choice is 1:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            print("\nYour father is", fatherDict[son])
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 2:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            del fatherDict[son]
            print("\nSon and father is gone")
        else:
            print("\nSon does not exist in the dictionary")
    if choice is 3:
        son = (input("Enter name of son: ")).lower()
        father = (input("Enter name of father: ")).lower()
        if not(son) in fatherDict:
            fatherDict[son] = father
            print("\nSon and father is added")
        else:
            print("\nSon exist in the dictionary")
    if choice is 4:
        son = (input("Enter name of son: ")).lower()
        if son in fatherDict:
            father = (input("Enter name of father: ")).lower()
            fatherDict[son] = father
            print("\nSon and father is united")
        else:
            print("\nSon does not exist in the dictionary")
