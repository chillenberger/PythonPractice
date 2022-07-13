from re import S
from typing import ItemsView
import pandas as pd
from pandas import Timestamp

meta_file = 'StackOverflow/assets/meta.txt'

df=pd.DataFrame({
'Tech en Innovation Fonds': {0: '63.57', 1: '63.57', 2: '63.57', 3: '63.57', 4: '61.03', 5: '61.03', 6: 61.03}, 'Aandelen Index Fonds': {0: '80.22', 1: '80.22', 2: '80.22', 3: '80.22', 4: '79.85', 5: '79.85', 6: 79.85}, 
'Behoudend Mix Fonds': {0: '44.80', 1: '44.8', 2: '44.8', 3: '44.8', 4: '44.8', 5: '44.8', 6: 44.8}, 
'Neutraal Mix Fonds': {0: '50.43', 1: '50.43', 2: '50.43', 3: '50.43', 4: '50.37', 5: '50.37', 6: 50.37}, 
'Dynamisch Mix Fonds': {0: '70.20', 1: '70.2', 2: '70.2', 3: '70.2', 4: '70.04', 5: '70.04', 6: 70.04}, 
'Risicomijdende Strategie': {0: '46.03', 1: '46.03', 2: '46.03', 3: '46.03', 4: '46.08', 5: '46.08', 6: 46.08}, 
'Tactische Strategie': {0: '48.69', 1: '48.69', 2: '48.69', 3: '48.69', 4: '48.62', 5: '48.62', 6: 48.62}, 
'Aandelen Groei Strategie': {0: '52.91', 1: '52.91', 2: '52.91', 3: '52.91', 4: '52.77', 5: '52.77', 6: 52.77}, 
'Datum': {0: Timestamp('2022-07-12 18:00:00'), 1: Timestamp('2022-07-11 19:42:55'), 2: Timestamp('2022-07-12 09:12:09'), 3: Timestamp('2022-07-12 09:29:53'), 4: Timestamp('2022-07-12 15:24:46'), 5: Timestamp('2022-07-12 15:30:02'), 6: Timestamp('2022-07-12 15:59:31')}})

def save_to_last_run_datum(): 
    with open(meta_file, mode='w') as f: 
        print(pd.Timestamp.now())
        f.write(str(pd.Timestamp.now()))

def get_last_run_datum(): 
    with open(meta_file, mode='r') as f: 
        return f.read()

if __name__ == '__main__':
    last_run = get_last_run_datum()
    date = pd.Timestamp.strftime(Timestamp(last_run), "%Y-%m-%d")
    # print(date)

    # print(df.groupby(df['Datum'].dt.date).last())
    
    df1 = df.groupby(df.Datum.dt.strftime("%Y-%m-%d")).last()
    df1 = df.loc[df.groupby(df['Datum'].dt.date)['Datum'].idxmax()].reset_index()
    df3 = df.sort_values('Datum').groupby(df['Datum'].dt.date).last()
    print(df.sort_values('Datum', ascending=False).reset_index())