#!/usr/bin/env python
# coding: utf-8

# In[7]:


import seaborn as sns
import pandas as pd


# In[4]:


df=sns.load_dataset('iris')


# In[5]:


df.head()


# In[11]:


x=df.drop(['species'],axis=1)
y=df['species']


# In[12]:


x


# In[15]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score


# In[16]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=101)


# # LogisticRegression

# In[17]:


Logomodel=LogisticRegression()
Logomodel.fit(x_train,y_train)


# In[18]:


prediction=Logomodel.predict(x_test)


# In[19]:


prediction


# In[20]:


print(classification_report(y_test,prediction))


# In[27]:


print (confusion_matrix(y_test, prediction))


# # DecisionTree

# In[21]:


from sklearn.tree import DecisionTreeClassifier


# In[22]:


dtree = DecisionTreeClassifier()


# In[23]:


dtree.fit(x_train,y_train)


# In[24]:


predict_tree = dtree.predict(x_test)


# In[39]:


predict_tree


# In[40]:


print(accuracy_score(y_test,predict_tree))


# In[28]:


print (classification_report(y_test,predict_tree))


# In[29]:


print (confusion_matrix(y_test, predict_tree))


# # KNN

# In[30]:


from sklearn.neighbors import KNeighborsClassifier


# In[31]:


knn=KNeighborsClassifier(n_neighbors=1)


# In[32]:


knn.fit(x_train,y_train)


# In[33]:


pred=knn.predict(x_test)


# In[36]:


pred


# In[34]:


print(confusion_matrix(y_test,pred))


# In[37]:


print(accuracy_score(y_test,pred))


# In[35]:


print (classification_report(y_test,pred))


# # RandomForest

# In[41]:


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(x_train,y_train)


# In[42]:


rfc


# In[43]:


rfc_pred = rfc.predict(x_test)


# In[44]:


rfc_pred


# In[45]:


print(confusion_matrix(y_test,rfc_pred))


# In[46]:


print (classification_report(y_test,rfc_pred))


# In[47]:


print(accuracy_score(y_test,rfc_pred))

