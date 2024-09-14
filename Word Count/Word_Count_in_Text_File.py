#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Word Count in text file
with open(r"C:\Users\Inspiron_5502\OneDrive\Desktop\Coursera\Google Python\Python Notes.txt", "r", encoding="utf-8") as file:
    count = 0
    
    # Loop through each line in the file
    for line in file:
        words = line.split(" ")  # Split the line into words
        count += len(words)  # Count the words in the current line

print(f"Total word count: {count}")


# In[ ]:




