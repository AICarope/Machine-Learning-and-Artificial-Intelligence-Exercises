#!/usr/bin/env python
# coding: utf-8

# ### Required Codio Assignmen 4.2: String Operations
# 
# 
# **Expected Time: 60 Minutes**
# 
# **Total Points: 20**
# 
# 
# For this activity, you will focus on using string methods on the `pandas` series.  Following the examples from video 4.8, a Wikipedia page on the states of the Russian Federation will be the dataset.  Below is a map of the boundaries for the states. 
# 
# #### Index:
# 
# - [Problem 1](#Problem-1)
# - [Problem 2](#Problem-2)
# - [Problem 3](#Problem-3)
# - [Problem 4](#Problem-4)
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Map_of_federal_subjects_of_Russia_%282014%29.svg/1380px-Map_of_federal_subjects_of_Russia_%282014%29.svg.png)

# ### Getting the Data
# 
# Below, we access the data directly using the url and the `read_html` method from `pandas`. This method reads any table from a web URL as a list of data frames. The data we are interested in is located in the fifth table on the page, so we index the list of data below.

# In[1]:


import pandas as pd


# In[2]:


russian_states = pd.read_csv('data/russian_states.csv', index_col = 0)


# In[3]:


russian_states.head()


# [Back to top](#Index:) 
# 
# ### Problem 1
# 
# #### Using the `contains` method
# 
# **5 Points**
# 
# Use the string method `contains` to subset the data based on entries in the `Economic region` column containing `Siberian`.  Assign your response as a DataFrame to `ans1` below.

# In[4]:


### GRADED

ans1 = None

# YOUR CODE HERE
ans1 = russian_states.loc[russian_states['Economic region'].str.contains("Siberian")]
type(ans1)

# Answer check
print(ans1.shape)
ans1.head()


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 2
# 
# #### Using the `startswith` method
# 
# **5 Points**
# 
# Subset the data based on entries in the `Economic region` column that starts with `North`.  Assign your answer as a DataFrame to `ans2` below.

# In[6]:


### GRADED

ans2 = None

# YOUR CODE HERE
ans2 = russian_states.loc[russian_states['Economic region'].str.startswith('North')]
type(ans2)

# Answer check
print(ans2.shape)
ans2.head()


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 3: Using the `upper` method
# 
# **5 Points**
# 
# Use the `upper` method to create a series where the entries in the `Federal district` column all uppercased.  Assign your response as a Series to `ans3` below.

# In[7]:


### GRADED

ans3 = None

# YOUR CODE HERE
ans3 = russian_states['Federal district'].str.upper()
type(ans3)

# Answer check
print(type(ans3))
ans3.head()


# In[ ]:





# [Back to top](#Index:) 
# 
# ### Problem 4
# 
# #### Examining the Population
# 
# **5 Points**
#  
# 
# Much like the example in the videos, the `Population[17]` column contains problematic characters that need to be replaced before the column can be converted to a float datatype.  Replace the `\[22\]`, `\[23\]`, and `,` values with empty strings. Finally, convert the `Population[17]` column to `float` datatypes.  
# 
# Assign your response as a series to `ans4` below.  

# In[8]:


### GRADED

ans4 = None

# YOUR CODE HERE
ans4 = russian_states['Population[17]'].str.replace("\[22\]", " ").str.replace("\[23\]", " ").str.replace(',', '').astype('float')
type(ans4)

# Answer check
print(type(ans4))
ans4.head()


# In[ ]:





# In[ ]:





# In[ ]:




