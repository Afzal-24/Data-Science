#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x=np.arange(1,11).reshape(5,2)
x


# In[6]:


y=np.arange(5)
list(y)


# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


x_train,x_test,y_train,y_test=train_test_split(x,y)


# In[9]:


x_train


# In[10]:


y_test


# In[11]:


y_train


# In[9]:


x_test


# # linear regression

# In[10]:


from sklearn.linear_model import LinearRegression


# In[11]:


model= LinearRegression()


# In[12]:


model.fit(x_train,y_train)


# In[13]:


model.predict(x_test)


# In[14]:


model.coef_


# MAE-MEAN ABSOLUTE ERROR
# MSE-MEAN SQUARED ERROR
# RMSE-ROOT MEAN SQUARED ERROR

# In[15]:


import pandas as pd
import seaborn as sns


# In[16]:


train=pd.read_csv('titanic_train.csv')


# In[17]:


train.head()


# In[18]:


sns.heatmap(train.isnull())


# In[19]:


train['Age']=train['Age'].fillna(method='ffill')


# In[20]:


train.drop('Cabin',axis=1,inplace=True)


# In[21]:


train.head()


# In[22]:


sns.heatmap(train.isnull())


# In[23]:


sex=pd.get_dummies(train['Sex'])
embark=pd.get_dummies(train['Embarked'])


# In[24]:


train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)


# In[25]:


sex


# In[26]:


embark


# In[27]:


from sklearn.model_selection import train_test_split


# In[28]:


x_train,x_test,y_train,y_test=train_test_split(train.drop('Survived',axis=1),train['Survived'],test_size=0.30,random_state=101)


# # LOGISTIC REGRESSION

# In[29]:


from sklearn.linear_model import LogisticRegression


# In[30]:


Logomodel=LogisticRegression()
Logomodel.fit(x_train,y_train)


# In[31]:


prediction=Logomodel.predict(x_test)


# In[32]:


prediction


# In[48]:


from sklearn.metrics import classification_report,confusion_matrix


# In[34]:


print(classification_report(y_test,prediction))


# # KNN

# In[52]:


from sklearn.neighbors import KNeighborsClassifier


# In[53]:


knn=KNeighborsClassifier(n_neighbors=1)


# In[54]:


knn.fit(x_train,y_train)


# In[55]:


pred=knn.predict(x_test)


# In[56]:


print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))


# # SCALER

# In[35]:


from sklearn.preprocessing import StandardScaler


# In[40]:


scaler=StandardScaler()


# In[41]:


scaler.fit(train.drop('Survived',axis=1))
scaled_features=scaler.transform(train.drop('Survived',axis=1))
df_feat=pd.DataFrame(scaled_features,columns=train.columns[1:])


# In[42]:


df_feat.head()


# # SVM

# In[43]:


from sklearn.svm import SVC


# In[44]:


model=SVC()


# In[45]:


model.fit(x_train,y_train)


# In[46]:


predict_svc=model.predict(x_test)


# In[49]:


print(confusion_matrix(y_test,predict_svc))

