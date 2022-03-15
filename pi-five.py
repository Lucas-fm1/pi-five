#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np

num = input('Choose the number of 5s:\n')

inum = 0
for i in range(int(num)):
    inum = inum + pow(10,int(i))*5
print('\nString of fives:', inum)
    
inv = 1/inum
res = np.sin(np.deg2rad(inv))
print('\nPi aproximation:')
print('sin( 1 /', inum, ') =', res)

