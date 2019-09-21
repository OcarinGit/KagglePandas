# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:41:54 2019

@author: User
"""

import pandas as pd

#(https://i.imgur.com/Ax3pp2A.png)
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({"Apples":[30],"Bananas":[21]})
print(fruits)

# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({"Apples":[35,41],"Bananas":[21,34]}, index=["2017 Sales","2018 Sales"])


ingredients = pd.Series(["4 cups","1 cup","2 large", "1 can"], index=["Flour","Milk","Eggs","Spam"], name="Dinner")

reviews = pd.read_csv("datasets/winemag-data_first150k.csv", index_col=0)
print(reviews.head())

#Import a sqlite db
import sqlite3

with sqlite3.connect("datasets/database.sqlite") as con:
    sql = "SELECT * FROM artists"
    df = pd.read_sql(sql, con)
    print(df.shape)
