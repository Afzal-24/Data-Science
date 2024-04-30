#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


df2=pd.DataFrame(np.random.randint(1,100,(4,3)),index=["Afzal","Aymaan","Fardin","Devshree"],columns=["Java","Python",".net"])
df2


# In[3]:


x =df2.index
y =df2["Python"]
plt.subplot(1,2,1)
plt.plot(x, y,"g^-")
plt.xlabel("marks")
plt.ylabel("students")
plt.title("Python marks ")
plt.grid(color='b', linestyle='--' )
plt.ylim(0,100)
plt.legend(['First line', 'Second line'])
plt.show()




x =df2.index
y =df2["Java"]
plt.subplot(1,2,1)
plt.plot(x, y,"r", marker='*', linestyle='-',data=df2)
plt.xlabel("marks")
plt.ylabel("students")
plt.title("Java marks ")
plt.grid(color='r', linestyle='--' )


# In[4]:


#legend
x =df2.index
y =df2["Python"]
plt.plot(x, y,"g^-")
plt.xlabel("student name")
plt.ylabel("student marks")
plt.title(" marks ")
y =df2["Java"]
plt.plot(x, y,"r*-")
plt.grid(color='r', linestyle='--' )
plt.ylim(0,100)
y =df2[".net"]
plt.plot(x, y,"y*-")

plt.legend(['Python', 'Java' ,".net"])


# In[5]:


plt.scatter(np.arange(10),np.arange(10)**2,c=np.arange(10), s=np.arange(10)**3, edgecolor="red"  )
plt.colorbar()


# In[6]:


plt.scatter(np.arange(10),np.arange(10)**2 )
plt.scatter(np.arange(10),np.arange(10)**2.1 )
plt.scatter(np.arange(10),np.arange(10)**2.2 )
plt.scatter(np.arange(10),np.arange(10)**2.3 )
plt.scatter(np.arange(10),np.arange(10)**2.4 )
plt.scatter(np.arange(10),np.arange(10)**2.5 )
plt.scatter(np.arange(10),np.arange(10)**2.6 )
plt.scatter(np.arange(10),np.arange(10)**2.7 )
plt.scatter(np.arange(10),np.arange(10)**2.8 )
plt.scatter(np.arange(10),np.arange(10)**2.9 )
plt.scatter(np.arange(10),np.arange(10)**3 )


# In[7]:


plt.stem([8,3,0,6,0,2,3,2,4,0],markerfmt="r*")
plt.stem([8,7,8,7,0,2,1,7,1,0],markerfmt="g*")


# In[8]:


df1=pd.DataFrame(np.random.randint(1,100,(4,3)),index=["Person1","Person2","Person3","Person4"],columns=["DSA","Php",".net"])
df1


# In[9]:


sns.displot(df1)


# In[10]:


penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")


# In[11]:


sns.jointplot(x=df1["DSA"],y=df1["Php"],data=df1)


# In[12]:


tips = sns.load_dataset("tips")
tips.head()


# In[13]:


sns.distplot(tips['total_bill'])


# In[14]:


sns.displot(tips['total_bill'])


# In[15]:


sns.distplot(tips['total_bill'],kde=False,bins=15)


# In[16]:


#Jointplot
#parameters in jointplot fpr 'kind' are: scatter, reg, resid, kde, hex
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')


# In[17]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[18]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[19]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='resid')


# In[20]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[21]:


#pairplot: allows us to plot pairwise relationships between variables within a dataset
sns.pairplot(tips)


# In[22]:


sns.pairplot(tips,hue='sex',palette='deep')


# In[26]:


sns.boxplot(data=tips)


# In[27]:


sns.barplot(data=tips )


# In[28]:


sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips,palette="coolwarm")


# In[32]:


sns.stripplot(data=tips)


# In[33]:


sns.swarmplot(data=tips)


# In[34]:


titanic=sns.load_dataset("titanic")


# In[35]:


titanic.head()


# In[36]:


sns.jointplot(x=titanic.fare , y=titanic.age ,data=titanic)


# In[37]:


sns.displot(data=titanic.fare)


# In[38]:


sns.boxplot(x=titanic.age ,y=titanic.deck ,data=titanic)

