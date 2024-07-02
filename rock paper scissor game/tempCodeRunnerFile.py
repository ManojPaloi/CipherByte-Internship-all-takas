import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Initialize scores
user_score = 0
computer_score = 0

# Define fonts and colors
title_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 16)
button_font = ("Helvetica", 14)
highlight_color = "#ffcc00"
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_fg_color = "#ffffff"

# Create labels
title_label = tk.Label(root, text="Rock Paper Scissors", font=title_font, bg=bg_color, fg=highlight_color)
title_label.pack(pady=20)

score_label = tk.Label(root, text="Scores", font=label_font, bg=bg_color)
score_label.pack(pady=10)

score_frame = tk.Frame(root, bg=bg_color)
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="You: 0", font=label_font, bg=bg_color)
user_score_label.grid(row=0, column=0, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer: 0", font=label_font, bg=bg_color)
computer_score_label.grid(row=0, column=1, padx=20)

result_label = tk.Label(root, text="", font=label_font, bg=bg_color)
result_label.pack(pady=20)

# Create buttons
button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=button_font, width=10, bg=button_bg_color, fg=button_fg_color, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=button_font, width=10, bg=button_bg_color, fg=button_fg_color, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = tk.Button(button_frame, text="Scissors", font=button_font, width=10, bg=button_bg_color, fg=button_fg_color, command=lambda: play("Scissors"))
scissor_button.grid(row=0, column=2, padx=10)

# Create a label to show user's and computer's choices
choices_label = tk.Label(root, text="", font=label_font, bg=bg_color)
choices_label.pack(pady=20)

# Function to update scores
def update_scores():
    user_score_label.config(text=f"You: {user_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

# Function to play the game
def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    choices_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}")
    
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!")
        user_score += 1
    else:
        result_label.config(text="Computer Wins!")
        computer_score += 1

    update_scores()

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    choices_label.config(text="")
    result_label.config(text="")

reset_button = tk.Button(root, text="Reset Game", font=button_font, width=15, bg=highlight_color, fg="#000000", command=reset_game)
reset_button.pack(pady=20)

# Run the main loop
root.mainloop()
