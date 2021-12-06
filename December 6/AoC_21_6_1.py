# Advent of Code 2021
# 06 December
# Part 1
# Jelle Bosschaart

import numpy as np

with open(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 6\AoC_21_6_1.txt', 'r') as f:
    lines = f.readlines()
    
data = np.array(list(map(int, lines[0].split(','))))

days = 80

def update_data(data):
    data = data - 1
    aantal = (sum(data==-1))
    data[data == -1] = 6
    data = np.append(data, [8] * aantal)
    return data

for day in range(days):
    data = update_data(data)

print(f'After {day} days, there dare {len(data)} lanterfish.')