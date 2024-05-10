#!/usr/bin/env python
# coding: utf-8

# In[24]:


def isAllNumeric(*args):
    for i in args:
        if isinstance (i , (int, float)):
            print("numeric")
        else:
            print("not numeric")
            
def sumOfAll(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


# In[ ]:




