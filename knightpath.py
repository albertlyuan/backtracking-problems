"""
Created on 12/6/2020

@author: Albert
"""
def make_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    board[0][0] = 1
    return board
def print_board(board):
    for lst in board:
        print(lst)
def solver(board, row, col, turn):
    if turn == len(board)**2:
        return True

    move_x = [-2, -2, -1, -1, 1, 1, 2, 2]
    move_y = [1, -1, -2, 2, -2, 2, 1, -1]
    for move in range(8):
        new_row = row + move_x[move]
        new_col = col + move_y[move]
        if valid_move(board, new_row, new_col):
            turn += 1
            board[new_row][new_col] = turn
            if solver(board, new_row, new_col, turn):
                return True
            turn -= 1
            board[new_row][new_col] = 0
    return False

def valid_move(board, row, col):
    n = len(board)
    if row >= 0 and row < n:
        if col >= 0 and col < n:
            if board[row][col] == 0:
                return True
            return False
        return False
    return False


if __name__ == '__main__':
    n = 8
    row = 0
    col = 0
    turn = 1
    board = make_board(n)
    if solver(board, row, col, turn):
        print_board(board)
    else:
        print("false")
