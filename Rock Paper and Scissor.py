import random

options = ["Rock", "Paper", "Scissors"]

user = input("Enter Rock, Paper, or Scissors: ")

computer = random.choice(options)

print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}\n")

if user == computer:
    print("It's a tie!")
elif user == "Rock" and computer == "Scissors":
    print("You win!")
elif user == "Paper" and computer == "Rock":
    print("You win!")
elif user == "Scissors" and computer == "Paper":
    print("You win!")
else:
    print("Computer wins!")
