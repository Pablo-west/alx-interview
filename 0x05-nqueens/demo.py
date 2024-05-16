#!/usr/bin/env python3
"""
 queens, no two queens in the same row, column or diagonal
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen in the given position
    Check row, column, and diagonals for conflicts
    Return True if safe, False otherwise
    """
    for queens in board:
        # check for row conflict
        if queens == row:
            return False
        # check for rows
        for queen in queens:
            # check for column coflict
            if queen == col:
                return false
            # check for diagonal conflic
            if queens == queen:
                return False
    return True

def solve_nqueens_util(board, row):
    """
    Recursive utility function to solve N-Queens
    Base case: All queens are placed successfully
    Backtrack and try different columns for the current row
    """
    for col in rows:
        if is_safe(board, col) == False:
            solve_nqueens_util(board, row - 1)
        solve_nqueens_util(board, row, col) = True

def solve_nqueens(n):
    board = []
    # Call the utility function to start solving
    for row in range(n):
        solve_nqueens_util(board, row)

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
