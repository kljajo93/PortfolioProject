#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:


import csv, sqlite3
conn = sqlite3.connect('socioeconomic.db')
cursor_obj = conn.cursor()
import pandas as pd


# In[4]:


get_ipython().run_line_magic('sql', 'sqlite:///socioeconomic.db')


# In[5]:


df= pd.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql('chicago_socioeconomic_data', conn, if_exists='replace',index=False,method="multi") 


# In[6]:


get_ipython().run_line_magic('sql', 'SELECT * FROM chicago_socioeconomic_data limit 5;')


# In[7]:


get_ipython().run_line_magic('sql', 'select count(*) from chicago_socioeconomic_data;')


# In[10]:


get_ipython().run_line_magic('sql', 'select count(*) from chicago_socioeconomic_data;')


# In[9]:


get_ipython().run_line_magic('sql', 'select * from chicago_socioeconomic_data where hardship_index>50.0;')


# In[11]:


get_ipython().run_line_magic('sql', 'select count(*) from chicago_socioeconomic_data where hardship_index>50.0;')


# In[12]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# In[ ]:




