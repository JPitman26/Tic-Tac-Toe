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

