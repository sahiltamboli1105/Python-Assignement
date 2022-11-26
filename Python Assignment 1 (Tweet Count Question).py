#!/usr/bin/env python
# coding: utf-8

# In[25]:


n = int(input())
dic = {}
for i in range(n):
    x = input().split()
    cnt = 1
    x_0 = x[0]
    if x_0 not in dic:
        dic[x_0] = [cnt]
    else:
        cnt = cnt+1
        dic[x_0] = [cnt]
MaxKey = max(dic, key=dic.get)
print(MaxKey, end = " ")
print(max(dic.values()))
        


# In[ ]:





# In[ ]:





# In[ ]:




