# Advent of Code 2021
# 02 December
# Part 2
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_excel('D:\GitHub\Advent-of-Code-2021\December 2\Data.xlsx')
data = data['Data'].tolist( )

y = 0
x = 0
aim = 0

for step in data:
    space = (step.index(" "))
    if step[:space] == 'forward':
        x += int(step[space+1:])
        y += aim * int(step[space+1:])
    if step[:space] == 'down':
        aim += int(step[space+1:])
    if step[:space] == 'up':
        aim -= int(step[space+1:])
        
print(x*y)