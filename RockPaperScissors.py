#This is a Rock Paper Scissors game :)
import random

def aiChoice(): #This function generates the computers choice of Rock, Paper or Scissors
    x = random.randint(0,2)
    if x == 0:
        choice = "rock"
    if x == 1:
        choice = "paper"
    if x == 2:
        choice = "scissors"
    return choice


def gameLoop(choice): #Main Game Loop
    playerChoice = input("Choose Rock, Paper or Scissors ")
    playerChoice = playerChoice.lower()
    if playerChoice == "rock": #If the player chooses Rock
        if choice == "rock": print("AI chose Rock, DRAW")
        elif choice == "paper": print("AI chose Paper, YOU LOSE")
        elif choice == "scissors": print("AI chose Scissors, YOU WIN")
        
    elif playerChoice == "paper": #If the player chooses Paper
        if choice == "rock": print("AI chose Rock, YOU WIN")
        elif choice == "paper": print("AI chose Paper, DRAW")
        elif choice == "scissors": print("AI chose Scissors, YOU LOSE")
        
    elif playerChoice == "scissors": #If the player chooses Scissors
        if choice == "rock": print("AI chose Rock, YOU LOSE")
        elif choice == "paper": print("AI chose Paper, YOU WIN")
        elif choice == "scissors": print("AI chose Scissors, DRAW")
    
    else: print("Oops you did a fuckywucky") #If the player chose none of the options

    repeat = input("Would you like to play again? Y/N ") #Asks the user if they wanna play again
    if repeat == "Y" or repeat == "y":
        gameLoop(choice) #Repeats the game loop
    elif repeat == "N" or repeat == "n":
        exit() #Ends the program

print("Welcome to Rock, Paper, Scissors")
ai = aiChoice()
aiChoice()       
gameLoop(ai)