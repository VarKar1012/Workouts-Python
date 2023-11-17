# Play Rock-Paper-Scissor game with computer.

import random

def playGame():
    # select a choice
    rpc = random.choice(["r", "p", "s"])
    print(f"Computer's choice is {rpc}")
    return rpc

def setWinner(userChoice, rpc):
    # define game rules
    # win: r>s, p>r, s>p 
    if(userChoice == "r" and rpc == "s") or \
    (userChoice == "p"  and rpc == "r") or \
    (userChoice == "s" and rpc == "p"):
        print("you wins")
    else:
        print("computer wins")

# driver code
feedBack = True
while(feedBack == True):
    userChoice = input("please enter your choice: rock(r), paper(p), scissor(s)\n")
    pcChoice = playGame()

    if userChoice != pcChoice:
        setWinner(userChoice, pcChoice)
        reply = input("Do you want to play again? yes / no?")
        feedBack = True if reply == "yes" else False
    else:
        print("Game tied. play again.")
