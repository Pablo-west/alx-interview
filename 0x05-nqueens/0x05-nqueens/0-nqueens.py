#!/usr/bin/python3
"""
This module creates and solves the nqueens logic, which is a puzze in which
nquens are placed in an nxn matrix (chessboard) in such a way that no queen
interfares or attacks the other queen,that
is no two queen are in the same row, column or diagonal
"""
import sys


global queen
queen = 1


def is_safe(board, row, col, N):
    """
    check if the current position (row, col)  is safe before inserting
    a queen, that is if inserting a queen at (row, col)
    will not cause an attack on other previous queens
    Args:
        Board (List): an N x N list of Lisf integers
        row (int): a list of integers, qn entry in board
        col (int): a single entry in row
        N: size of the Board
    """
    # for k in col will check from 0 to col - 1, effectively checking the
    # previous cols
    for k in range(col):
        # check for column safety
        if board[row][k] == queen:
            return False

    # check for Top-Right to Bottom-Left diagonal indexes
    TR_ROW = range(row, -1, -1)
    TR_COL = range(col, -1, -1)
    for row_diag, col_diag in zip(TR_ROW, TR_COL):
        if board[row_diag][col_diag] == queen:
            return False

    # check for Top-Left to Bottom-Right diagonal
    TL_ROW = range(row, N, 1)
    TL_COL = range(col, -1, -1)
    for row_diag, col_diag in zip(TL_ROW, TL_COL):
        if board[row_diag][col_diag] == queen:
            return False
    return True


def solve_nqueens(board, col, N):
    """
    This will attempt to find a solution to the nqueens puzzle
    by checking to find the best position to insert a queen
    if none is found it uses backtracking algorith to redo
    the previous insertion, then try another solution
    """
    # base condition: all queens were inserted
    if col == N:
        print_board(board)
        return True

    res = False
    for row in range(N):
        # if its safe to insert a queen in column, insert it
        # and move onto the next row to check if it too has a column
        # that can accept a queen
        if is_safe(board, row, col, N):
            board[row][col] = queen
            res = solve_nqueens(board, col + 1, N) or res
            # Backtrack: After attempting to place a queen and exploring
            # its subsequent columns, reset the current position (row, col) to,
            # 0 indicating that no queen can be placed here.
            # This allows the algorithm to explore other possibilities
            # and configurations.
            board[row][col] = 0

    return res


def nqueens(N):
    """
    this function solves the queen to any given number or size of
    the chessboard
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)
    return


def print_board(board):
    """
    displays list of solutiob to the chessboard game, per line
    """
    # range_board = range(len(board))
    solutions = []
    for p, row in enumerate(board):
        solution = []
        for k, col in enumerate(row):
            if col == queen:
                solution.append(p)
                solution.append(k)
        solutions.append(solution)
    print(solutions)


def main():
    """
    execution entry point
    """
    args = sys.argv
    if len(args) < 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
