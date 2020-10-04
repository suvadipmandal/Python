
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


crew= pd.read_csv('crew.csv')
print(crew)


# In[4]:


crew.head()


# In[5]:


crew.tail()


# In[4]:


crew['Salary'].sum()


# In[5]:


crew['Salary'].mean()


# In[6]:


crew['bonus']=crew.Salary*.1


# In[7]:


crew['Newsal']=crew.Salary+crew.bonus
crew


# In[9]:


crew1 =crew[['JobCode', 'homebase','Salary']]


# In[12]:


crew1


# In[10]:


crew1.head()


# In[14]:


crew1.tail()


# In[15]:


crew_sorted = crew.sort_values("Salary",ascending=True)


# In[16]:


crew_sorted


# In[11]:


crew_desc_sorted = crew.sort_values("Salary",ascending=False)


# In[12]:


crew_desc_sorted


# In[13]:


crew_desc_sorted['Salary'].hist()
plt.title('Histogram of Salary of Crew Data')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# In[27]:


crew_desc_sorted['Salary'].median()


# In[5]:


#Conditional Data Extraction
Fltat=crew[crew.JobCode=="FLTAT1"]


# In[32]:


Fltat


# In[6]:


crew_sal=crew[crew.Salary >90000]
crew_sal


# In[7]:


crew_sal_less=crew[crew.Salary<=75000]
crew_sal_less


# In[8]:


crew_sal_less.count()


# In[9]:


crew.count()


# In[14]:


crew.hist()
plt.show()


# In[12]:


count_Jobcode=crew['JobCode'].value_counts()
count_Jobcode



# In[21]:



plt.bar(['FLTAT2','FLTAT1','FLTAT3','PILOT2','PILOT3','PILOT1'],count_Jobcode,color='Red')
plt.title('The Freq of Jobcode')


# In[ ]:


plt.bar(['FLTAT2','FLTAT1','FLTAT3','PILOT2','PILOT3','PILOT1'],count_Jobcode,color='Red')
plt.title('The Freq of Jobcode')


# In[11]:


crew['Salary'].mean()


# In[13]:


crew_sal['Salary'].mean()


# In[14]:


crew_sal_diff= crew['Salary'].max() - crew['Salary'].min()
crew_sal_diff


# In[15]:


#Statistical Overview
crew.describe()

