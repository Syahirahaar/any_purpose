# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 12:30:14 2021

@author: Syahirahar
"""


import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/Syahirahar/Desktop/IDEAS ICERD_2000 (Responses) - Form Responses 1.csv')

#df.columns.values[3] = "q1"
#df["q1"].replace('', np.nan,inplace=True)
#df.dropna(subset=['q1'],inplace=True)


    
df.columns.values[2] = "Phonenum"
df.columns.values[26] = "gender"
df.columns.values[27] = "eth"
df.columns.values[28] = "age"
df.columns.values[29] = "edu"
df.columns.values[31] = "occ"
df.columns.values[32] = "income"

df1 = df[["Phonenum","gender","eth","age","edu","occ","income"]]

df1=df1.dropna()
    
    
df1["eth"] = df1["eth"].str.split("/").str[0]

df1["eth"] = [i.strip(' ').upper() for i in df1["eth"]]

df1.to_excel("C:/Users/Syahirahar/Desktop/enrich_icerd.xlsx")


