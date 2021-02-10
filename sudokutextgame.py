"""
Created on 12/2/2020

@author: Albert
"""

def checkcol(board, pos, num):
    row = pos[0]
    col = pos[1]
    for i in range(9):
        if row != i:  #check if comparing to self
            # check if same number in column
            if board[i][col] == num:
                return False
    return True

def checkrow(board, pos, num):
    row = pos[0]
    col = pos[1]
    for i in range(9):
        if col != i:  #check if comparing to self
            # check if same number in column
            if board[row][i] == num:
                return False
    return True


def checkbox(board, pos, num):
    row = pos[0]
    col = pos[1]
    for r in range(3):
        for c in range(3):
            if ((row//3)*3 + r, (col//3)*3 + c) != pos:
                if board[(row//3)*3 + r][(col//3)*3 + c] == num:
                    return False
    return True


def checks(board, pos, num):
    if checkrow(board, pos, num) and checkbox(board, pos, num) and checkcol(board, pos, num):
        return True
    return False

def numbersneeded(sudokuboard):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    missingnumbers = []
    for row in sudokuboard:
        tempnumbers = numbers
        missing = []
        for number in tempnumbers:
            if number not in row:
                missing.append(number)
        missingnumbers.append(missing)
    return missingnumbers

def printgrid(board):
    for i in range(9):
        print(board[i])
def emptysquare(board):
    for row in range(9):
        for col in range(9):
            if sudokuboard[row][col] == 0:
                return (row,col)
    return False

def solver(board):
    empty = emptysquare(board)
    if empty:
        row = empty[0]
        col = empty[1]
    else:
        return True
    missingnumbers = numbersneeded(board)
    missing_rownums = missingnumbers[row]
    for potential in missing_rownums:
        if checks(board, (row, col), potential) == True:
            board[row][col] = potential
            if solver(board):
                return True
            board[row][col] = 0
    return False


if __name__ == '__main__':
    """
     [[3, 5, 6, 9], 
     [1, 2, 3, 4, 8], 
     [2, 3, 4, 5, 9], 
     [1, 3, 5, 8, 9], 
     [2, 4, 6, 7, 8], 
     [1, 2, 3, 7, 8], 
     [4, 5, 6, 8, 9], 
     [3, 5, 6, 8, 9], 
     [1, 3, 5, 8]]
     """
    sudokuboard = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
                   [6, 0, 0, 0, 7, 5, 0, 0, 9],
                   [0, 0, 0, 6, 0, 1, 0, 7, 8],
                   [0, 0, 7, 0, 4, 0, 2, 6, 0],
                   [0, 0, 1, 0, 5, 0, 9, 3, 0],
                   [9, 0, 4, 0, 6, 0, 0, 0, 5],
                   [0, 7, 0, 3, 0, 0, 0, 1, 2],
                   [1, 2, 0, 0, 0, 7, 4, 0, 0],
                   [0, 4, 9, 2, 0, 6, 0, 0, 7]]
    solver(sudokuboard)
    print(printgrid(sudokuboard))
    #print(checkbox(sudokuboard, (0,2), 6))
    #print(checkcol(sudokuboard, (0,2), 7))
    #print(checkrow(sudokuboard, (0,2), 7))
    #print(numbersneeded(sudokuboard))
    #print(printgrid(solver(sudokuboard)))
    #print(checks(sudokuboard))
    #print(numbersneeded(sudokuboard))


    """
    sudokuboard = [[7, 8, 5, 4, 3, 9, 1, 2, 6],
                   [6, 1, 2, 8, 7, 5, 3, 4, 9],
                   [4, 9, 3, 6, 2, 1, 5, 7, 8],
                   [8, 5, 7, 9, 4, 3, 2, 6, 1],
                   [2, 6, 1, 9, 5, 8, 9, 3, 4],
                   [9, 3, 4, 1, 6, 2, 7, 8, 5],
                   [5, 7, 8, 3, 9, 4, 6, 1, 2],
                   [1, 2, 6, 5, 8, 7, 4, 9, 3],
                   [3, 4, 9, 2, 1, 6, 8, 5, 7]]
    """