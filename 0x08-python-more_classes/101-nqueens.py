#!/usr/bin/python3
import sys
"""Module for N queens puzzle"""


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 values
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        """checks if it's safe to place a queen at a specific position
        on the board"""
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def add_solution():
        """responsible for adding a valid solution to the list of solutions"""
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        solutions.append(solution)

    def place_queen(row):
        """function is a recursive function that tries to place the
        queens on the board row by row"""
        if row == n:
            add_solution()
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row + 1)

    place_queen(0)

    return solutions


# Main program
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sus.exit(1)

solutions = solve_nqueens(N)

for solution in solutions:
    print(solution)
