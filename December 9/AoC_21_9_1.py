# Advent of code 2021
# Jelle Bosschaart
# December 09
# Part 1

with open(r'D:\GitHub\Advent-of-Code-2021\December 9\AoC_21_9.txt', 'r') as f:
    lines = f.readlines()

total = 0

for y in range(len(lines)):
    lines[y] = (lines[y].rstrip('\n'))
    for x in range(len(lines[y])): 
        try: value = int(lines[y][x])
        except: continue
        if y-1 != -1:
            try: up = int(lines[y-1][x])
            except: up = 10
        else:
            up = 10
        try: down = int(lines[y+1][x])
        except: down = 10
        if x-1 != -1:
            try: left = int(lines[y][x-1])
            except: left = 10
        else:
            left = 10
        try: right = int(lines[y][x+1])
        except: right = 10
        #print("--------")
        #print(f"   {up}")
        #print(f" {left} {value} {right}")
        #print(f"   {down}")
        if value < up and value < down and value < left and value < right:
            #print("TRUE")
            total += value+1
print(total)