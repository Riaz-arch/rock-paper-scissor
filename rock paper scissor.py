import pygame
import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Create a label
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label.pack(pady=10)

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()