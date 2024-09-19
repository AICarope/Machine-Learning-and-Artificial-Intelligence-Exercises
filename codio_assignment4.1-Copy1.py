#!/usr/bin/env python
# coding: utf-8

# ### Required Codio Assignment 4.1: Complex Joins on Datasets
# 
# **Expected Time: 60 Minutes**
# 
# **Total Points: 10**
# 
# ![](images/kiva.png)
# 
# This assignment focuses on using pandas `merge` to answer questions using multiple data sources.  Here, you will combine data and use many of the earlier `pandas` methods together with the `merge` function to extract insights from our data source.  The data comes from the Kiva loan provider organization and was part of a Kaggle Data Science for Good contest [here](https://www.kaggle.com/kiva/data-science-for-good-kiva-crowdfunding).
# 
# #### Index:
# 
# - [Problem 1](#Problem-1)
# - [Problem 2](#Problem-2)
# - [Problem 3](#Problem-3)
# - [Problem 4](#Problem-4)
# - [Problem 5](#Problem-5)

# ### The Data
# 
# Kiva allows users to fund loans to small organizations around the world.  The four datasets contain a subset of the data provided on Kaggle and describe information on the individual loan when it was given, where the borrowers were located, and what the loans were being used for.  Below, the data is loaded into four DataFrames, and the first two rows of each displayed.  Note the shared `id` column across all four datasets.

# In[1]:


import pandas as pd


# In[2]:


crowdsource = pd.read_csv('data/kiva/crowdsource.csv')
crowdsource.head(2)


# In[3]:


demographics = pd.read_csv('data/kiva/demographics.csv')
demographics.head(2)


# In[4]:


financials = pd.read_csv('data/kiva/financials.csv')
financials.head(2)


# In[5]:


use = pd.read_csv('data/kiva/use.csv')
use.head(2)


# [Back to top](#Index:) 
# 
# ### Problem 1
# 
# #### Kenyan Loan Amounts
# 
# **5 Points**
# 
# 
# Use the `demographics` and `financials` data to determine the average loan amount for the country `Kenya`.  
# 
# Note that the average loan amount in each country can be calculated by computing the mean of the `funded_amount` column.
# 
# 
# Save your response as a float to `ans1` below.

# In[6]:


### GRADED

ans1 = None

# YOUR CODE HERE
ans1 = pd.merge(demographics.loc[demographics['country'] == 'Kenya'], financials, on = 'id')[['funded_amount']].mean().values[0]
type(ans1)

# Answer check
print(ans1)
print(type(ans1))


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 2
# 
# ### El Salvador Top Sector
# 
# **5 Points**
# 
# Use the `demographics` and `use` datasets to determine the sector of work that received the most loans in `El Salvador`.  
# 
# Note that the  the sector of work in each country can be calculated by using `value_counts()` on the `sector` column.
# 
# 
# Assign your result as a string to `ans2` below.

# In[7]:


### GRADED

ans2 = None

# YOUR CODE HERE
ans2 = pd.merge(demographics.loc[demographics['country'] == 'El Salvador'], use, on = 'id')['sector'].value_counts().index[0]
type(ans2)

# Answer check
print(ans2)
print(type(ans2))


# In[ ]:





# ### Problem 3
# 
# #### Pakistan Loans in Agriculture
# 
# **5 Points**
# 
# 
# Merge the DataFrames `use` and `demographics` on `id`. Assign your result to `p1`.
# 
# Merge the DataFrames `p1` and `financials` on `id`. Assign your result to `a`.
# 
# Use `loc` on the `a` DataFrame to select the rows in which `country` is equal to `Pakistan`. Assogn your result to `b`.
# 
# 
# Determine the total amount of loans (`funded_amount`) for `Agriculture` in Pakistan.  Assign your results as a float to `ans3` below.

# In[8]:


### GRADED

ans3 = None

# YOUR CODE HERE
p1 = pd.merge(use, demographics, on = 'id')
a = pd.merge(p1, financials, on = 'id')
b = a.loc[a['country'] == 'Pakistan']
ans3 = b.loc[b['sector'] == 'Agriculture'][['funded_amount']].sum().values[0]

# Answer check
print(ans3)
print(type(ans3))


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 4
# 
# #### Top Total Loan Sector
# 
# **5 Points**
# 
# Merge the `financials` and `use` DataFrames on `id`. To this, chain a `groupby()` operation on `sector` and use a double square bracket notation to select the column `funded_amount`.
# 
# 
# 
# What sector received the most total dollars in funding?  Assign your response as a string to `ans4` below.

# In[9]:


### GRADED

ans4 = None

# YOUR CODE HERE
ans4 = pd.merge(financials, use, on = 'id').groupby('sector')[['funded_amount']].sum().sort_values(by = 'funded_amount', ascending = False).index[0]

# Answer check
print(ans4)
print(type(ans4))


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 5
# 
# #### Top Loan by Lender Amount
# 
# **5 Points**
# 
# Merge the DataFrames `financials` and `use` on `id`. Assign your result to `a`.
# 
# Merge the DataFrames `a` and `crowdsource` on `id`. Assign your result to `b`.
# 
# In the `b` DataFrame, create a new column `ratio`. To this column assign the ratio of the columns `funded_amount` and `lender_count` of the `b` DataFrame.
# 
# 
# Determine which loan sector has the highest ratio of currency to lender amount. Assign the sector with the highest ratio as a string to `ans5` below. 

# In[10]:


### GRADED

ans5 = None

# YOUR CODE HERE
a = pd.merge(financials, use, on = 'id')
b = pd.merge(a, crowdsource, on = 'id')
b['ratio'] = b['funded_amount']/b['lender_count']
ans5 = b.groupby('sector')['ratio'].max().idxmax()

# Answer check
print(ans5)
print(type(ans5))


# In[ ]:





# In[ ]:





# In[ ]:




