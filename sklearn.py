#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


train = pd.read_csv("titanic_train.csv")


# In[4]:


train.head()


# In[5]:


train['Age']=train['Age'].fillna(method='ffill')


# In[6]:


sns.heatmap(train.isnull())


# In[7]:


train.drop('Cabin',axis = 1, inplace = True)


# In[8]:


train.head()


# In[9]:


sex = pd.get_dummies(train['Sex'])


# In[10]:


train.drop(['Sex','Embarked','Name','Ticket'],axis = 1, inplace = True)


# In[11]:


sex


# In[12]:


from sklearn.model_selection import train_test_split


# In[13]:


train.drop('Survived', axis = 1)


# In[14]:


x_train, x_test, y_train, y_test = train_test_split(train.drop('Survived',axis = 1),train['Survived'], test_size = 0.30,
                                                   random_state = 101)


# In[15]:


from sklearn.linear_model import LogisticRegression


# In[16]:


logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)


# In[17]:


prediction = logmodel.predict(x_test)


# In[18]:


prediction


# In[19]:


from sklearn.metrics import classification_report, confusion_matrix


# In[20]:


print(classification_report(y_test,prediction))


# In[21]:


print(confusion_matrix(y_test,prediction))


# In[22]:


from sklearn.tree import DecisionTreeClassifier


# In[23]:


dtree = DecisionTreeClassifier()


# In[24]:


dtree.fit(x_train,y_train)


# In[25]:


predict_tree = dtree.predict(x_test)


# In[26]:


from sklearn.metrics import classification_report,confusion_matrix


# In[27]:


print (classification_report(y_test,prediction))


# In[28]:


print (confusion_matrix(y_test, prediction))


# In[29]:


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(x_train,y_train)


# In[30]:


rfc


# In[31]:


rfc_pred = rfc.predict(x_test)


# In[32]:


print(confusion_matrix(y_test,rfc_pred))


# In[33]:


print (classification_report(y_test,rfc_pred))


# In[ ]:




