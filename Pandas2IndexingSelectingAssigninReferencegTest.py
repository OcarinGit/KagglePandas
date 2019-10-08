# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:21:06 2019

@author: User
"""

import pandas as pd
import os

#Setup
"""Run the following cell to load your data and some utility functions (including code to check your answers).
import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")
"""
os.chdir("D:\Ocarin\Data Scientist\Python Practices\Kaggle\Pandas Course")
    
reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)
print(reviews.shape)
#Look at an overview of your data by running the following line
print(reviews.head())
print(reviews.tail())
print(reviews.columns)
print("Setup Complete")

pd.set_option("display.max_rows",5)
print(reviews)
pd.set_option("display.max_rows",100)
print(reviews)

"""Exercise No 1 ## 1.

Select the `description` column from `reviews` and assign the result to the variable `desc`.
"""
desc = reviews.description
desc = reviews["description"]
descSeries = reviews.loc[:,"description"]
descDataFrame = reviews.loc[:,["description"]]
print(desc.shape)
print(desc.head())

"""Follow-up question: what type of object is `desc`? If you're not sure, you can check by calling Python's `type` function: `type(desc)`.
"""
print(type(descSeries))
print(type(descDataFrame))  

"""Exercise No 2 
Select the first value from the description column of `reviews`, assigning it to variable `first_description`.
"""
first_description = reviews.description[0]
print("Way 1")
print(first_description)
first_description = reviews["description"][0]
print("Way 2")
print(first_description)
first_description = reviews.loc[0,["description"]]
print("Way 3")
print(first_description)

"""Answer: Correct:

first_description = reviews.description.iloc[0]

Note that while this is the preferred way to obtain the entry in the DataFrame, many other options will return a valid result, such as reviews.description.loc[0], reviews.description[0], and more!
"""

"""Exercise ## 3. 

Select the first row of data (the first record) from `reviews`, assigning it to the variable `first_row`.
"""

first_row = reviews.iloc[0,:]
print(first_row.shape)
print(first_row)
first_row = reviews.loc[0,:]
print(first_row.shape)
print(first_row)

""" Exercise ## 4.

Select the first 10 values from the `description` column in `reviews`, assigning the result to variable `first_descriptions`.

Hint: format your output as a `pandas` `Series`.
"""
print(reviews.columns)

#First, obtain the index of the column description
print("Column number for description column name is:")
print(reviews.columns.get_loc("description"))
column_number = reviews.columns.get_loc("description")
first_description = reviews.iloc[0:9, column_number]
print(first_description)
print(type(first_description))

first_description = reviews.loc[0:9, "description"]
print(first_description)
print(type(first_description))

"""Correct:

first_descriptions = reviews.description.iloc[:10]

Note that many other options will return a valid result, such as desc.head(10) and reviews.loc[:9, "description"].
"""

"""## 5.

Select the records with index labels `1`, `2`, `3`, `5`, and `8`, assigning the result to the variable `sample_reviews`.

In other words, generate the following DataFrame:

![](https://i.imgur.com/sHZvI1O.png)
"""
sample_reviews = reviews.loc[reviews.index.isin([1,2,3,5,8])]
print(sample_reviews.head())

sample_reviews = reviews.loc[(reviews.index==1)|
                             (reviews.index==2)|
                             (reviews.index==3)|
                             (reviews.index==5)|
                             (reviews.index==8)]
print(sample_reviews.head())


""" Exercise ## 6.

Create a variable `df` containing the `country`, `province`, `region_1`, and `region_2` columns of the records with the index labels `0`, `1`, `10`, and `100`. In other words, generate the following `DataFrame`:
"""
df = reviews.loc[reviews.index.isin([0,1,10,100]),["country","province","region_1","region_2"]]
print(df)
df = reviews.loc[(reviews.index==0)| 
                 (reviews.index==1)|
                 (reviews.index==10)|
                 (reviews.index==100),
                 ["country","province","region_1","region_2"]]
print(df)

"""## 7.

Create a variable `df` containing the `country` and `variety` columns of the first 100 records. 

Hint: you may use `loc` or `iloc`. When working on the answer this question and the several of the ones that follow, keep the following "gotcha" described in the [reference](https://www.kaggle.com/residentmario/indexing-selecting-assigning-reference) for this tutorial section:

> `iloc` uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So `0:10` will select entries `0,...,9`. `loc`, meanwhile, indexes inclusively. So `0:10` will select entries `0,...,10`.

> [...]

> ...[consider] when the DataFrame index is a simple numerical list, e.g. `0,...,1000`. In this case `reviews.iloc[0:1000]` will return 1000 entries, while `reviews.loc[0:1000]` return 1001 of them! To get 1000 elements using `iloc`, you will need to go one higher and ask for `reviews.iloc[0:1001]`.
"""

df = reviews.loc[0:99,["country","variety"]]
print(df)

column_numbers_list = []
column_numbers_list.append(reviews.columns.get_loc("country"))
column_numbers_list.append(reviews.columns.get_loc("variety"))
print(reviews.columns)
print(column_numbers_list)
df = reviews.iloc[0:100,column_numbers_list]
print(df)

"""Correct:

cols = ['country', 'variety']
df = reviews.loc[:99, cols]

or

cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]
"""

""" Exercise ## 8.

Create a DataFrame `italian_wines` containing reviews of wines made in `Italy`. Hint: `reviews.country` equals what?
"""
italian_wines = reviews.loc[reviews.country == "Italy"]
print(italian_wines)
print(type(italian_wines))

""" Exercise ## 9.

Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
"""
print(reviews.columns)
top_oceania_wines = reviews.loc[((reviews.country=="Australia")|(reviews.country=="New Zealand")) & (reviews.points>=95)]
print(top_oceania_wines)
print(reviews.loc[(reviews.country=="New Zealand")])
