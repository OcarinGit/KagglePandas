# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:11:49 2019

@author: El Macho
"""

import pandas as pd

reviews = pd.read_csv("datasets/winemag-data-130k-v2.csv", index_col=0)
print(reviews)
pd.set_option("display.max_rows",5)
print(reviews)

"""Selecting specific values of a pandas DataFrame or Series to work on is an implicit step in almost any data operation you'll run. Hence a solid understanding of how to slice and dice a dataset is vital.
"""

#Naive accessors
#Native Python objects provide many good ways of indexing data. pandas carries all of these over, which helps make it easy to start with.
print(reviews.shape)


"""

In Python we can access the property of an object by accessing it as an attribute. A book object, for example, might have a title property, which we can access by calling book.title. Columns in a pandas DataFrame work in much the same way.

Hence to access the country property of our reviews we can use:
"""
print(reviews.country)

"""

If we have a dict object in Python, we can access its values using the indexing ([]) operator. Again, we can do the same with pandas DataFrame columns. It "just works":
"""
print(reviews["country"])

"""

These are the two ways of selecting a specific columnar Series out of a pandas DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

Doesn't a pandas Series look kind of like a fancy dict? It pretty much is, so it's no surprise that, to drill down to a single specific value, we need only use the indexing operator [] once more:
"""
print("Element 0 of the country attribute of object reviews:"
      +reviews["country"][0])

"""
Index-based selection

The indexing operator and attribute selection are nice because they work just like they do in the rest of the Python ecosystem. As a novice, this makes them easy to pick up and use. However, pandas has its own accessor operators, loc and iloc. For more advanced operations, these are the ones you're supposed to be using.

pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.

To select the first row of data in this DataFrame, we may use the following:
"""
print("--------------- Content of the first row of object reviews ------------------")
print(reviews.iloc[0])

""" 

Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.

This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. To get a column with iloc, we can do the following:
"""
print("---------- Content of the first row of object reviews, first column ------------------")
print(reviews.iloc[:,0])