# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
#Write your code below this line:


import random
while True:
    user_action = input("Please select (rock, paper, scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("computer chose +computer_action")
    if user_action == computer_action:
        print(f"\n You tie, both players selected {user_action}")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"\nYou are a genius {user_action} beats {computer_action}")
        else: print(f"\nPaper covers rock you lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print(f"\n{user_action}")