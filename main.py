import random

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
rounds_played = 0

print("Welcome to Rock, Paper, Scissors!")
player_name = input("Please enter your name: ")

while True:
    print(f"\nRound {rounds_played + 1} - {player_name}: {user_wins} | Computer: {computer_wins}\n")
    user_input = input("Type 'rock', 'paper', or 'scissors' to play or 'quit' to exit: ").lower()

    if user_input == "quit":
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissors") or (user_input == "paper" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "paper"):
        print(f"{player_name} wins!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

    rounds_played += 1

print(f"\nFinal score: {player_name}: {user_wins} | Computer: {computer_wins}")
print("Thank you for playing!")
