def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in the given cell (row, col) on the board.

    Parameters:
        board (list): The N x N chessboard.
        row (int): Row index where the queen is to be placed.
        col (int): Column index where the queen is to be placed.
        N (int): Size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check diagonal from top-left to bottom-right
    for i in range(row):
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

    # Check diagonal from top-right to bottom-left
    for i in range(row):
        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False

    return True

def solve_n_queens(board, row, N):
    """
    Recursively solve the N-Queens problem using backtracking.

    Parameters:
        board (list): The N x N chessboard.
        row (int): Current row being considered.
        N (int): Size of the chessboard.

    Returns:
        None
    """
    if row == N:
        # All queens have been placed successfully
        for r in board:
            print(' '.join(map(str, r)))
        print()
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place a queen and explore further
            board[row][col] = 1
            solve_n_queens(board, row + 1, N)
            # Backtrack by removing the queen from the cell
            board[row][col] = 0

def n_queens(N):
    """
    Solve the N-Queens problem of size N.

    Parameters:
        N (int): Size of the chessboard.

    Returns:
        None
    """
    board = [[0] * N for _ in range(N)]  # Initialize an empty chessboard
    solve_n_queens(board, 0, N)  # Start solving from the first row

n_queens(4)  # Solve 4-Queens problem
