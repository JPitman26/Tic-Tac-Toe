import random
import tkinter as tk
from tkinter import messagebox

def print_board(board):
    """
    Prints the Tic-Tac-Toe board on the console.

    Args:
        board (list): A 2D list representing the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    Checks if a player has won the game.

    Args:
        board (list): A 2D list representing the Tic-Tac-Toe board.
        player (str): The player's symbol ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Checks if the Tic-Tac-Toe board is full.

    Args:
        board (list): A 2D list representing the Tic-Tac-Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_input(board, player, row, col):
    """
    Gets the input (row and column) from the player.

    Args:
        board (list): A 2D list representing the Tic-Tac-Toe board.
        player (str): The player's symbol ('X' or 'O').
        row (tk.IntVar): Variable to store the chosen row.
        col (tk.IntVar): Variable to store the chosen column.

    Notes:
        This function sets the row and col variables to 0 for 'X' player, 
        and for 'O' player, it generates random row and column values 
        to simulate the CPU's move. The actual CPU move is done in the 
        cpu_move function.
    """
    if player == "X":
        row.set(0)
        col.set(0)
    # No need for CPU move in this function

def cpu_move(board, player):
    """
    Simulates the CPU's move by generating random row and column values.

    Args:
        board (list): A 2D list representing the Tic-Tac-Toe board.
        player (str): The player's symbol ('X' or 'O').

    Returns:
        int: The chosen row for the CPU's move.
        int: The chosen column for the CPU's move.
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            print(f"CPU chose row {row + 1} and column {col + 1}")
            return row, col

def play_tic_tac_toe():
    """
    The main function to play the Tic-Tac-Toe game with a GUI.

    This function sets up the graphical user interface, handles player 
    input, and simulates the CPU's moves using the CPU_move function.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]

    def on_click(row, col):
        """
        Handles the player's move when a button on the GUI is clicked.

        Args:
            row (int): The row of the clicked button.
            col (int): The column of the clicked button.
        """
        if board[row][col] == " ":
            player = players[0]
            board[row][col] = player
            button = buttons[row * 3 + col]
            button.config(text=player, state=tk.DISABLED)

            if check_winner(board, player):
                print_board(board)
                messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
                root.quit()
                return

            if is_board_full(board):
                print_board(board)
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                root.quit()
                return

            row, col = cpu_move(board, players[1])
            button = buttons[row * 3 + col]
            button.config(text=players[1], state=tk.DISABLED)

            if check_winner(board, players[1]):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {players[1]} wins!")
                root.quit()
                return

            if is_board_full(board):
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                root.quit()
                return

    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("300x300")

    buttons = []
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text=" ", width=10, height=5, command=lambda row=i, col=j: on_click(row, col))
            button.grid(row=i, column=j)
            buttons.append(button)

    root.mainloop()

if __name__ == "__main__":
    play_tic_tac_toe()
