"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays against a computer that randomly selects its move,
with the game showing who won each round.
Add a score counter that tracks player and computer wins,
and allow the game to continue until the player types “quit”.
"""
import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

# GUI Application
def play(choice):
    global player_score, computer_score, ties

    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)

    if result == "player":
        player_score += 1
        result_label.config(text=f"You win! Computer chose {computer_choice}.")
    elif result == "computer":
        computer_score += 1
        result_label.config(text=f"You lose! Computer chose {computer_choice}.")
    else:
        ties += 1
        result_label.config(text=f"It's a draw! Computer also chose {computer_choice}.")

    # Update the detailed scoreboard
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score} | Ties: {ties}")

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
ties = 0

# Widgets
welcome_label = tk.Label(root, text="Welcome to Rock Paper Scissors!", font=("Arial", 14))
welcome_label.pack(pady=10)

score_label = tk.Label(root, text="Player: 0 | Computer: 0 | Ties: 0", font=("Arial", 12))
score_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white")
quit_button.pack(pady=10)

# Run the application
root.mainloop()