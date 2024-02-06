#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv,sqlite3
conn=sqlite3.connect('FinalDB.db')


# In[10]:


cursor=conn.cursor()


# In[13]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///FinalDB.db')


# In[16]:


import pandas
df = pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CENSUS_DATA",conn, if_exists ='replace', index = False, method='multi')
df=pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CHICAGO_PUBLIC_SCHOOLS", conn, if_exists='replace', index = False, method = 'multi')
df= pandas.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01")
df.to_sql("CHICAGO_CRIME_DATA",conn, if_exists='replace', index=False, method='multi')


# In[18]:


get_ipython().run_line_magic('sql', 'select count(*) from CHICAGO_CRIME_DATA')


# In[21]:


get_ipython().run_line_magic('sql', "select name from PRAGMA_TABLE_INFO('CENSUS_DATA');")


# In[24]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME,PER_CAPITA_INCOME  from CENSUS_DATA where PER_CAPITA_INCOME<11000  order by PER_CAPITA_INCOME ;')


# In[29]:


get_ipython().run_line_magic('sql', "select * from CHICAGO_CRIME_DATA where DESCRIPTION like '%minor%';")


# In[70]:


get_ipython().run_line_magic('sql', "select * from CHICAGO_CRIME_DATA where PRIMARY_TYPE like '%kidnapping%' and DESCRIPTION LIKE '%child%';")


# In[34]:


get_ipython().run_line_magic('sql', "select distinct PRIMARY_TYPE from CHICAGO_CRIME_DATA where LOCATION_DESCRIPTION like '%school%'")


# In[41]:


get_ipython().run_line_magic('sql', "alter table CHICAGO_PUBLIC_SCHOOLS  rename column 'Elementary, Middle, or High School' to school_type")


# In[44]:


get_ipython().run_line_magic('sql', 'select school_type, avg(SAFETY_SCORE)  from CHICAGO_PUBLIC_SCHOOLS  group by school_type')


# In[47]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME, PERCENT_HOUSEHOLDS_BELOW_POVERTY  from CENSUS_DATA  order by PERCENT_HOUSEHOLDS_BELOW_POVERTY desc limit 5')


# In[45]:


get_ipython().run_line_magic('sql', 'select *  from CENSUS_DATA  limit 5')


# In[72]:


get_ipython().run_line_magic('sql', 'select count(*), COMMUNITY_AREA_NUMBER   from CHICAGO_CRIME_DATA  group by COMMUNITY_AREA_NUMBER  order by count(*) desc')


# In[53]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA where HARDSHIP_INDEX =(select max(HARDSHIP_INDEX) from CENSUS_DATA)')


# In[60]:


get_ipython().run_line_magic('sql', "select * from CHICAGO_CRIME_DATA where  DESCRIPTION LIKE '%child%';")


# In[63]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA where COMMUNITY_AREA_NUMBER =25.0')


# In[ ]:




