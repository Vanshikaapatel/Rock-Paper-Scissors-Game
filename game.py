import random
import tkinter as tk
from tkinter import messagebox


user_score = 0
computer_score = 0


def determine_winner(user_choice):
    global user_score, computer_score

    
    choices = ['Rock', 'Paper', 'Scissors']
    
   
    computer_choice = random.choice(choices)

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    
    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    
  
    label_score.config(text=f"Score - You: {user_score}  Computer: {computer_score}")


def play_again():
    answer = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not answer:
        root.quit()


root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")


label_welcome = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=('Arial', 16))
label_welcome.pack(pady=10)


label_instruction = tk.Label(root, text="Choose your option:")
label_instruction.pack(pady=5)


button_rock = tk.Button(root, text="Rock", width=15, command=lambda: determine_winner('Rock'))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", width=15, command=lambda: determine_winner('Paper'))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: determine_winner('Scissors'))
button_scissors.pack(pady=5)


label_result = tk.Label(root, text="", font=('Arial', 12))
label_result.pack(pady=10)


label_score = tk.Label(root, text="Score - You: 0  Computer: 0", font=('Arial', 12))
label_score.pack(pady=10)


button_again = tk.Button(root, text="Play Again", command=play_again)
button_again.pack(pady=10)


root.mainloop()
