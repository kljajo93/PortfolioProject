#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# In[45]:


path='Div_Trips1'
df1= pd.read_csv(r'C:\Users\kljaj\Desktop\bicycle\Div_Trips1.csv')
df2=pd.read_csv(r'C:\Users\kljaj\Desktop\bicycle\Divvy_Trips_2019_Q2\Divvy_Trips_2019_Q2.csv')
df3=pd.read_csv(r'C:\Users\kljaj\Desktop\bicycle\Divvy_Trips_2019_Q3\Divvy_Trips_2019_Q3.csv')
df4=pd.read_csv(r'C:\Users\kljaj\Desktop\bicycle\Divvy_Trips_2019_Q4\Divvy_Trips_2019_Q4.csv')


# In[46]:


df1.head()


# In[47]:


df2.rename(columns={'01 - Rental Details Rental ID': 'trip_id','01 - Rental Details Local Start Time':'start_time',
                   '01 - Rental Details Local End Time':'end_time', '01 - Rental Details Bike ID':'bikeid',
                   '01 - Rental Details Duration In Seconds Uncapped':'tripduration',
                   '03 - Rental Start Station ID':'from_station_id', '03 - Rental Start Station Name':'from_station_name',
                   '02 - Rental End Station ID':'to_station_id', '02 - Rental End Station Name':'to_station_name',
                   'User Type':'usertype', 'Member Gender':'gender','05 - Member Details Member Birthday Year':'birthyear'},inplace=True)


# In[48]:


df2.head()


# In[49]:


df3.head()


# In[50]:


df4.head()


# In[51]:


df=pd.concat([df1,df2,df3,df4])


# In[52]:


df.reset_index(inplace=True)


# In[53]:


df.info()


# In[54]:


df.drop(columns=['index'],inplace=True)


# In[55]:


df.head()


# In[56]:


df['start_time']=pd.to_datetime(df['start_time'])


# In[57]:


df['end_time']=pd.to_datetime(df['end_time'])


# In[58]:


df['birthyear'].isnull().value_counts()


# In[59]:


df.isnull().sum()


# In[60]:


df.dropna(inplace=True)
df.reset_index(inplace=True)


# In[61]:


df['birthyear']=df['birthyear'].astype('int')


# Users born before 1945 

# In[62]:


df.info()


# In[63]:


df=df[df['birthyear']>1945].reset_index()


# In[64]:


df['to_station_name'].value_counts()


# In[65]:


df[df['tripduration'].str.isnumeric()==False]


# In[66]:


df['tripduration']=df['tripduration'].str.replace('.0','').str.replace(',','').astype('int64')


# In[67]:


df.drop(columns=['level_0','index'],inplace=True)


# In[68]:


df.groupby('usertype')['tripduration'].sum()/df['usertype'].value_counts()


# In[69]:


df['usertype'].value_counts()


# In[70]:


df.corr(numeric_only=True)


# In[71]:


df['ride_length']=df['end_time']-df['start_time']


# In[72]:


df.sort_values(by='ride_length',ascending=False)


# In[73]:


df.info()


# In[74]:


df[df['start_time']>df['end_time']]


# In[75]:


df.loc[df.index[2959074],'end_time']=('2019-11-03 02:09:56')
df.loc[df.index[2959079],'end_time']=('2019-11-03 02:02:40')
df.loc[df.index[2959080],'end_time']=('2019-11-03 02:16:48')
df.loc[df.index[2959081],'end_time']=('2019-11-03 02:04:25')
df.loc[df.index[2959083],'end_time']=('2019-11-03 02:03:02')
df.loc[df.index[2959085],'end_time']=('2019-11-03 02:01:52')
df.loc[df.index[2959085],'end_time']=('2019-11-03 02:01:52')
df.loc[df.index[2959086],'end_time']=('2019-11-03 02:01:26')
df.loc[df.index[2959087],'end_time']=('2019-11-03 02:08:27')




# In[76]:


df[df['start_time']>df['end_time']]


# In[99]:


df['week_day']=df['start_time'].dt.weekday
df.head()


# In[100]:


df['weekend']=df['week_day'].apply(lambda x: x==5|x==6)


# In[123]:


df['day_name']=df['start_time'].dt.day_name()


# In[126]:


byday=df['day_name'].value_counts()


# In[131]:


byday=byday.reset_index()


# In[245]:


df.groupby('usertype')['tripduration'].sum()/df.shape[0]


# In[136]:


df.plot(kind='bar',x='day_name' y=)


# In[135]:


df.groupby(['usertype','day_name']).count()


# In[247]:


df['usertype'].value_counts()


# In[248]:


df.shape[0]


# In[249]:


df.groupby('usertype')['tripduration'].sum()


# In[253]:


df.groupby('usertype')['tripduration'].mean().plot()


# In[255]:


ax=sns.barplot(x='usertype',y='tripduration',data=df, estimator='mean',errorbar=None)
ax.set_xlabel('User Type')
ax.set_ylabel('Average Trip Duration')


# In[256]:


ax=sns.barplot(x='usertype',y='tripduration',data=df,hue='gender', estimator='mean',errorbar=None)
ax.set_xlabel('User Type')
ax.set_ylabel('Average Trip Duration')


# In[ ]:


sns.

