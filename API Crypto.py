#!/usr/bin/env python
# coding: utf-8

# In[72]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e8268e9f-eaef-4e69-9a95-35e1d0cb0d86',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
#NOTE:
# I had to go in and put "jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"
# Into the Anaconda Prompt to change this to allow to pull dat


# In[38]:


type(data)


# In[73]:


import pandas as pd
pd.set_option('display.max_columns', None)


# In[74]:


df = pd.json_normalize(data['data'])
df['timestamp']=pd.to_datetime('now')
df


# In[44]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'e8268e9f-eaef-4e69-9a95-35e1d0cb0d86',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    df = pd.json_normalize(data['data'])
    df['timestamp']=pd.to_datetime('now')
    #df=pd.concat([df,df2])
    
    if not os.path.isfile(r'C:\Users\kljaj\Desktop\DataAnalysis\excel\API.csv'):
        df.to_csv(r'C:\Users\kljaj\Desktop\DataAnalysis\excel\API.csv', header='column_names')
    else:
        df.to_csv(r'C:\Users\kljaj\Desktop\DataAnalysis\excel\API.csv', mode='a', header=False)
        
    #Then to read in the file: df = pd.read_csv(r'C:\Users\alexf\OneDrive\Documents\Python Scripts\API.csv')

    #NOTE:
    # I had to go in and put "jupyter notebook --NotebookApp.iopub_data_rate_limit=1e10"
    # Into the Anaconda Prompt to change this to allow to pull data


# In[45]:


import os 
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep(60) #sleep for 1 minute
exit()


# In[47]:


df3=pd.read_csv(r'C:\Users\kljaj\Desktop\DataAnalysis\excel\API.csv')


# In[49]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)
df3


# In[53]:


df2 =df.groupby('name', sort = False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()


# In[54]:


df3= df2.stack()
df3


# In[56]:


df4= df3.to_frame(name='values')
df4.count()


# In[62]:


index= pd.Index(range(90))
df5=df4.reset_index()
df5


# In[63]:


df5= df5.rename(columns={'level_1':'percent_change'})


# In[69]:


df5['percent_change'] = df5['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df5


# In[70]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='percent_change',y='values',hue='name', kind='point', data=df5)


# In[75]:


df10 = df[['name','quote.USD.price','timestamp']]
df10 = df10.query("name == 'Bitcoin'")
df10
sns.set_theme(style="darkgrid")

sns.lineplot(x='timestamp', y='quote.USD.price', data = df10)


# In[76]:


df10


# In[ ]:




