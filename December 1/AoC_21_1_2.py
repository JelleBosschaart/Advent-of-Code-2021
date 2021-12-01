# Advent of Code 2021
# 01 December
# Part 2
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\jnbos\Downloads\Advent of Code 2021\AoC_21_1_2.xlsx')
data = np.array(data)
last_sum = np.sum(data[0:3])
counter = 0 

for i in range(len(data)):
    current_sum = np.sum(data[i:i+3])
    if current_sum > last_sum:
        counter += 1
    last_sum = np.sum(data[i:i+3])