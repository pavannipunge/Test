#!/usr/bin/env python
# coding: utf-8

# #  Case Study 1: Sales Analysis

# You have a dataset containing sales data with information like product ID, sales quantity, and revenue. Perform the following tasks:
# Load the dataset and inspect its structure.
# Clean the data (handle missing values, duplicates, etc.).
# Calculate total revenue and quantity sold for each product.
# Find the top-selling products.
# Analyze monthly sales trends.

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("E:\\Ed - Byte\\Test 3\\sales data.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.sample(8)


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


duplicates = df[df.duplicated()]    # check for duplicates entries
duplicates


# In[10]:


df.columns


# # Now calculate  the total Revenue

# In the dataframe, we have columns like Quantity and Price per Quatity. from this we can calculate the total revenue.

# In[11]:


df['Revenue'] = df['Quantity'] * df['Price per Quatity']


# In[12]:


df.sample(3)


# In[13]:


total_revenue = (df['Quantity'] * df['Price per Quatity']).sum()
print("Total Revenue:",total_revenue  )
                                    


# In[14]:


# Now calculate the quanty sold for each product


# In[15]:


quantity_sold = df.groupby('Sub-Category')['Quantity'].sum()
quantity_sold


# In[16]:


max_selling_category = quantity_sold.idxmax()
print("Max selling category:", max_selling_category)


# #  Case Study 2 Employee Performance Analysis

# Problem Statement:
# You have a dataset with information about employees, including their performance ratings, years of experience, and department. Perform the following tasks:
# 
# Load the dataset and understand its structure.
# Explore the distribution of performance ratings.
# Identify factors affecting performance (e.g., experience, department).
# Calculate average performance ratings for each department.
# Visualize the performance distribution using histograms.

# In[17]:


df1 = pd.read_csv("E:\\Ed - Byte\\Test 3\\Attrition.csv")


# In[18]:


df1.head()


# In[19]:


df1.tail()


# In[20]:


df1.shape


# In[21]:


df1.info()


# In[22]:


df1.describe()


# In[23]:


df1.isnull().sum()


# #  Now Explore the distribution of performance ratings.

# In[25]:


# Count the occurrences of each performance rating
performance_rating_counts = df1['PerformanceRating'].value_counts()
performance_rating_counts


# In[26]:


# Count the occurrences of each performance rating
df1['PerformanceRating'].value_counts().plot(kind = 'bar')


# #  Lets find factor affecting on performance

# In[29]:


df1.columns


# In[30]:


q = pd.crosstab(df1['PerformanceRating'], df1['Education'])
sns.heatmap(q)


# In[31]:


#  above heatmap shows employee having higher education had less performance rating.
# so education is one of the factor which can impact on permance of an employee.


# In[32]:


df1.head()


# In[33]:


sns.barplot(y=df1['Age'],x=df1['PerformanceRating'],hue = df1['Gender'])


# In[34]:


# from above graph we able to see in both performance rating female's are more productive than male in similar age group.


# In[37]:


sns.barplot(x = df1['PerformanceRating'], y = df1['HourlyRate'], hue = df1['JobSatisfaction'])


# In[38]:


# from above graph we can say that higher the hourly then performance and job satisfaction
# of an enmployee is also high.


# In[48]:


sns.barplot(x= df1['PerformanceRating'], y= df1['BusinessTravel'])


# In[44]:


# above graph shows that empoyee who did not travel for the job they perform better.


# In[51]:


sns.scatterplot(x=df1['YearsWithCurrManager'],y= df1[ 'YearsInCurrentRole'], hue = df1['PerformanceRating'])


# In[52]:


# above scatterplot shows that employee having  less years in organization perform better than who having more experience.


# In[53]:


# Calculate average performance ratings for each department
average_performance_by_department = df1.groupby('Department')['PerformanceRating'].mean()
average_performance_by_department


# In[54]:


df1.groupby('Department')['PerformanceRating'].mean().plot(kind='bar')


# In[ ]:




