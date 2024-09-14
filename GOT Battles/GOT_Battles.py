#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
#from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import os,sys
import gc


# In[19]:


#Upload the csv file
battle = pd.read_csv(r"C:\Users\Inspiron_5502\OneDrive\Desktop\Python Projects For Fun\GOT Battles\battles.csv")

#Read the first few rows
#print(battle.head()) 

battle.head() # use this to get the data in the tabular format, You can also add head(10) for first 10 rows


# In[20]:


battle.tail() # This is for last five rows


# In[21]:


battle.shape # Get the number of rows and columns, format: (rows, columns)


# In[22]:


# Check if there are any null values in the entire DataFrame
null_counts = battle.isnull().sum()
print(null_counts)


# In[23]:


#How to change the column name in the data frame
battle.rename(columns={'attacker_1' : 'primary_attacker'}, inplace=True)
battle.head()


# In[24]:


# Change the row names
#battle.rename(index={0: 'Row1', 1: 'Row2', 2: 'Row3'}, inplace=True)
#battle.head()


# In[31]:


#How to check how many times each unique value is repeated in a specific column 
battle['attacker_king'].value_counts() 


# In[32]:


#How to check how many times each unique value is repeated in a specific column 
battle['defender_king'].value_counts()


# In[33]:


#How to check how many times each unique value is repeated in a specific column 
battle['year'].value_counts() 


# In[52]:


sns.set(rc={'figure.figsize': (13, 6)})
sns.set_palette("deep")
sns.barplot(x = 'attacker_king', y = 'attacker_size', data = battle)
plt.title('Attacker Side')
plt.xlabel('Attacker King')
plt.ylabel('Attacker Size')
plt.show()


# In[53]:


sns.set(rc={'figure.figsize': (15, 6)})
sns.set_palette("pastel")
sns.barplot(x = 'defender_king', y = 'defender_size', data = battle)
plt.title('Defender Side')
plt.xlabel('Defender King')
plt.ylabel('Defender Size')
plt.show()


# In[54]:


# Count the number of battles for each attacker against each defender
battle_counts = battle.groupby(['attacker_king', 'defender_king']).size().reset_index(name='counts')

# Set the figure size
sns.set(rc={'figure.figsize': (13, 5)})

# Create the bar plot
sns.barplot(x='attacker_king', y='counts', hue='defender_king', data=battle_counts)

# Show the plot
plt.title('Number of Battles by Attacker King and Defender King')
plt.xlabel('Attacker King')
plt.ylabel('Number of Battles')
plt.legend(title='Defender King')
plt.show()


# In[55]:


death = pd.read_csv(r"C:\Users\Inspiron_5502\OneDrive\Desktop\Python Projects For Fun\GOT Battles\character-deaths.csv")


# In[56]:


death.head()


# In[57]:


death.tail()


# In[60]:


death.shape


# In[62]:


death['Gender'].value_counts()


# In[63]:


death['Nobility'].value_counts()


# In[66]:


# Assuming 'death' is your DataFrame and 'Death Year' is the column you're interested in
sns.countplot(x='Death Year', data=death)

# Add title and labels
plt.title('Count of Deaths by Year')  # Optional: Add a title for better understanding
plt.xlabel('Death Year')               # Optional: Add x-label
plt.ylabel('Count')                     # Optional: Add y-label

# Show the plot
plt.show()


# In[67]:


# Set the figure size & Create a count plot for allegiances
sns.set(rc={'figure.figsize': (30, 10)})
sns.countplot(x='Allegiances', data=death)

# Add title and labels
plt.title('Count of Deaths by Allegiance')
plt.xlabel('Allegiances')
plt.ylabel('Count')
# Show the plot
plt.show()


# In[ ]:




