#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[46]:


csv_location = "/mtechstudentdata (1).xlsx"
csv_location


# In[3]:


data = pd.read_excel(csv_location)


# In[23]:


data.head()
data.dropna(inplace=True)


# In[24]:


data.columns


# In[35]:


y = data['bmi']
#features = ['height(meter)', 'weight']
X = data[['height(meter)', 'weight']]
#X= X.dropna(axis=0)


# In[38]:


#print (X)
X


# In[27]:


from sklearn.tree import DecisionTreeRegressor


# In[28]:


model = DecisionTreeRegressor(random_state=1)


# In[29]:


model.fit(X,y)


# In[36]:


model.predict(X.head())


# In[44]:


model.predict ([1,53])


# In[ ]:




