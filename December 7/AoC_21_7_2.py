# Advent of Code 2021
# 07 December
# Part 2
# Jelle Bosschaart

import numpy as np

def get_indu_fuel(travel):
    indu_fuel = 0
    for i in range(1, travel+1):
        indu_fuel += i
    return indu_fuel

def get_total_fuel(data, h_pos):
    total_fuel = 0
    for pos in data:
        indu_fuel = get_indu_fuel(abs(h_pos-pos))
        total_fuel += indu_fuel
    return total_fuel
        
with open(r'D:\GitHub\Advent-of-Code-2021\December 7\AoC_21_7_1.txt', 'r') as f:
    data = np.array(list(map(int, f.readlines()[0].split(','))))

last_pos = min(data)-1
last_fuel = get_total_fuel(data, min(data)-1)
for pos in range(min(data), max(data)):
    current_fuel = get_total_fuel(data, pos)
    if current_fuel > last_fuel:
        print(last_pos, last_fuel)
        break
    last_fuel = current_fuel
    last_pos = pos