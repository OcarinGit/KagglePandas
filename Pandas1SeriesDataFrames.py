# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:56:10 2019

@author: El Macho
"""


"""here are two core objects in pandas: the DataFrame and the Series.

A DataFrame is a table. It contains an array of individual entries, each of 
which has a certain value. Each entry corresponds with a row (or record) and a column.
"""


import pandas as pd

#For example, consider the following simple DataFrame:"""
#Curly brackets are used in Python for creating Dictionaries (HashMaps, key,value pairs)
miTable = pd.DataFrame({'Yes':[50,21], 'No':[131,2]})
print(miTable)
#print("Content of miTable Pandas Object:"+str(miTable))

#Data frame of strings
print(pd.DataFrame({'Bob':['I liked it', 'It was awful'], 'Sue':['Pretty Good.','Bland']}))

#Assigning indexes to the rows
print(pd.DataFrame({'Bob':['I liked it', 'It was awful'], 'Sue':['Pretty Good.','Bland']},index=['Product A','Product B']))
print(type(pd.DataFrame({'Bob':['I liked it', 'It was awful'], 'Sue':['Pretty Good.','Bland']},index=['Product A','Product B'])))

#A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:
miSeries = pd.Series([1,2,3,4,5,6,7,8])
print(miSeries)

#Adding indexes and overall name to the series
miSeries = pd.Series([60,70,80], index=["Sales 2016","Sales 2017","Sales 2016"], name="Overall name of the Series")
print(miSeries)

#Reading common file formats
wine_reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv")

#See how big is our dataset
print(wine_reviews.shape)

#See the first five lines
print(wine_reviews.head())

#Read and excel file
wic = pd.read_excel("datasets/WICAgencies2013ytd.xls", sheetn_name="Total Women")
print(wic.shape)
print(wic.head())

#Import from mysql database
from sqlalchemy import create_engine
#import MySQLdb
import pymysql

db_connection_string='mysql+pymysql://root:root@localhost:3306/abarrotes'
sql_engine = create_engine(db_connection_string)
df = pd.read_sql("SELECT * FROM empleados", sql_engine)
print(df)

"""

Writing common file formats

Writing data to a file is usually easier than reading it out of one, because pandas handles the nuisance of conversions for you.

We'll start with CSV files again. The opposite of read_csv, which reads our data, is to_csv, which writes it. With CSV files it's dead simple:
"""
wine_reviews.to_csv("datasets/prueba.csv")
wic.to_excel("datasets/pruebaExcel.xls", sheet_name="PRUEBA WOMEN")
df.to_sql("empleados2", sql_engine)

