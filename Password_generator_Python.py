#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the necessary modules
import secrets
import string

print('Welcome to Password generator')

#Input the length of password
length = int(input('\nEnter the length of password: '))                      

#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Combine the data
all = lower + upper + num + symbols

#Use secrets

password = ''.join(secrets.choice(all) for i in range(length))  

#Print the password
print(password)


# In[ ]:




