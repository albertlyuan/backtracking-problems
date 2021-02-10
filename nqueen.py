"""
Created on 12/11/2020

@author: Albert
"""


def make_board(n,debug):
    if debug:
        board = [[0 for i in range(n)] for j in range(n)]
    else:
        board = [[0 for i in range(n)] for j in range(n)]
    return board


def print_board(board):
    for lst in board:
        print(lst)


def valid_move(row, col, rows_used, posdiag_used, negdiag_used):
    if rows_used[row] > 0:
        return False
    if posdiag_used[row + col] > 0:
        return False
    if negdiag_used[row - col + 7] > 0:
        return False
    return True

def debugboard(board, row, col, action):
    letters = "abcdefgh"
    for r in range(len(board)):
        for c in range(len(board)):
            if r == row:
                if action == True:
                    board[r][c] += 1
                else:
                    board[r][c] -= 1
            if r+c == row + col:
                if action == True:
                    board[r][c] += 1
                else:
                    board[r][c] -= 1
            if r-c+7 == row-col+7:
                if action == True:
                    board[r][c] += 1
                else:
                    board[r][c] -= 1

    print("debugstart")
    print_board(board)
    print("debugend")



def solver(board, col, rows_used, posdiag_used, negdiag_used, debug):
    if col >= len(board):
        return True
    if col < len(board):
        for row in range(len(board)):
            if valid_move(row, col, rows_used, posdiag_used, negdiag_used):
                board[row][col] = 1
                rows_used[row] += 1
                posdiag_used[row + col] += 1
                negdiag_used[row - col + 7] += 1
                debugboard(debug, row, col, True)
                print("new")
                print_board(board)
                if solver(board, col + 1, rows_used, posdiag_used,
                          negdiag_used, debug):
                    return True
                board[row][col] = 0
                rows_used[row] -= 1
                posdiag_used[row + col] -= 1
                negdiag_used[row - col + 7] -= 1
                debugboard(debug, row, col, False)

    return False


if __name__ == '__main__':
    board = make_board(8, False)
    rows_used = []
    posdiag_used = []
    negdiag_used = []
    for i in range(len(board)):
        rows_used.append(0)
        for i in range(2):
            posdiag_used.append(0)
            negdiag_used.append(0)
    posdiag_used = posdiag_used[:len(board) * 2 - 1]
    negdiag_used = negdiag_used[:len(board) * 2 - 1]

    debug = make_board(8, True)
    print_board(debug)
    solver(board, 0, rows_used, posdiag_used, negdiag_used, debug)
    print("spacer")
    print_board(board)
