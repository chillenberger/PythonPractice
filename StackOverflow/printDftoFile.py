import pandas as pd 
import numpy as np
import random

file_name = 'StackOverflow/assets/largeranddata.txt'
file_name_html = 'StackOverflow/assets/largeranddata.html'

def pretty_output(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', 3000, "expand_frame_repr", False): 
        with open(file_name, mode='w') as f:
            print(df, file=f, end='')

dict = {'Name': [random.choice(['a','b']) for x in range(10)],
    'Surface Gravity':list(range(10)),
    'Equilibrium Temperature':list(range(10)),
    'Scale Height':list(range(10)),
    'Transmission Difference':list(range(10))}

df = pd.DataFrame(dict)

df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
df['new_col'] = df['Surface Gravity']*df['Equilibrium Temperature']
print(df)
print(df.groupby('Name').sum())





