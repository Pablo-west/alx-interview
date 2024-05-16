#!/usr/bin/env python3
"""
N-Queens, no two queens in the same row, column or diagonal
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen in the given position
    Check row, column, and diagonals for conflicts
    Return True if safe, False otherwise
    """
    for queens_row, queens_col in enumerate(board):
        # Check for row conflict
        if queens_row == row:
            return False
        # Check for column conflict
        if queens_col == col:
            return False
        # Check for diagonal conflict
        if abs(queens_row - row) == abs(queens_col - col):
            return False
    return True

def solve_nqueens_util(board, row):
    """
    Recursive utility function to solve N-Queens
    Base case: All queens are placed successfully
    Backtrack and try different columns for the current row
    """
    n = len(board)
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            if solve_nqueens_util(board, row + 1):
                return True
            board.pop()

    return False

def solve_nqueens(n):
    board = []
    if solve_nqueens_util(board, 0):
        print("Solution exists:")
        for col in board:
            row = ["." for _ in range(n)]
            row[col] = "Q"
            print(" ".join(row))
    else:
        print("No solution exists.")

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()
