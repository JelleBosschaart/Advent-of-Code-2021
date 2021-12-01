# Advent of Code 2021
# 01 December
# Part 1
# Jelle Bosschaart

import pandas as pd
import numpy as np

data = pd.read_excel(r'C:\Users\jnbos\Downloads\Advent of Code 2021\AoC_21_1_1.xlsx')
data = np.array(data)

last_elem = data[0]
counter = 0

for elem in data:
    if elem > last_elem:
        counter += 1
    last_elem = elem
        
print(counter)