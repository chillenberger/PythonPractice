
import csv
import os
import pandas as pd
import matplotlib as mp
import random
import numpy as np

print(os.getcwd())
fileName = 'StackOverflow/assets/Untitled.csv'

data = pd.read_csv(fileName)
print(data)
data = data.fillna(method='ffill')
print(data)

random_df = pd.DataFrame(np.random.randint(0, 10, size=(10,4)), columns=['a','b','c','d'])

big = pd.concat([data, random_df], axis=1)
print(big[(big.c > 5) | (big.c < 2)])