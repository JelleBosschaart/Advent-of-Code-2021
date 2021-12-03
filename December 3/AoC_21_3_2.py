# Advent of Code 2021
# 03 December
# Part 2
# Jelle Bosschaart

import pandas as pd
import copy

org_data = pd.read_csv(r'C:\Users\jnbos\Documents\GitHub\Advent-of-Code-2021\December 3\AoC_21_3_1.txt', dtype='string')
data = copy.deepcopy(org_data)

# OGR
it = 0
while len(data) != 1:
    som = sum(list((data['Data'].str[it]).astype(int)))
    if som < len(data)-som:
        for i in data['Data']:
            if i[it] == '1':
                data = data.drop(data.loc[data['Data']==i].index)
    else:         
        for i in data['Data']:
            if i[it] == '0':
                data = data.drop(data.loc[data['Data']==i].index)
    it += 1   
OGR = str(data['Data'])

data = copy.deepcopy(org_data)

# CO2SR
it = 0
while len(data) != 1:
    som = sum(list((data['Data'].str[it]).astype(int)))
    if som < len(data)-som:
        for i in data['Data']:
            if i[it] == '0':
                data = data.drop(data.loc[data['Data']==i].index)
    else:
        for i in data['Data']:
            if i[it] == '1':
                data = data.drop(data.loc[data['Data']==i].index)
    it += 1
    
CO2SR = str(data['Data'])

OGR_b = 789
CO3SR_b = 3586

life_support_rating = OGR_b * CO3SR_b