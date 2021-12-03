# Advent of Code 2021
# 03 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_csv('D:\GitHub\Advent-of-Code-2021\December 3\AoC_21_3_1.txt', dtype='string')
data = data['Data'].tolist()

totals = {'1_0': 0, '1_1': 0, '2_0': 0, '2_1': 0,'3_0': 0, '3_1': 0,'4_0': 0, '4_1': 0,'5_0': 0, '5_1': 0,}

for i in data:
    for u in range(1, 12):
        if i[u] == 0:
            totals[f'{u}_0'] += 1
        else:
            totals[f'{u}_1'] += 1
        
    
    
