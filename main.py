import tkinter as tk
import random

# Define the main function that plays the game
def play_game(user_input):
    options = ["rock", "paper", "scissors"]
    computer_pick = random.choice(options)

    # Determine the winner
    if user_input == computer_pick:
        result = "Draw!"
    elif (user_input == "rock" and computer_pick == "scissors") or (user_input == "paper" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "paper"):
        result = "You won!"
    else:
        result = "You lost!"

    # Update the output label with the result and the computer's pick
    output_label.config(text=f"Computer picked {computer_pick}. {result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create the UI elements
instructions_label = tk.Label(root, text="Type Rock/Paper/Scissors and click Play:")
instructions_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

play_button = tk.Button(root, text="Play", command=lambda: play_game(input_entry.get().lower()))
play_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

# Start the main event loop
root.mainloop()
