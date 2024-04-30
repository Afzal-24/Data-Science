#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[3]:


np.ones(10)


# In[4]:


np.ones(10)*5


# In[6]:


np.arange(10,51)


# In[7]:


np.arange(10,51,2)


# In[15]:


a=np.arange(0,9)

a.reshape(3,3)


# In[16]:


np.eye(3)


# In[19]:


np.random.rand(1)


# In[20]:


np.random.rand(25)


# In[22]:


np.linspace(0.01,1,100).reshape(10,10)


# In[27]:


ar=np.arange(1,101)
ar.reshape(10,10)/100


# 

# In[28]:


ar = np.arange(0.01,1.01,.01)
ar.reshape(10,10)


# In[32]:


ar = np.arange(1,26).reshape(5,5)
ar


# In[33]:


ar[2,2]
ar[3,4]


# In[34]:


ar[2,2:5]


# In[35]:


ar[2:5,2]


# In[36]:


ar[2:5,2:5]


# In[37]:


ar[2:,2:]


# In[38]:


ar[0:3,0:3]


# In[39]:


ar[:3,:3]


# In[40]:


ar[1:4,1:4]


# In[41]:


ar[2:,1:]


# In[43]:


ar[:3,1]


# In[47]:


ar[4:]


# In[46]:


ar[3]


# In[48]:


ar[3:]


# In[49]:


np.sum(ar)


# In[50]:


np.std(ar)


# In[53]:


np.sum(ar,axis=1)


# In[54]:


ar = np.arange(0,12).reshape(3,2,2)
ar


# In[55]:


ar = np.arange(0,12)
ar


# In[61]:


ar = np.arange(1,26).reshape(5,5)
ar


# In[62]:


ar.dtype


# In[63]:


ar.shape


# In[65]:


type(ar)


# In[67]:


ar = np.zeros(12)
ar


# In[73]:


ar = np.ones(4).reshape(2,2)
ar


# In[77]:


ar = np.zeros(27).reshape(3,3,3)
ar


# In[85]:


np.random.rand(int(25))*100


# In[ ]:




