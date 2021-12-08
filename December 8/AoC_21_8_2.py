# Advent of Code 2021
# 08 December
# Part 2
# Jelle Bosschaart

with open(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 8\AoC_21_8.txt', 'r') as f:
    lines = f.readlines()

inputD = [[] for x in range(len(lines))]
outputD = [[] for x in range(len(lines))]

for i in range(len(lines)):
    dash = lines[i].index("|")
    for u in lines[i][dash+2:].split(" "):
        outputD[i].append(''.join(sorted(u.rstrip())))
    for o in lines[i][:dash-1].split(" "):
        inputD[i].append(''.join(sorted(o.rstrip())))

lengths = [2, 4, 3, 7]
output_values = []

righttop = ''
lefttop = ''
top = ''
middle = ''
rightbottem = ''
leftbottem = ''
bottem = ''

for i in range(len(inputD)):
    inputL, outputL = inputD[i], outputD[i]
    len_six = []
    for inp in inputL:
        if len(inp) == 2:
            one = inp
        elif len(inp) == 3:
            seven = inp
        elif len(inp) == 4:
            four = inp
        elif len(inp) == 7:
            eight = inp
        elif len(inp) == 6:
            len_six.append(inp)
            
    for a in list(set(one) & set(seven)):
        top = a
    
    for ls in len_six:
        str(list((set(ls)) - set(list((set(ls) & set(aight)))))[0])
              
    
    
        
    print(one, four, seven, eight)