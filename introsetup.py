'''
Setup file for Intro to Pandas.
Creates a pandas series and  DataFrame to be displayed on Kaggle
'''

import pandas as pd

def series_1():
    s1_data = [2098.71, 5356.83, 8987.65, 5634.12]
    s1 = pd.Series(data=s1_data)
    print(s1)
    print()

def series_2():
    s2_data = [2098.71, 5356.83, 8987.65, 5634.12]
    s2_idx = [2006, 2007, 2008, 2009]
    s2 = pd.Series(data=s2_data , index= s2_idx , name='Sales Data')
    print(s2)
    print()

def df_1():
    df1_data = {'Randwick Store': [2563.89, 2098.18, 3013.45, 3856.99] ,
                 'Maroubra Store': [1887.35, 2098.65, 2562.77, 3298.99]}
    df1 = pd.DataFrame(data = df1_data)
    print(df1.head())
    print()

def df_2():
    df2_data = {'Randwick Store': [2563.89, 2098.18, 3013.45, 3856.99],
                 'Maroubra Store': [1887.35, 2098.65, 2562.77, 3298.99]}
    df2_idx = [2006, 2007, 2008, 2009]
    df2 = pd.DataFrame(data=df2_data, index=df2_idx)
    print(df2.head())
    print()
