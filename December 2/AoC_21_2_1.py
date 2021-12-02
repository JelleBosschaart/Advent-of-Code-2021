# Advent of Code 2021
# 02 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_excel('D:\GitHub\Advent-of-Code-2021\December 2\Data.xlsx')
data = data['Data'].tolist( )

y = 0
x = 0

for step in data:
    space = (step.index(" "))
    if step[:space] == 'forward':
        x += int(step[space+1:])
    if step[:space] == 'down':
        y += int(step[space+1:])
    if step[:space] == 'up':
        y -= int(step[space+1:])
        
print(x*y)