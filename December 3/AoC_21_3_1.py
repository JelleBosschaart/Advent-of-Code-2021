# Advent of Code 2021
# 03 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 3\AoC_21_3_1.txt', dtype='string')
totals = []
gamma = []

for i in range(0, len(data['Data'][0])):
    totals.append(sum(list((data['Data'].str[i]).astype(int))))

totals = np.array(totals)
gamma = list(map(int, totals > len(data)/2))
epsilon = list(map(int, totals < len(data)/2))

gamma_d = 394
epsilon_d = 3701
power_consumption = gamma_d * epsilon_d