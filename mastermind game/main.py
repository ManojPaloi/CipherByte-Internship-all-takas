import random
import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        
        self.number_length = 4  # Number of digits in the secret number
        self.secret_number = ''  # To store the secret number
        self.attempts = 0  # Number of attempts by Player 2
        self.player1_wins = 0
        self.player2_wins = 0
        
        # Load sound files for correct and incorrect guesses
        self.correct_sound = "correct.wav"
        self.incorrect_sound = "incorrect.wav"
        
        self.create_widgets()
        self.reset_game()
    
    def create_widgets(self):
        # Frame for Player 1
        frame_player1 = tk.LabelFrame(self.root, text="Player 1", font=("Arial", 12))
        frame_player1.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Instruction label for Player 1
        self.label_player1 = tk.Label(frame_player1, text="Set a 4-digit number (digits should be unique)", font=("Arial", 12))
        self.label_player1.pack(pady=10)
        
        # Entry field for Player 1 to set the number
        self.entry_number = tk.Entry(frame_player1, font=("Arial", 16), justify='center')
        self.entry_number.pack(pady=10)
        
        # Button for Player 1 to set the number
        self.button_set = tk.Button(frame_player1, text="Set Number", command=self.set_number, font=("Arial", 12))
        self.button_set.pack(pady=10)
        
        # Frame for Player 2
        frame_player2 = tk.LabelFrame(self.root, text="Player 2", font=("Arial", 12))
        frame_player2.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Instruction label for Player 2
        self.label_player2 = tk.Label(frame_player2, text="Make a guess", font=("Arial", 12))
        self.label_player2.pack(pady=10)
        
        # Entry field for Player 2 to make a guess
        self.entry_guess = tk.Entry(frame_player2, font=("Arial", 16), justify='center', state=tk.DISABLED)
        self.entry_guess.pack(pady=10)
        
        # Button for Player 2 to make a guess
        self.button_guess = tk.Button(frame_player2, text="Guess", command=self.make_guess, state=tk.DISABLED, font=("Arial", 12))
        self.button_guess.pack(pady=10)
        
        # Label to display feedback for Player 2
        self.label_feedback = tk.Label(frame_player2, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=10)
        
        # Label to display scoreboard
        self.label_score = tk.Label(self.root, text=f"Player 1: {self.player1_wins} | Player 2: {self.player2_wins}", font=("Arial", 12))
        self.label_score.pack(pady=10)
        
        # Button to reset the game
        self.button_reset = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=("Arial", 12))
        self.button_reset.pack(pady=10)
    
    def reset_game(self):
        self.secret_number = ''
        self.attempts = 0
        self.entry_number.config(state=tk.NORMAL, bg="white", fg="black")
        self.button_set.config(state=tk.NORMAL, bg="#4CAF50", fg="white")  # Green button
        self.entry_guess.config(state=tk.DISABLED, text='', bg="white", fg="black")
        self.button_guess.config(state=tk.DISABLED, bg="#4CAF50", fg="white")  # Green button
        self.label_player2.config(text="Make a guess", fg="black")
        self.label_feedback.config(text='', fg="black")
    
    def set_number(self):
        number = self.entry_number.get().strip()
        
        if len(number) != self.number_length or not number.isdigit() or len(set(number)) != self.number_length:
            messagebox.showerror("Error", f"Please enter a {self.number_length}-digit number with unique digits.")
            return
        
        self.secret_number = number
        self.entry_number.config(state=tk.DISABLED, bg="#f0f0f0")  # Light gray background
        self.button_set.config(state=tk.DISABLED)
        self.entry_guess.config(state=tk.NORMAL)
        self.button_guess.config(state=tk.NORMAL)
        self.label_player2.config(text="Make a guess")
    
    def make_guess(self):
        guess = self.entry_guess.get().strip()
        
        if len(guess) != self.number_length or not guess.isdigit() or len(set(guess)) != self.number_length:
            messagebox.showerror("Error", f"Please enter a {self.number_length}-digit number with unique digits.")
            return
        
        self.attempts += 1
        correct_digits, misplaced_digits = self.get_hint(guess)
        
        if correct_digits == self.number_length:
            messagebox.showinfo("Winner!", f"Player 2 guessed the number {self.secret_number} in {self.attempts} attempts!")
            self.player2_wins += 1
            self.update_scoreboard()
            self.reset_game()
        else:
            feedback = f"{correct_digits} correct digits in the correct position\n"
            feedback += f"{misplaced_digits} correct digits in the wrong position"
            self.label_feedback.config(text=feedback)
    
    def update_scoreboard(self):
        self.label_score.config(text=f"Player 1: {self.player1_wins} | Player 2: {self.player2_wins}")

    def get_hint(self, guess):
        correct_digits = sum(1 for i in range(self.number_length) if guess[i] == self.secret_number[i])
        correct_and_misplaced_digits = sum(min(guess.count(digit), self.secret_number.count(digit)) for digit in set(guess))
        misplaced_digits = correct_and_misplaced_digits - correct_digits
        return correct_digits, misplaced_digits

def main():
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
