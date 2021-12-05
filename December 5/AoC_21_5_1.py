# Advent of Code 2021
# 05 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

with open(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 5\AoC_21_5_1.txt', 'r') as f:
    lines = f.readlines()

xy1, xy2 = [], []

for iline in range(len(lines)):
    dot1, arrow, dot2 = lines[iline].index(','), lines[iline].index('->'), lines[iline].index(',', arrow, len(lines[iline]))
    xy1.append((int(lines[iline][0:dot1]), int(lines[iline][dot1+1:arrow-1])))
    xy2.append((int(lines[iline][arrow+3:dot2]), int(lines[iline][dot2+1:len(lines[iline])])))

# Coordinate system dimentions
x = 1000
y = 1000
coord_sys = [[0 for p in range(0, x)] for u in range(0, y)]

for iline in range(len(lines)):
    if (xy1[iline][0] == xy2[iline][0]):
        for y in range(min([xy1[iline][1], xy2[iline][1]]), abs(xy1[iline][1] - xy2[iline][1]) + min([xy1[iline][1], xy2[iline][1]]) + 1):
            coord_sys[y][xy1[iline][0]] += 1
    elif (xy1[iline][1] == xy2[iline][1]):
        for x in range(min([xy1[iline][0], xy2[iline][0]]), abs(xy1[iline][0] - xy2[iline][0]) + min([xy1[iline][0], xy2[iline][0]]) + 1):
            coord_sys[xy1[iline][1]][x] += 1     
            
answer = 0
for i in coord_sys:
    part_answer = sum(np.array(i)>1)
    answer += part_answer
    
print(answer)