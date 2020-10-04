
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


crime=pd.read_csv('crime.csv')


# In[5]:


crime


# In[3]:


type(crime)


# In[4]:


crime.head()


# In[3]:


crime.tail(10)


# In[6]:


crime1 =crime[['Category', 'DayOfWeek','PdDistrict']]


# In[7]:


crime1


# In[4]:


crime_sorted = crime.sort_values("Category",ascending=True)


# In[13]:


crime_sorted


# In[14]:


crime.info()


# In[7]:


crime_sorted['Category'].hist()
plt.title('Histogram of Categoty of crime')
plt.xlabel('category')
plt.ylabel('Frequency')
plt.show()


# In[5]:


count_category=crime['Category'].value_counts()
count_category


# In[7]:


sample1=count_category.head()
sample1


# In[8]:


type(count_category)


# In[9]:


df=pd.DataFrame(count_category)
df


# In[11]:


DF1=df.reset_index()
DF1


# In[12]:





DF1.columns=['Category','Freq']
DF1
Sample=DF1.head()
Sample


# In[13]:


DF1.columns=['Category','Freq']
DF1
sample=DF1.head()


# In[14]:


sample


# In[27]:


df=pd.DataFrame(count_category)
df


# In[13]:


DF1=df.reset_index()
DF1


# In[28]:


type(DF1)


# In[29]:


DF1_Desc=DF1.sort_values("Category",ascending=False)
DF1_Desc


# In[13]:


DF1.columns=['Category','Freq']
DF1
Sample=DF1.head()
Sample


# In[14]:



plt.bar(Sample['Category'],Sample['Freq'],color="Red")
plt.xlabel("Category")
plt.ylabel("Freq")
plt.title("The Freq of Category of Crime")
plt.show()


# In[15]:


count_Dayofweek=crime['DayOfWeek'].value_counts()
count_Dayofweek


# In[16]:


type(count_Dayofweek)
df2=pd.DataFrame(count_Dayofweek)
df2
DF2=df2.reset_index()
DF2
DF2.columns=['Dayofweek','Freq']
DF2


# In[17]:


plt.bar(DF2['Dayofweek'],DF2['Freq'],color=['Red','Yellow','Green'])
plt.title('The Freq of crime daywise')
plt.show()


# In[18]:


count_Pd_district=crime['PdDistrict'].value_counts()
count_Pd_district
type(count_Pd_district)


# In[19]:


df3=pd.DataFrame(count_Pd_district)
df3


# In[20]:



DF3=df3.reset_index()
DF3
DF3.columns=['PdDistrict','Freq']
DF3


# In[21]:


plt.pie(DF3['Freq'], labels=DF3['PdDistrict']) 
plt.title("The Pie Plot")
plt.show()


# In[3]:


count_resolved=crime['Resolution'].value_counts()
count_resolved


# In[4]:


type(count_resolved)


# In[5]:


df4=pd.DataFrame(count_resolved)


# In[24]:


df4
type(df4)


# In[6]:



DF4=df4.reset_index()
DF4
DF4.columns=['Resolution','Freq']
DF4


# In[7]:


x=["Arrest","Pending"]
x


# In[8]:


y=[sum(DF4.iloc[[1,2],1]),sum(DF4.iloc[2:17,1]+DF4.iloc[0,1])]
y
plt.bar(x,y,color=["Green","Red"])
plt.xlabel("Resolution")
plt.ylabel("Frequency")
plt.title("The Resolved vs Pending Cases")
plt.show()


# In[9]:


y

