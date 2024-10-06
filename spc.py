"""my input 
computer input
case:
    rock,rock = tie
    rock,paper = paper win
    rock,scissor = rock win

    paper,paper = tie
    paper,rock = paper win
    paper,scissor = scissor win

    scissor,scissor = tie
    scissor,paper = scissor win
    scissor,rock = rock win
"""

import random

#selection

item_list = ["rock","paper","scissor"]
my_choice = input("Enter rock,paper,scissor = ")

#random choice

com_choice = random.choice(item_list)

print(f"I choos {my_choice}, Computer choose {com_choice}")

#if else  condition

if my_choice == com_choice:
    print("Both choose same : Game Tie")
elif my_choice == "rock":
    if com_choice == "paper":
        print("Paper cover rock : Computer Win")
    else:
        print("rock smashes scissor : you Win")
elif my_choice == "paper":
    if com_choice == "rock":
        print("paper cover rock : you win")
    else:
        print("scissor cut the paper : computer win")
elif my_choice == "scissor":
    if com_choice == "rock":
        print("rock smashed scissor  : computer win")
    else:
        print("scissor cut the paper : you win")

else:
    print("error Please Enter a valid name ")
