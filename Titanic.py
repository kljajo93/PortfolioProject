#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


dataset= np.random.randn(15)


# In[6]:


dataset


# In[12]:


plt.hist(dataset, alpha =0.5)


# In[14]:


titanic_df= pd.read_csv(r'C:\Users\kljaj\Downloads\train.csv')


# In[16]:


titanic_df.head()


# In[17]:


titanic_df.info()


# In[22]:


sns.countplot(x='Sex', data=titanic_df)


# In[23]:


sns.countplot(x='Sex', data=titanic_df, hue='Pclass')


# In[24]:


sns.countplot(x='Pclass', data=titanic_df, hue='Sex')


# In[25]:


def male_female_child(passenger):
    age,sex = passenger
    if age < 16:
       return 'child'
   
    else:
        return sex


# In[26]:


titanic_df['Person']=titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)


# In[31]:


titanic_df.head(10)


# In[32]:


titanic_df['Age'].hist(bins=70)


# In[33]:


titanic_df['Age'].mean()


# In[34]:


titanic_df['Person'].value_counts()


# In[38]:


fig = sns.FacetGrid(titanic_df, hue='Sex',aspect=4)
fig.map(sns.kdeplot, 'Age', fill=True)

oldest= titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[40]:


deck = titanic_df['Cabin'].dropna()


# In[46]:


levels = []

for level in deck:
    levels.append(level[0])
    
cabin_df = pd.DataFrame(levels)
cabin_df.columns = ['Cabin']
#cabin_df = cabin_df[cabin_df.Cabin !='T']
sns.countplot(x='Cabin', data=cabin_df, palette='summer')


# In[51]:


sns.countplot(x='Embarked', data=titanic_df, hue='Pclass', order=['C','Q','S'])


# In[52]:


titanic_df.head()


# In[53]:


titanic_df['Alone']=titanic_df.SibSp + titanic_df.Parch


# In[54]:


titanic_df['Alone']


# In[55]:


titanic_df['Alone'].loc[titanic_df['Alone'] >0]='With Family'
titanic_df['Alone'].loc[titanic_df['Alone']==0]='Alone'


# In[56]:


titanic_df.head()


# In[57]:


sns.countplot(x='Alone', data=titanic_df, palette='Blues')


# In[60]:


titanic_df['Survivor'] = titanic_df.Survived.map({0:'no', 1:'yes'})


# In[63]:


sns.countplot(x='Survivor', data=titanic_df,hue='Pclass', palette='Set1')


# In[95]:


survivor_class= titanic_df[[('Survived'), 'Pclass']].groupby('Pclass')


# In[97]:


survivor_class.sum('Survived')


# In[93]:


titanic_df.head()


# In[ ]:




