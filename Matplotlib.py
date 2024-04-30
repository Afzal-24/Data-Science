#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[1]:


import numpy as np
x= np.linspace(0,5,11)
y= x**2


# In[4]:


x


# In[5]:


y


# In[15]:


plt.plot(x,y,'b>')#b is for blue colour and > is for linestyle
plt.xlabel('x axis title')
plt.ylabel('y axis title')
plt.title('chart')
plt.xlim(-5,100)#sets limit for the x axis
plt.ylim(-5,100)#sets limit for the y axis
plt.show()


# In[ ]:


'''attributes for chart in plt.show():
x axis
y axis
color
linstyle
marker
'''


# In[ ]:


#types ofmarker
marker='0'
marker='.'
marker='x'
marker='+'
marker='^'
marker='*'
marker='s'
marker='d'


# In[10]:


#plt.subplot() is used for plotting multple charts in a single plot area
plt.subplot(1,2,1) # the parameters for tjis will be rows, columns and chart no.
plt.plot(x,y,'b')
plt.subplot(1,2,2) # targets the second chart of the single plot
plt.plot(x,y,'r')
plt.show()


# In[4]:


get_ipython().run_line_magic('pinfo', 'plt.subplot')


# In[23]:


plt.subplot(1,3,1)
plt.plot(x,y,'m.')
plt.xlabel('x axis of subplot1')
plt.ylabel('y axis of subplot1')
plt.xlim(-5,10)
plt.ylim(-5,20)
plt.subplot(1,3,2)
plt.plot(x,y,'g-.')
plt.xlabel('x axis of subplot2')
plt.ylabel('y axis of subplot2')
plt.xlim(-10,20)
plt.ylim(-10,20)
plt.subplot(1,3,3)
plt.plot(x,y,'k^')
plt.show()


# In[8]:


plt.subplot(1,3,1)


# In[ ]:


#Object oriented approach
#this approach is nicer when dealing with a canvas that has multiple plots in it


# In[42]:


#Creates a figure(empty canvas)
fig= plt.figure()
# to add axes
axes= fig.add_axes([0.1,0.1, 0.9, 0.9]) # left, bottom, width, height
axes2= fig.add_axes([0.2,0.5,0.4,0.3])
axes3= fig.add_axes([0.7,0.1,0.3,0.3])

#plot on that set of axes
axes.plot(x,y,'r')
axes.set_xlabel('x axis label')
axes.set_ylabel('y axis label')
axes.set_title(' set title')

#second chart
axes2.plot(x,y,'g-.')
axes2.set_xlabel('x axis label')
axes2.set_ylabel('y axis label')
axes2.set_title(' set title')


# In[21]:


#Scatter Plot
a=np.arange(10)
b=a**2
c1=np.random.randint(0,100,10)#to make all markers of different colors
#plotting a scatter plot
plt.scatter(a,b,c=c1,s=100,edgecolor='white',marker='p',linewidth=1.75,cmap='brg') #s for size, 's' in marker is for square

plt.colorbar() #to show a color bar at the side


# In[5]:


get_ipython().run_line_magic('pinfo', 'plt.scatter')


# In[25]:


#histogram
plt.hist(a,b)


# In[31]:


from random import sample
data= sample(range(1,1000),100)
plt.hist(data,color='g',linewidth=0.6,edgecolor='red')


# In[37]:


plt.stem(data)


# In[35]:


plt.stairs(data)


# In[45]:


#stackplot
x=np.arange(0,100,10)

y=np.random.randint(0,100,10)
z=x*2
plt.stackplot(x,y,z)


# In[48]:


x=[1,2,3,4]
e=(0.4,0,0,0)
plt.pie(x,explode=e)


# In[49]:


#boxplot
d=np.random.normal(0,100,60)
plt.boxplot(d)


# In[53]:


data=[np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data,vert=False,patch_artist=True)


# In[54]:


data=[np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data,vert=True,patch_artist=True)

