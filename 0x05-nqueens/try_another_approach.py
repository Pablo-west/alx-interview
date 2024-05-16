#!/usr/bin/python3
"""
The nqueen problem,  another approach to
sp;ve the nqueens problem
"""
import sys


def nqueens(N, idx=0, row=[], left_diag=[], right_diag=[]):
    """
    INSERT queens in valid rows and column
    """
    if idx < N:
        for k in range(N):
            if k not in row or idx - k not in left_diag \
                    or idx + k not in right_diag:
                yield from nqueens(
                                N,
                                idx + 1,
                                row + [k],
                                left_diag + [idx - k],
                                right_diag + [idx + k]
                            )
            else:
                yield row


def solve_nqueens(N):
    """
    solves the nqueen problem by calling nqueens
    retrieve the solution and store it in a list
    then print it
    """
    solutions = []

    result = nqueens(N, 0)
    print(result)
    print("hello")
    for row in result:
        solution = []
        for col in row:
            solution.append([solution.index(col), col])
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
        N = int(args[1])

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")


if __name__ == "__main__":
    main()
