#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from scipy import stats
from tqdm import tqdm


# In[2]:


# data = pd.read_csv("outfield_full_skill.csv")
data = pd.read_csv("gk_full_skill.csv")


# In[3]:


x = data.corr(method='spearman')


# In[4]:


for x in tqdm(range(1, 21)):
    data = pd.read_csv("gk_full_skill.csv")
    for y in tqdm(range (1, x)) :
        data = data.replace(y, 0)
    for z in tqdm(range (x, 21)) :
        data = data.replace(z, 1)
    c = data.corr(method='spearman')
    c.to_csv('c_gk_' + str(x) + '.csv')


# In[5]:


attributes = ['goa', 'hid', 'men', 'mtr', 'phy']
for attribute in attributes :
    for x in tqdm(range(1, 21)):
        data = pd.read_csv("gk_" + attribute + "_full_skill.csv")
        for y in tqdm(range (1, x)) :
            data = data.replace(y, 0)
        for z in tqdm(range (x, 21)) :
            data = data.replace(z, 1)
        c = data.corr(method='spearman')
        c.to_csv('c_' + attribute + "_" + str(x) + '.csv')


# In[6]:


goa = pd.read_csv("gk_goa_full_skill.csv")
hid = pd.read_csv("gk_hid_full_skill.csv")
men = pd.read_csv("gk_men_full_skill.csv")
mtr = pd.read_csv("gk_mtr_full_skill.csv")
phy = pd.read_csv("gk_phy_full_skill.csv")


# In[7]:


goa_x = goa.corr(method='spearman')
hid_x = hid.corr(method='spearman')
men_x = men.corr(method='spearman')
mtr_x = mtr.corr(method='spearman')
phy_x = phy.corr(method='spearman')


# In[8]:


goa_x.to_csv('goa_cor.csv')
hid_x.to_csv('hid_cor.csv')
men_x.to_csv('men_cor.csv')
mtr_x.to_csv('mtr_cor.csv')
phy_x.to_csv('phy_cor.csv')


# In[ ]:





# In[ ]:




