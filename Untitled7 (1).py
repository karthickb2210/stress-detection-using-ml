#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv('B:\KARTHICK\stress.csv')
df.head()


# In[6]:


df.describe()


# In[8]:


df.isnull()


# In[9]:


df.isnull().sum()

