
'''
Objective: The Sudoku Solver using the brute-force approach is a method to solve a Sudoku
puzzle by trying every possible number in each empty cell until the puzzle is
solved. The brute-force algorithm systematically fills in each cell with numbers
from 1 to 9 and checks if the puzzle remains valid after each placement. If a
placement leads to a valid state, the algorithm proceeds to the next empty cell.
If a placement leads to a contradiction, the algorithm backtracks and tries the
next number.
Here is a step-by-step explanation:
1. Find an Empty Cell: Locate the first empty cell in the Sudoku grid.
2. Try Numbers: Attempt to place each number from 1 to 9 in the empty
cell.
3. Check Validity: Verify that placing the number does not violate Sudoku
rules:
• No repeated numbers in the same row.
• No repeated numbers in the same column.
• No repeated numbers in the same 3x3 sub-grid.
4. Move to Next Cell: If the placement is valid, proceed to the next empty
cell.
5. Backtrack if Necessary: If a placement leads to an invalid state later,
undo the placement (backtrack) and try the next number.
6. Complete: Continue until the Sudoku puzzle is fully solved or all possibilities
are exhausted.


Author: Sarju S
Date: 30-11-2024
'''
def is_valid(board, row, col, num):
    """
    Check if placing `num` in board[row][col] is valid.
    """
    # Check the row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check the column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def find_empty_cell(board):
    """
    Find the first empty cell (represented by 0) in the board.
    Returns (row, col) or None if no empty cells are found.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using a simple brute-force approach.
    """
    # Find an empty cell
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        # No empty cells left; puzzle is solved
        return True

    row, col = empty_cell

    # Try placing numbers 1-9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number
            board[row][col] = num

            # Recursively try to solve the rest of the board
            if solve_sudoku(board):
                return True

            # Undo the placement 
            board[row][col] = 0

    return False

# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve and display the result
if solve_sudoku(board):
    print("Sudoku solved successfully!")
    for row in board:
        print(row)
else:
    print("No solution exists for the given Sudoku puzzle.")
