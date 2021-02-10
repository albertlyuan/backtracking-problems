"""
Created on 12/8/2020

@author: Albert
"""
def print_board(board):
    for lst in board:
        print(lst)
def initate_maze():
    maze = [
        [1,1,1,0],
        [1,0,1,1],
        [0,1,0,1],
        [1,1,1,1]
    ]
    row = 0
    col = 0
    blank_maze = [[0 for i in range(len(maze))] for j in range(len(maze))]
    blank_maze[0][0] = 1
    solver(maze, row, col, blank_maze)
    print_board(blank_maze)
def solver(maze, row, col, blank_maze):
    possible_moves = [[0,1],[1,0]]
    for move in possible_moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if valid_move(maze, new_row, new_col):
            blank_maze[new_row][new_col] = 1
            if solver(maze, new_row, new_col, blank_maze):
                return True
            blank_maze[new_row][new_col] = 0

    if row == len(maze)-1 and col == len(maze)-1:
        return True
    return False

def valid_move(maze, row, col):
    n = len(maze)
    if row >= 0 and row < n:
        if col >= 0 and col < n:
            if maze[row][col] == 1:
                return True
    return False


if __name__ == '__main__':
    initate_maze()

