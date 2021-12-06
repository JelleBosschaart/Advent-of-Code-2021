# Advent of Code 2021
# 06 December
# Part 2
# Jelle Bosschaart

import numpy as np

with open(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 6\AoC_21_6_1.txt', 'r') as f:
    lines = f.readlines()
    
data = np.array(list(map(int, lines[0].split(','))))

def update_lanterfish(lanterfish):  
    old_0 = lanterfish[0]
    for age in range(len(lanterfish.keys())-1):
        lanterfish[age] = lanterfish[age+1]
    lanterfish[6] += old_0
    lanterfish[8] = old_0
    return lanterfish
    
# I had to make the process more efficient using a dictionairy, because the old script took way to long
lanterfish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for age in data:
    try:
        lanterfish[age] += 1
    except:
        lanterfish[age] = 1
        
days = 256
for day in range(days):
    lanterfish = update_lanterfish(lanterfish)
    
print(f'After {day+1} days, there are {(sum(lanterfish.values()))} lanterfish.')

