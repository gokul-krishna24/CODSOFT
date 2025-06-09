import tkinter as tk
from tkinter import messagebox
import math


board = [' ' for _ in range(9)]

window = tk.Tk()
window.title("Tic-Tac-Toe: AI vs You")
buttons = []

def is_winner(player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def is_full():
    return ' ' not in board

def minimax(is_maximizing):
    if is_winner('X'):
        return 1
    elif is_winner('O'):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def click(index):
    if board[index] == ' ':
        board[index] = 'O'
        buttons[index].config(text='O', state='disabled')

        if is_winner('O'):
            messagebox.showinfo("Game Over", "You win!")
            window.quit()
        elif is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            window.quit()
        else:
            ai_turn()

def ai_turn():
    move = best_move()
    board[move] = 'X'
    buttons[move].config(text='X', state='disabled')

    if is_winner('X'):
        messagebox.showinfo("Game Over", "AI wins!")
        window.quit()
    elif is_full():
        messagebox.showinfo("Game Over", "It's a draw!")
        window.quit()


for i in range(9):
    btn = tk.Button(window, text=' ', font='Arial 20', width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

window.mainloop()
