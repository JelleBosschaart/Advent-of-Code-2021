# Advent of Code 2021
# 04 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

with open(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 4\AoC_21_4_1.txt', 'r') as f:
    numbers = list(map(int, f.readline().split(',')))
    lines = f.readlines()

# Function to check if the board has won
def check_board(board):
    verticals = [[] for x in range(0, len(board))]
    for line in board:
        if sum(line) == -50:
            return True
        for i in range(0,5):
            verticals[i].append(line[i])
    for line in verticals:
        if sum(line) == -50:
            return True
    return False

# Fixing the lines
for iline in range(len(lines)):
    line = lines[iline]
    if line == '\n':
        continue
    line = line.replace('\n', '').split(' ')
    lines[iline] = list(map(int, (filter(('').__ne__, line))))
del(iline, f, line)

lines = list(filter(('\n').__ne__, lines))
boards = [[] for x in range(0, len(lines)//5)]
board_counter = -1
win = False

# Creating the boards
for iline in range(len(lines)):
    line = lines[iline]
    if iline % 5 == 0:
        board_counter += 1
    boards[board_counter].append(line)
    
# Drawing the numbers and stopping at the first winner
for drawn_number in numbers:
    if win:
        break
    for board in boards:
        for iline in range(len(board)):
            line = board[iline]
            try:
                i = line.index(drawn_number)
            except:
                continue
            line[i] = -10
            amount_drawn = (board[iline].count(-10))
            if amount_drawn >= 1:
                win = check_board(board)
        if win == True:
            win_board = board
            last_drawn_number = drawn_number
            break
# Get the sum of the winning board and the answer
sum_win_board = 0
for iline in range(len(win_board)):
    line = list(filter((-10).__ne__, win_board[iline]))
    win_board[iline] = line
    sum_win_board += sum(line)
    
answer = last_drawn_number * sum_win_board
print(f"The last board to win has score {answer}!")