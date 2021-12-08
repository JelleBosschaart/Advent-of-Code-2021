# Advent of Code 2021
# 08 December
# Part 1
# Jelle Bosschaart

import numpy as np

with open(r'D:\GitHub\Advent-of-Code-2021\December 8\AoC_21_8.txt', 'r') as f:
    lines = f.readlines()
print(lines)
data = []
for i in range(len(lines)):
    dash = lines[i].index("|")
    print(lines[i])
    for u in lines[i][dash+2:].split(" "):
        data.append(u.rstrip())
        
print(data)   
lengths = [2, 4, 3, 7]
counter = 0

for i in data:
    if len(i) in lengths:
        counter += 1
print(counter)
