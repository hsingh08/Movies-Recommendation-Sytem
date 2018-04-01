#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:25:08 2018

@author: yash.joshi
"""

import pandas as pd
import ast
from collections import Counter

xl = pd.ExcelFile("/Users/yash.joshi/Desktop/harmeet/filtered_data.xlsx")
xl.sheet_names
df = xl.parse("Sheet1")
df1 = df.to_dict()
a = df.iloc[0][0]

df_size = len(df)

userList = [[] for _ in range(5)]

'''Find all the ids per user'''
for userId in range(5):
    idList=[]
    for rows in range(df_size):
        if df.iloc[rows][1] == userId+1:
            d = ast.literal_eval(df.iloc[rows][0])
            for i in range(len(d)):
                idList.append(d[i]['id'])
                
    for element in idList:
        userList[userId].append(element)

'''Find number of each id per user'''

user1 = dict(Counter(userList[0]))
print('User1: ')
print(user1)
print('\n')

user2 = dict(Counter(userList[1]))
print('User2: ')
print(user2)
print('\n')

user3 = dict(Counter(userList[2]))
print('User3: ')
print(user3)
print('\n')

user4 = dict(Counter(userList[3]))
print('User4: ')
print(user4)
print('\n')

user5 = dict(Counter(userList[4]))
print('User5: ')
print(user5)
print('\n')