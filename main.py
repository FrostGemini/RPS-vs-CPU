import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q o quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0=rock 1=paper 2=scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw!")
        continue

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!")
        continue

    elif user_input == "rock" and computer_pick == "rock":
        print("Draw!")
        continue

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_win, "times!")
print("The computer had", computer_wins, "times!")
print("Goodbye!")