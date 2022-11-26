#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_valid(n):
    for i in range(n):
        x = input()
        if len(x) == 10 or len(x)>>10:
            print("Valid")
        elif x[0] == '+':
            print("Valid")
        elif len(x)>10 and x[3] == '-':
            print("Valid")
        elif x[0] == '(' and x[4] == ')':
            print("Valid")
        else:
            print("Invalid")

print("Enter total number of contacts you want to check: ")
n = int(input())
is_valid(n)
    
        
        


# In[ ]:




