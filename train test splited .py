#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


csv_location = "C:/Users/Mit/Downloads/mtechstudentdata (1).xlsx" 
csv_location


# In[18]:


data = pd.read_excel(csv_location)


# In[19]:


data.head()
data.dropna(inplace=True)


# In[20]:


data.columns


# In[21]:


y = data['bmi']
#features = ['height(meter)', 'weight']
X = data[['height(meter)', 'weight']]
#X= X.dropna(axis=0)


# In[32]:


from sklearn.model_selection import train_test_split


# In[43]:


train_X , val_X , train_y , val_y = train_test_split(X, y , random_state = 0)


# In[ ]:






# In[49]:


from sklearn.tree import DecisionTreeRegressor


# In[50]:


model = DecisionTreeRegressor(random_state=1)


# In[51]:


model.fit(train_X,train_y)


# In[55]:


model.predict(val_X)


# In[56]:


predicted_value = model.predict (val_X)


# In[57]:


from sklearn.metrics import mean_absolute_error


# In[59]:


mean_absolute_error(predicted_value,val_y)


# In[ ]:


#this model has MEA of 4.11 model is not good enough 


# In[ ]:




