'''
Basic Rules:
The game has three choices: Rock, Paper, and Scissors.
Two players (or a player and the computer) each choose one option.
The winner is determined based on the interaction of the two chosen options.
Winning Combinations:
Rock beats Scissors: Rock crushes Scissors, so Rock wins.
Scissors beats Paper: Scissors cut Paper, so Scissors win.
Paper beats Rock: Paper wraps Rock, so Paper wins.
Tie:
If both players choose the same option (e.g., Rock vs. Rock), it’s a tie, and no one wins.


Author: Sarju S
Date: 14-11-2024
'''
import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Game loop
while True:
    # Get player's choice
    player_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if player_choice == "quit":
        print("Thanks for playing!")
        break

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # Get computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    print()  # Print a blank line for readability
