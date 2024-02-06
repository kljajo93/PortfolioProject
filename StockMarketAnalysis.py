#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


sns.set_style('whitegrid')


# In[8]:


get_ipython().run_line_magic('pip', 'install yfinance')


# In[11]:


import yfinance as yf


# In[12]:


get_ipython().system('pip3 install pandas_datareader')


# In[5]:


import pandas_datareader.data as web


# In[6]:


from datetime import datetime


# In[7]:


from __future__ import division


# In[8]:


tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']


# In[9]:


end = datetime.now()
start = datetime(end.year-1,end.month,end.day)


# In[36]:


for stock in tech_list:
    globals()[stock]= yf.download(stock,start,end)


# In[37]:


AAPL


# In[22]:


another = yf.Ticker('AMZN')


# In[19]:


another.history(period='1y')


# In[43]:


AAPL.info()


# In[38]:


AAPL


# In[44]:


AAPL['Adj Close'].plot(legend=True,figsize=(10,4))


# In[45]:


AAPL['Volume'].plot(legend=True, figsize=(10,4))


# In[49]:


ma_day=[10,20,50]

for ma in ma_day:
    column_name ="MA for %s days" %(str(ma))
    AAPL[column_name]= pd.DataFrame.rolling(AAPL['Adj Close'],ma).mean()


# In[51]:


AAPL.head(30)


# In[55]:


AAPL[['Adj Close','MA for 10 days', 'MA for 20 days','MA for 50 days']].plot(subplots=False, figsize=(10,4))


# In[56]:


AAPL['Daily Return']= AAPL['Adj Close'].pct_change()


# In[57]:


AAPL.head(30)


# In[60]:


AAPL['Daily Return'].plot(figsize=(10,4), legend=True, marker='o')


# In[66]:


sns.histplot(AAPL['Daily Return'].dropna(), bins=100, kde=True)


# In[67]:


closing_df= yf.download(tech_list,start,end)['Adj Close']


# In[68]:


closing_df.head()


# In[69]:


tech_returns= closing_df.pct_change()


# In[70]:


tech_returns.head()


# In[75]:


sns.jointplot(x='AMZN', y='MSFT',data= tech_returns, kind='scatter')


# In[76]:


sns.pairplot(tech_returns.dropna())


# In[77]:


ret_fig=sns.PairGrid(tech_returns.dropna())
ret_fig.map_upper(plt.scatter,color='purple')
ret_fig.map_lower(sns.kdeplot, cmap='cool_d')
ret_fig.map_diag(plt.hist,bins=30)


# In[79]:


tech_rets_corr= tech_returns.dropna().corr()
sns.heatmap(tech_rets_corr, annot=True, fmt='.2f')
plt.show()


# In[80]:


rets= tech_returns.dropna()


# In[87]:


area= np.pi
plt.scatter(rets.mean(),rets.std(), s=area)
plt.xlabel('Expected Returns')
plt.ylabel('Risk')
for label,x,y in zip(rets.columns,rets.mean(),rets.std()):
    plt.annotate(
    label,
    xy=(x,y),xytext=(50,50),
    textcoords='offset points', ha='right', va='bottom',
    arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=-0.3'))
    
    


# In[89]:


sns.histplot(AAPL['Daily Return'].dropna(),kde=True, bins=100)


# In[90]:


rets['AAPL'].quantile(0.05)


# In[91]:


days =365
dt =1/days
mu=rets.mean()['GOOG']
sigma=rets.std()['GOOG']


# In[92]:


def monte_carlo(start_price,days,mu,sigma):
    price=np.zeros(days)
    price[0]=start_price
    drift=np.zeros(days)
    shock=np.zeros(days)
    
    for x in range(1,days):
      shock[x]=np.random.normal(loc=mu*dt, scale=sigma * np.sqrt(dt))
      drift[x]=mu*dt
      price[x]=price[x-1] + (price[x-1] * (drift[x]+shock[x]))
    return price


# In[94]:


GOOG.head()
start_price=97.86


# In[95]:


for run in range(100):
    plt.plot(monte_carlo(start_price,days,mu,sigma))
plt.xlabel('Days')
plt.ylabel('Price')


# In[ ]:




