#!/usr/bin/python3
"""N Queens puzzle solver using backtracking."""
import sys


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, board, row, solutions):
    """Solve N queens using backtracking."""
    if row == n:
        # Convert board to required format
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, board, row + 1, solutions)
            board[row] = -1  # Backtrack


def main():
    """Main entry point for N Queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
