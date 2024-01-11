import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")

player_choice = input(
    "Enter... \n1 for Rock, \n 2 for Paper, or \n 3 for Scissors:\n\n"
)

player_choice = int(player_choice)

# User Choice Output
if player_choice < 1 or player_choice > 3:
    sys.exit(
        "You have entered wrong input. Please input number from range between 1 - 3."
    )
else:
    print("You Have Entered " + str(RPS(player_choice))[4:].title())


# Random Computer Choice
computer_choice = random.randint(1, 3)

# Computer Choice Output
print("Compoter Have Choosen " + str(RPS(computer_choice))[4:].title())

# Get Game Outcome
if player_choice == computer_choice:
    print("Draw! Play Again 🎮")
elif player_choice == 1 and computer_choice == 2:
    print("Computer Won 💻")
elif player_choice == 1 and computer_choice == 3:
    print("You Won 🎉")
elif player_choice == 2 and computer_choice == 1:
    print("You Win 🎉")
elif player_choice == 2 and computer_choice == 3:
    print("Computer Wins 💻")
elif player_choice == 3 and computer_choice == 1:
    print("Computer Wins 💻")
elif player_choice == 3 and computer_choice == 2:
    print("You Win 🎉")
