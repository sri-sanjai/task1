#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt




# In[8]:


data = pd.read_csv('titanic.csv')



# In[9]:


ages = data['Age']


# In[11]:





# In[ ]:





# In[5]:


ages.dropna(inplace=True)


# In[6]:


plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[ ]:




