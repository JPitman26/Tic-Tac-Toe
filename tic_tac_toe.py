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

