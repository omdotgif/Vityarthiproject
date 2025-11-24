import random

# List of possible choices
options = ["Rock", "Paper", "Scissors"]

# Get user's input
user_choice = input("Enter Rock, Paper, or Scissors: ")

# Computer's random choice
computer_choice = random.choice(options)

# Print choices
print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")
else:
    print("Computer wins!")