#!/usr/bin/python3
"""
This is an nqueen game, in this game no queen should
in the same row, column or diagonal with other queens
"""
import sys


def is_anAttackQueen(board, row, col):
    """
    this will check if a queen occupying a position
    is being attacked by another queen. this reflects in whether
    the the queens are in the same row, column or diagonal
    return:
        return true if the queens are in attacking positions
        else return false
    """
    for queens_row, queens_col in enumerate(board):
        # check if the queens are in the same row
        if queens_row == row:
            return True
        # check if they are in the same column
        if queens_col == col:
            return True
        # check if they are within a diagonal line
        if abs(queens_row - row) == abs(queens_col - col):
            return True
    return False


def solve_nqueens(board, row, n):
    """
    this will solve the problem of nqueen using backtracking
    """
    n = len(board)
    if n == row:
        print_board(board)
        return True

    for col in range(n):
        if not is_anAttackQueen(board, row, col):
            board[row] = col
            print_nqueens(board)
        solve_nqueens(board, col + 1):
    return False


def nqueens(n):
    """
    solves te nqueen problemm with the given value of n
    """
    # we first insert queens starting from the first row
    board = []
    if solve_nqueens(board, 0):
        print_board(board)


def print_board(board):
    print([[col for col in rows] for rows in board])


def main():
    """
    execution entry point
    """
    args = sys.argv
    if len(args) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(args[1])

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
