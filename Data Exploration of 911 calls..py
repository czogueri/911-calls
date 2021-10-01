#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('Desktop/911.csv')


# In[4]:


df.info()


# In[5]:


df.head()


# In[16]:


#top 5 zipcodes 
df['zip'].value_counts().head()


# In[19]:


#top 5 townships
df['twp'].value_counts().head()


# In[22]:


#unique titles
df['title'].nunique()


# In[27]:


x = df['title'].iloc[0]


# In[29]:


x.split(':')[0]


# In[31]:


df['Reason']= df['title'].apply(lambda title: title.split(':')[0])


# In[32]:


df['Reason']


# In[33]:


df.describe()


# In[35]:


df['Reason'].value_counts()


# In[38]:


sns.countplot(x= 'Reason', data = df)


# In[41]:


df.info()


# In[42]:


#converting datetime from strings to datetime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[43]:


df['timeStamp']


# In[49]:


time = df['timeStamp'].iloc[0]
time.hour


# In[51]:


#creating new columns for hour, month, day of the week.
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['month'] = df['timeStamp'].apply(lambda time: time.month)
df['day of the week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[55]:


df.head()


# In[56]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[57]:


df['day of the week'] = df['day of the week'].map(dmap)


# In[58]:


df.head()


# In[61]:


sns.countplot(x = 'day of the week', data = df, hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[62]:


sns.countplot(x = 'month', data = df, hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[66]:


bymonth = df.groupby('month').count()
bymonth.head()


# In[72]:


bymonth['twp'].plot()


# In[75]:


#use seaborn's lmplot() to create a linear fit on the number of calls per month
sns.lmplot(x = 'month', y ='twp', data = bymonth.reset_index())


# In[79]:


#Create a new column called 'Date' that contains the date from the timeStamp column.
df['Date']= df['timeStamp'].apply(lambda t: t.date())


# In[80]:


df.head()


# In[83]:


#groupby this Date column with the count() aggregate and create a plot of counts of 911 calls
df.groupby('Date').count().head()


# In[88]:


df.groupby('Date').count()['twp'].plot()
plt.tight_layout()


# In[90]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[91]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# In[92]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()


# In[95]:


dayHour = df.groupby(by=['day of the week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[98]:


plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')


# In[99]:


#creating clustermap with df
sns.clustermap(dayHour,cmap='viridis')


# In[103]:


dayMonth = df.groupby(by=['day of the week','month']).count()['Reason'].unstack()
dayMonth.head()


# In[104]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')


# In[105]:


sns.clustermap(dayMonth,cmap='viridis')


# In[ ]:




