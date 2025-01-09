# Module docstring
'''
This module contains the functions to solve a sudoku puzzle
'''

def is_valid(board, row, col, num):
    '''
    This is a helper function to check if a number can be placed in a cell
    '''
    for i in range(9):
        if num in (board[row][i], board[i][col]):
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_mrv(board):
    '''
    This is a helper function to find the cell with the minimum remaining values
    '''
    min_count = 10
    mrv_position = (-1, -1)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                count = sum(is_valid(board, row, col, num) for num in range(1, 10))
                if count < min_count:
                    min_count = count
                    mrv_position = (row, col)

    # print("MRV Position:", mrv_position)
    return mrv_position

all_boards = []

def solve_sudoku(board):
    '''
    This is the main function to solve the sudoku puzzle
    '''
    all_boards.append([row[:] for row in board])
    empty = find_mrv(board)
    if empty == (-1, -1):
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0

    return False
