import random

# Define the game choices
choices = ["rock", "paper", "scissors"]

# Get the computer's choice
computer_choice = random.choice(choices)

# Get the player's choice
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors" \
   or player_choice == "paper" and computer_choice == "rock" \
   or player_choice == "scissors" and computer_choice == "paper":
    print("You win! The computer chose", computer_choice)
else:
    print("You lose! The computer chose", computer_choice)


