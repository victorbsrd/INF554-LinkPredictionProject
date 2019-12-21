#!/usr/bin/env python
# coding: utf-8

# # Data Exploration
# *by Aubry d'Andoque on 12/21/19*
# 
# ## Getting Ready

# ### Importing Librairies

# In[4]:


import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt


# ### Importing Data
# Data file must be in './data/'

# In[3]:


with open('./data/training.txt', 'r') as f :
    testing_set = [] 
    for line in f:
        line = line.split()
        testing_set.append(line)

dataset = pd.DataFrame(testing_set, columns=["Node1","Node2","Edge"])
dataset = dataset.astype(np.int)


# ## Node File Analysis

# In[4]:


dataset.head()


# In[5]:


dataset.describe()


# ### Adjacency Matrix

# In[6]:


ind_max_node = int(max(dataset['Node1']))
adjacency_matrix = np.zeros(shape = (ind_max_node,ind_max_node))
for index, row in dataset.iterrows():
    adjacency_matrix[row['Node1']-1,row['Node2']-1] = row['Edge']


# In[ ]:


print(adjacency_matrix)


# In[15]:


adj_matrix = dataset.pivot('Node1', 'Node2','Edge')


# In[3]:


adj_matrix.head()

