#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


# In[6]:


x,y=load_iris(return_X_y=True)


# In[25]:


x


# In[3]:


y


# # Elbow method

# indicating the ideal numbers of groups to divid the data into

# In[7]:


sse=[]
for k in range(1,11):
    km=KMeans(n_clusters=k,init='k-means++',max_iter=300,n_init=10,random_state=2)
    km.fit(x)
    sse.append(km.inertia_)


# In[8]:


plt.plot(sse)


# In[45]:


kmeans.inertia_


# In[10]:


g=sns.lineplot(x=range(1,11),y=sse)
g.set(xlabel="Number of cluster(k)",
     ylabel="Sum of squared error",
     title="Elbow method")


# In[21]:


#build kmeans cluster model
kmeans=KMeans(n_clusters=3,random_state=2)
kmeans.fit(x)


# In[23]:


#find cluster centers
kmeans.cluster_centers_


# In[24]:


pred=kmeans.fit_predict(x)


# In[42]:


kmeans.labels_


# In[43]:


pred


# In[41]:


plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker='^',color="red")
plt.scatter(x[:,0],x[:,1],c=kmeans.labels_)

fig,(ax1,ax2)=plt.subplots(1,2)
ax1.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],marker='^',color="red")
ax1.scatter(x[:,0],x[:,1],c=kmeans.labels_)
ax1.set_title('sepal length vs sepal width')

ax2.scatter(kmeans.cluster_centers_[:,2],kmeans.cluster_centers_[:,3],marker='^',color="red")
ax2.scatter(x[:,2],x[:,3],c=kmeans.labels_)
ax2.set_title('petal length vs petal width')


# # KMEANS CLUSTERING

# In[12]:


from sklearn.datasets import make_blobs


# In[13]:


data=make_blobs(n_samples=200,n_features=2,centers=4,cluster_std=1.8,random_state=101)


# In[14]:


data


# In[16]:


plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')


# In[17]:


kmeans=KMeans(n_clusters=4)


# In[19]:


kmeans.fit(data[0])


# In[20]:


kmeans.cluster_centers_


# In[ ]:




