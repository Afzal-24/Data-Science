#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1d array
import numpy as np
a=np.arange(0,10)
a


# In[6]:


#2d array
b=np.arange(0,9).reshape(3,3)
b


# In[7]:


#3d array
c=np.arange(0,12).reshape(3,2,2)
c


# In[9]:


#to know the dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)


# In[12]:


marks=np.random.randint(0,100,20)
marks


# In[13]:


aes=np.sort(marks)
aes


# In[15]:


#deep copying
co=np.copy(aes)
co


# In[32]:


#
identity=np.eye(5).reshape(25)
identity


# In[29]:


identity=np.eye(5).flatten()
identity


# In[33]:


identity=np.eye(5).ravel()
identity


# In[37]:


get_ipython().run_line_magic('pinfo', 'np.ravel')


# In[36]:


get_ipython().run_line_magic('pinfo', 'identity.flatten')


# In[44]:


np.append(b,[[10,12,13]],axis=0)


# In[49]:


np.eye(4)+4


# In[52]:


farr=np.random.uniform(1,20,5)
farr


# In[53]:


np.ceil(farr)


# In[54]:


np.floor(farr)


# In[55]:


np.round(farr,decimals=3)


# In[59]:


mat=np.arange(0,25).reshape(5,5)
mat


# In[60]:


np.min(mat)


# In[61]:


np.max(mat)


# In[66]:


np.std(mat)


# In[73]:


null_vector=np.arange(0,11,dtype=float)
null_vector


# In[74]:


null_vector[:]='NaN'
null_vector


# In[75]:


null_vector[6]=200
null_vector


# In[78]:


#1d array vector
arr_vector=np.arange(100,151)
arr_vector


# In[79]:


#To reverse an array
np.flip(arr_vector)


# In[84]:


#returns indices for a condtion
list=[1,0,2,0,0,4,0,8]
arr=np.array(list)
np.where(arr>0)


# In[89]:


n=np.ones(100).reshape(10,10)
n[1:9,1:9]=0
n


# In[2]:


import numpy as np
np.linspace(0,1,10)


# In[5]:


get_ipython().run_line_magic('pinfo', 'np.random.uniform')


# In[6]:


import numpy as np
list=[1,2,3]
np.array(list)

