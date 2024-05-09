# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments
import os
import random
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
print("As you walk into the forest,you see a beautiful white castle \n")
response = ""
while response not in yes_no:
    response = input("would you like to journey toward the castle? \nyes/no\n")
    if response == "yes":
        print("As you walk toward the castle, you encounter an old, scary looking bridge.")
    elif response =="no":
        print("Thanks for playing.")
        quit()
    else:
        print("Please try again")
    if response == "yes":
        response = input("As you start to cross the bridge, you see an angry troll warning you to turn back. \nWould you like to continue crossing? \nyes/no\n")
    elif response == "no":
        print("you are no fun, goodbye!")
        quit()
    else:
        print("I didn't understand that.\n")
    if response == "yes":
        print("You have successfully crossed the bridge, and you are on you're way to the castle!")
    

    print("After crossing the bridge, you notice the troll is still staring at you omeniously n\You see a pile of small rocks.")
    response = input("Would you like to throw a rock at the troll? \nyes/no\n")
    if response == "yes":
        rock = input("would you like to throw a small or large rock? s/l")
        if rock == "l":
            print("You hit the troll in the head and he stops looking at you.  You continue on you're way to the castle.")
        else:
            print("You throw the small rock and the troll keeps staring at you.")
    elif response == "no":
        print("You still go on your journey, but the troll keeps looking at you.")
    else:
        print("try again")
        quit()
    print("After the bridge, you see a large hornet's nest")
    response = input("would you like to knock down the nest? \nyes/no\n")
    if response == "yes":
        print("That was really stupid! The hornets sting you, now you have to go back across the bridge and deal with the troll again.")
        troll = input("You see the troll again.  Would you like to pass through or hit him with another rock: pass or rock")
        cross = random.randint(1,10)
        if troll == "pass":
            print("Let's see if you are fast enough to pass")
            if cross >= 5:
                print("You are faster than the troll")
            else:
                print("You are too slow, you shouldn't have messed with hornets.")
        elif troll == "rock":
            rock = random.randint(1,10)
            if rock >=5:
                print("You hit the troll again and get away.  You don't feel bad about the castle because you abused the troll")
            else:
                print("The troll eats your leg")
