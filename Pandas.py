#!/usr/bin/env python
# coding: utf-8
Pandas
# In[4]:


#to store marks of students in a series
import pandas as pd
marks_list=[60,70,80]
labels=['Maths','OOP','Python']
a=pd.Series(data=marks_list, index=labels)
print(a)


# In[5]:


dict={"Name":"Afzal Kapadwala","Rollno":22000544, "Program":"BCA"}
s=pd.Series(dict)
s


# In[6]:


s.values


# In[7]:


import numpy as np
b=np.random.randint(0,100,(4,3))
b


# In[8]:


s.keys()


# In[10]:


s=pd.DataFrame(data=b,index=["person1","person2","person3","Person4"],columns=["RDBMS","Software",".NET"])
s


# In[11]:


s["Total"]=s["RDBMS"]+s["Software"]+s[".NET"]
s


# In[12]:


s["Percentage"]=s["Total"]/300*100
s


# In[13]:


s.loc[["person1","person2"]]


# In[14]:


s.tail(1)


# In[15]:


s.loc["person1"]


# In[16]:


s.loc["person2":]


# In[17]:


s.iloc[2:3]


# In[18]:


s.drop("Percentage",axis=1)


# In[ ]:





# In[19]:


s.drop("RDBMS",axis=1)


# In[20]:


s


# In[21]:


s.drop("Total",axis=1,inplace=True)


# In[22]:


s


# In[23]:


s.drop("person1",axis=0)


# In[24]:


#create a dataframe which has productid, product name, product price
import pandas as pd
product_id=[101,102,103,104,105]
product_name=["watch","keyboard","mouse","laptop","pc"]
product_price=[2000,3500,300,50000,25000]
df=pd.DataFrame(data=[product_id,product_name,product_price],index=["product_id","product_name","product_price"])


# In[25]:


df1=df.transpose()


# In[26]:


df1


# In[27]:


#to access each column
for d in df1:
    print(df1[d])


# In[28]:


#to access individual rows
for i in df1.iterrows():
    print(i)


# In[29]:


df1.iloc[0]


# In[30]:


df1.loc[:3,["product_name"]]


# In[31]:


s


# In[32]:


s.loc[s["Software"]<40,"Software"]=41
s


# In[33]:


df1.isnull()
#returns true for the places where null value exists. 


# In[34]:


df1.dropna() #drops the rows where null value exists. we can use the axis=1 attribute to drop  column


# In[35]:


df1.notnull() #returns true when the values are not null(NaN or none)


# In[36]:


df1.dropna(thresh=2) # drops the rows which exceeds the thresh. thresh=2 will keep the rows that has 1 NaN value but will delete for two more


# In[38]:


df1.fillna(value=4) # it will fill value 4 wherever Nan is


# In[41]:


import numpy as np
df=pd.read_csv("Salaries.csv")


# In[42]:


df=df.replace("Not Provided", np.nan)


# In[43]:


df


# In[44]:


df=df.replace("Not provided", np.nan)
df


# In[45]:


df['BasePay']=df['BasePay'].astype('float')


# In[46]:


df.info()


# In[47]:


df['BasePay'].mean()


# In[48]:


df['OvertimePay']=df['OvertimePay'].astype('float')


# In[49]:


df['OvertimePay'].max()

# Merging, Joining and Concatenating
# In[50]:


import pandas as pd
import numpy as np


# In[51]:


A=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[1,2,3], columns=[1,2,3])
A


# In[52]:


B=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[4,5,6], columns=[1,2,3])
B


# In[53]:


C=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[7,8,9], columns=[1,2,3])
C


# In[54]:


display(A, B, C,pd.concat([A,B,C]))


# In[55]:


left= pd.DataFrame({'key':['K0','K2','K5','K3'],
                   'A':['A0','A2','A5','A3'],
                   'B':['B0','B2','B5','B3']})

right= pd.DataFrame({'key':['K0','K1','K2','K9'],
                   'C':['C0','C1','C2','C9'],
                   'D':['D0','D1','D2','D9']})


# In[56]:


display(left, right, pd.merge(left, right, how='inner', on=['key']))


# In[57]:


pd.merge(left, right, how='outer', on=['key'])


# In[58]:


pd.merge(left, right, how='left', on=['key'])


# In[59]:


pd.merge(left, right, how='right', on=['key'])


# In[60]:


#Join
left.set_index('key',inplace=True)


# In[61]:


right.set_index('key',inplace=True)


# In[62]:


left.join(right,how='inner')


# In[63]:


left.join(right,how='outer')


# In[64]:


left.join(right,how='left')


# In[65]:


left.join(right,how='right')


# In[ ]:




