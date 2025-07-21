# Write a minigame of rock, paper, scissors
import random

userwins = 0
computerwins = 0
ties = 0

def play_rps():
    global userwins, computerwins, ties
    if userwins == 0 and computerwins == 0:
        print("Welcome to Rock, Paper, Scissors!")

    print("You can type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")  
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        return play_rps()
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        userwins += 1
    else:
        print("You lose!")
        computerwins += 1

    user_choice = input("Do you like continue playing?: ").lower()
    if user_choice == 'yes' or user_choice == 'y' or user_choice == 'continue':
        return play_rps()
    else:
        print("Thanks for playing!")
        print(f"Final Score - You: {userwins}, Computer: {computerwins}, Ties: {ties}")

play_rps()