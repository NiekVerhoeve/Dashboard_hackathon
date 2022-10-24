#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import os 
import streamlit as st
import seaborn as sns
import matplotlib as plt
import requests
import plotly.graph_objects as go
import plotly.express as px


# In[4]:


df = pd.read_csv('/Users/luukvlug/Desktop/School/Data Science Minor/HairEyeColor.csv')


# In[5]:


df.head(10)


# In[18]:


fig2 = px.bar(df,x='Sex',y='Hair')
fig2.show()


# In[9]:


st.header('Hoi')


# In[19]:


st.plotly_chart(fig2)


# In[ ]:




