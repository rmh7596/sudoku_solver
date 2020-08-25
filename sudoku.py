#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
board = [
            [9,0,0,3,0,0,0,8,0],
            [0,0,7,0,1,0,0,0,0],
            [0,0,0,0,0,8,1,2,7],
            [7,6,5,0,0,1,0,0,0],
            [0,9,0,0,7,0,0,1,0],
            [0,0,0,4,0,0,3,7,5],
            [1,4,6,5,0,0,0,0,0],
            [0,0,0,0,8,0,2,0,0],
            [0,2,0,0,0,3,0,0,1]
        ]

def clone(board):
    new_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            row.append(board[i][j])
        new_board.append(row)
    return new_board



def is_valid(i, j,potential, board):
    print 'trying ', i, ', ', j

    if potential>9:
        return False

    # check to see if the number is in the
    # row to the right
    row = board[i]
    for x in row[j+1:]:
        if x  == potential:
            return False #not valid

    # check to see if the number is in the
    # row to the left
    row = board[i]
    for x in row[:j]:
        if x == potential:
            return False

    # check to see if the number is
    # in this column above
    for x in range(0, i):
        num  = board[x][j]
        if num == potential:
            return False

    # check to see if the number is
    # in this column from below
    for x in range(i+1, len(board)):
        num = board[x][j]
        if num == potential:
            return False

    #check to see if the number is
    #within the block
    def get_box(i,j):
     if i < 3 and j < 3:
         return 1
     if i < 3 and j > 2 and j < 6:
         return 2
     if i < 3 and j > 5 and j < 9:
         return 3
     if i > 2 and i < 6 and j < 3:
         return 4
     if i > 2 and i < 6 and j>2 and j<6:
         return 5
     if i > 2 and i < 6 and j > 5 and j < 9:
         return 6
     if i > 5 and i < 9 and j < 3:
         return 7
     if i > 5 and i < 9 and j > 2 and j < 6:
         return 8
     if i > 5 and i < 9 and j > 5 and j < 9:
         return 9
    box1 = board[0][0], board[0][1], board[0][2], board[1][0],board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]
    box2 = board[0][3], board[0][4], board[0][5], board[1][3],board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]
    box3 = board[0][6], board[0][7], board[0][8], board[1][6],board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]
    box4 = board[3][0], board[3][1], board[3][2], board[4][0],board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]
    box5 = board[3][3], board[3][4], board[3][5], board[4][3],board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]
    box6 = board[3][6], board[3][7], board[3][8], board[4][6],board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]
    box7 = board[6][0], board[6][1], board[6][2], board[7][0],board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]
    box8 = board[6][3], board[6][4], board[6][5], board[7][3],board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]
    box9 = board[6][6], board[6][7], board[6][8], board[7][6],board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]
    if get_box(i,j) == 1:
        for x in box1:
            if x == potential:
                return False
    if get_box(i,j) == 2:
         for x in box2:
             if x == potential:
                 return False
    if get_box(i,j) == 3:
         for x in box3:
             if x == potential:
                 return False

    if get_box(i,j) == 4:
         for x in box4:
             if x == potential:
                 return False
    if get_box(i,j) == 5:
         for x in box5:
             if x == potential:
                 return False
    if get_box(i,j) == 6:
         for x in box6:
             if x == potential:
                 return False
    if get_box(i,j) == 7:
         for x in box7:
             if x == potential:
                 return False
    if get_box(i,j) == 8:
         for x in box8:
             if x == potential:
                 return False
    if get_box(i,j) == 9:
         for x in box9:
             if x == potential:
                 return False


def solve(i,j,board):
    if i<9:
        if j <9:
            if board[i][j] == 0:
                for val in range(0,10):
                    if is_valid(i,j,val, board) != False:
                        # then place the number on the board
                        next_board = clone(board)
                        next_board[i][j] = val
                        success = solve(i,j+1,next_board)
                        if success != None:
                            return success
                return None

            else:
                return solve(i,j+1, board)
        else:
            return solve(i+1,0,board)
    else:
        return board

def sudoku(board):
    solution = solve(0,0,board)
    print(np.matrix(solution))

sudoku(board)



