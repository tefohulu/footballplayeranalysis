#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sys
import pandas as pd
from tqdm import tqdm
from itertools import combinations, groupby
from collections import Counter
from IPython.display import display
pd.options.display.max_columns = 60
pd.options.display.max_rows = 120
pd.options.mode.chained_assignment = None


# In[2]:


data = pd.read_csv("outfield_full_skill.csv")
data.head()


# In[3]:


data_full_skill = data


# In[4]:


for y in tqdm(range (1, 11)) :
    data_full_skill = data_full_skill.replace(y, 0)
for z in tqdm(range (11, 21)) :
    data_full_skill = data_full_skill.replace(z, 1)


# In[5]:


for col in tqdm(data_full_skill.columns):
    data_full_skill.loc[data_full_skill[col] == 0, col] = np.nan
    data_full_skill.loc[data_full_skill[col] == 1, col] = col


# In[6]:


records = []
hid_only = []
men_only = []
mtr_only = []
phy_only = []
tec_only = []


# In[7]:


for i in tqdm(range(0, 47733)):
    records.append(
        [str(data_full_skill.values[i, j]) for j in range(0, 49) if (pd.notnull(data_full_skill.values[i, j]))])
    hid_only.append(
        [str(data_full_skill.values[i, j]) for j in range(0, 5) if (pd.notnull(data_full_skill.values[i, j]))])
    men_only.append(
        [str(data_full_skill.values[i, j]) for j in range(5, 19) if (pd.notnull(data_full_skill.values[i, j]))])
    mtr_only.append(
        [str(data_full_skill.values[i, j]) for j in range(19, 27) if (pd.notnull(data_full_skill.values[i, j]))])
    phy_only.append(
        [str(data_full_skill.values[i, j]) for j in range(27, 35) if (pd.notnull(data_full_skill.values[i, j]))])
    tec_only.append(
        [str(data_full_skill.values[i, j]) for j in range(35, 49) if (pd.notnull(data_full_skill.values[i, j]))])


# In[8]:


data_full_skill['index_col'] = data_full_skill.index + 1


# In[9]:


data_full_skill = data_full_skill[['index_col',
                                  'hid_con', 'hid_dir', 'hid_imp', 'hid_inj', 'hid_ver',
                                  'men_agg', 'men_ant', 'men_bra', 'men_com', 'men_con', 'men_dec', 'men_det', 'men_fla', 'men_lea', 'men_off', 'men_pos', 'men_tea', 'men_vis', 'men_wor', 
                                  'mtr_ada', 'mtr_amb', 'mtr_con', 'mtr_loy', 'mtr_pre', 'mtr_pro', 'mtr_spo', 'mtr_tem', 
                                  'phy_acc', 'phy_agi', 'phy_bal', 'phy_jum', 'phy_nat', 'phy_pac', 'phy_sta', 'phy_str',
                                  'tec_cor', 'tec_cro', 'tec_dri', 'tec_fin', 'tec_fir', 'tec_fre', 'tec_hea', 'tec_lsh', 'tec_lth', 'tec_mar', 'tec_pas', 'tec_pen', 'tec_tac', 'tec_tec']]


# In[10]:


data_full_skill_hid = data_full_skill[['index_col',
                                  'hid_con', 'hid_dir', 'hid_imp', 'hid_inj', 'hid_ver']]
data_full_skill_men = data_full_skill[['index_col',
                                  'men_agg', 'men_ant', 'men_bra', 'men_com', 'men_con', 'men_dec', 'men_det', 'men_fla', 'men_lea', 'men_off', 'men_pos', 'men_tea', 'men_vis', 'men_wor']]
data_full_skill_mtr = data_full_skill[['index_col',
                                  'mtr_ada', 'mtr_amb', 'mtr_con', 'mtr_loy', 'mtr_pre', 'mtr_pro', 'mtr_spo', 'mtr_tem']]
data_full_skill_phy = data_full_skill[['index_col',
                                  'phy_acc', 'phy_agi', 'phy_bal', 'phy_jum', 'phy_nat', 'phy_pac', 'phy_sta', 'phy_str']]
data_full_skill_tec = data_full_skill[['index_col',
                                  'tec_cor', 'tec_cro', 'tec_dri', 'tec_fin', 'tec_fir', 'tec_fre', 'tec_hea', 'tec_lsh', 'tec_lth', 'tec_mar', 'tec_pas', 'tec_pen', 'tec_tac', 'tec_tec']]


# In[11]:


data_full_skill['records'] = pd.DataFrame({'records' : records})


# In[12]:


data_full_skill = data_full_skill.drop(['hid_con', 'hid_dir', 'hid_imp', 'hid_inj', 'hid_ver',
                  'men_agg', 'men_ant', 'men_bra', 'men_com', 'men_con', 'men_dec', 'men_det', 'men_fla', 'men_lea', 'men_off', 'men_pos', 'men_tea', 'men_vis', 'men_wor', 
                  'mtr_ada', 'mtr_amb', 'mtr_con', 'mtr_loy', 'mtr_pre', 'mtr_pro', 'mtr_spo', 'mtr_tem', 
                  'phy_acc', 'phy_agi', 'phy_bal', 'phy_jum', 'phy_nat', 'phy_pac', 'phy_sta', 'phy_str',
                  'tec_cor', 'tec_cro', 'tec_dri', 'tec_fin', 'tec_fir', 'tec_fre', 'tec_hea', 'tec_lsh', 'tec_lth', 'tec_mar', 'tec_pas', 'tec_pen', 'tec_tac', 'tec_tec'], axis=1)


# In[13]:


data_full_skill.to_csv('data_full_skill.csv', sep='\t')


# In[14]:


data_hid_only = pd.DataFrame({'hid_only' : hid_only})
data_men_only = pd.DataFrame({'men_only' : men_only})
data_mtr_only = pd.DataFrame({'mtr_only' : mtr_only})
data_phy_only = pd.DataFrame({'phy_only' : phy_only})
data_tec_only = pd.DataFrame({'tec_only' : tec_only})


# In[15]:


data_hid_only.to_csv('data_hid_only.csv', sep='\t')
data_men_only.to_csv('data_men_only.csv', sep='\t')
data_mtr_only.to_csv('data_mtr_only.csv', sep='\t')
data_phy_only.to_csv('data_phy_only.csv', sep='\t')
data_tec_only.to_csv('data_tec_only.csv', sep='\t')


# In[16]:


data_full_skill_hid['records'] = pd.DataFrame({'hid_only' : hid_only})
data_full_skill_men['records'] = pd.DataFrame({'men_only' : men_only})
data_full_skill_mtr['records'] = pd.DataFrame({'mtr_only' : mtr_only})
data_full_skill_phy['records'] = pd.DataFrame({'phy_only' : phy_only})
data_full_skill_tec['records'] = pd.DataFrame({'tec_only' : tec_only})


# In[17]:


data_full_skill_hid.drop(['hid_con', 'hid_dir', 'hid_imp', 'hid_inj', 'hid_ver'], axis=1)
data_full_skill_men.drop(['men_agg', 'men_ant', 'men_bra', 'men_com', 'men_con', 'men_dec', 'men_det', 'men_fla', 'men_lea', 'men_off', 'men_pos', 'men_tea', 'men_vis', 'men_wor'], axis=1)
data_full_skill_mtr.drop(['mtr_ada', 'mtr_amb', 'mtr_con', 'mtr_loy', 'mtr_pre', 'mtr_pro', 'mtr_spo', 'mtr_tem'], axis=1)
data_full_skill_phy.drop(['phy_acc', 'phy_agi', 'phy_bal', 'phy_jum', 'phy_nat', 'phy_pac', 'phy_sta', 'phy_str'], axis=1)
data_full_skill_tec.drop(['tec_cor', 'tec_cro', 'tec_dri', 'tec_fin', 'tec_fir', 'tec_fre', 'tec_hea', 'tec_lsh', 'tec_lth', 'tec_mar', 'tec_pas', 'tec_pen', 'tec_tac', 'tec_tec'], axis=1)


# In[18]:


all_final = data_full_skill.apply(lambda x : pd.Series(x['records']), axis=1).stack().reset_index(level=1, drop=True)
hid_final = data_full_skill_hid.apply(lambda x: pd.Series(x['records']),axis=1).stack().reset_index(level=1, drop=True)
men_final = data_full_skill_men.apply(lambda x: pd.Series(x['records']),axis=1).stack().reset_index(level=1, drop=True)
mtr_final = data_full_skill_mtr.apply(lambda x: pd.Series(x['records']),axis=1).stack().reset_index(level=1, drop=True)
phy_final = data_full_skill_phy.apply(lambda x: pd.Series(x['records']),axis=1).stack().reset_index(level=1, drop=True)
tec_final = data_full_skill_tec.apply(lambda x: pd.Series(x['records']),axis=1).stack().reset_index(level=1, drop=True)


# In[19]:


all_final_df = pd.DataFrame(all_final)
all_final_df = all_final_df.reset_index()
all_final_df = all_final_df.rename(columns={0 : 'all_final', 'index' : 'list_id'})
all_final_df = all_final_df.set_index('list_id')['all_final']

hid_final_df = pd.DataFrame(hid_final)
hid_final_df = hid_final_df.reset_index()
hid_final_df = hid_final_df.rename(columns={0 : 'hid_final', 'index' : 'list_id'})
hid_final_df = hid_final_df.set_index('list_id')['hid_final']

men_final_df = pd.DataFrame(men_final)
men_final_df = men_final_df.reset_index()
men_final_df = men_final_df.rename(columns={0 : 'men_final', 'index' : 'list_id'})
men_final_df = men_final_df.set_index('list_id')['men_final']

mtr_final_df = pd.DataFrame(mtr_final)
mtr_final_df = mtr_final_df.reset_index()
mtr_final_df = mtr_final_df.rename(columns={0 : 'mtr_final', 'index' : 'list_id'})
mtr_final_df = mtr_final_df.set_index('list_id')['mtr_final']

phy_final_df = pd.DataFrame(phy_final)
phy_final_df = phy_final_df.reset_index()
phy_final_df = phy_final_df.rename(columns={0 : 'phy_final', 'index' : 'list_id'})
phy_final_df = phy_final_df.set_index('list_id')['phy_final']

tec_final_df = pd.DataFrame(tec_final)
tec_final_df = tec_final_df.reset_index()
tec_final_df = tec_final_df.rename(columns={0 : 'tec_final', 'index' : 'list_id'})
tec_final_df = tec_final_df.set_index('list_id')['tec_final']


# In[20]:


def size(obj):
    return "{0:.2f} MB".format(sys.getsizeof(obj) / (1000 * 1000))


# In[21]:


def freq(iterable):
    if type(iterable) == pd.core.series.Series:
        return iterable.value_counts().rename("freq")
    else:
        return pd.Series(Counter(iterable)).rename("freq")


# In[22]:


def order_count(order_item):
    return len(set(order_item.index))


# In[23]:


def get_item_pairs(order_item):
    order_item = order_item.reset_index().as_matrix()
    for order_id, order_object in tqdm(groupby(order_item, lambda x: x[0])):
        item_list = [item[1] for item in order_object]

        for item_pair in combinations(item_list, 2):
            yield item_pair


# In[24]:


def merge_item_stats(item_pairs, item_stats):
    return (item_pairs.merge(item_stats.rename(columns={'freq': 'freqA', 'support': 'supportA'}), left_on='item_A',
                             right_index=True).merge(
        item_stats.rename(columns={'freq': 'freqB', 'support': 'supportB'}), left_on='item_B', right_index=True))


# In[32]:


def merge_item_name(rules, item_name):
    columns = ['itemA', 'itemB', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']
    rules = (rules.merge(item_name.rename(columns={'item_name': 'itemA'}), left_on='item_A', right_on='item_id').merge(
        item_name.rename(columns={'item_name': 'itemB'}), left_on='item_B', right_on='item_id'))
    return rules[columns]


# In[35]:


def association_rules(order_item, min_support):
    print("Starting order item: {:22d}".format(len(order_item)))
    
    item_stats = freq(order_item).to_frame("freq")
    item_stats['support'] = item_stats['freq'] / order_count(order_item) * 100

    qualifying_items = item_stats[item_stats['support'] >= min_support].index
    order_item = order_item[order_item.isin(qualifying_items)]

    print("Items with support >= {}: {:15d}".format(min_support, len(qualifying_items)))
    print("Remaining order_item: {:21d}".format(len(order_item)))

    order_size = freq(order_item.index)
    qualifying_orders = order_size[order_size >= 2].index
    order_item = order_item[order_item.index.isin(qualifying_orders)]

    print("Remaining orders with 2+ items: {:11d}".format(len(qualifying_orders)))
    print("Remaining order_item: {:21d}".format(len(order_item)))

    item_stats = freq(order_item).to_frame("freq")
    item_stats['support'] = item_stats['freq'] / order_count(order_item) * 100

    item_pair_gen = get_item_pairs(order_item)

    item_pairs = freq(item_pair_gen).to_frame("freqAB")
    item_pairs['supportAB'] = item_pairs['freqAB'] / len(qualifying_orders) * 100

    print("Item pairs: {:31d}".format(len(item_pairs)))

    item_pairs = item_pairs[item_pairs['supportAB'] >= min_support]

    print("Item pairs with support >= {} : {:10d}\n".format(min_support, len(item_pairs)))

    item_pairs = item_pairs.reset_index().rename(columns={'level_0': 'item_A', 'level_1': 'item_B'})
    item_pairs = merge_item_stats(item_pairs, item_stats)

    item_pairs['confidenceAtoB'] = item_pairs['supportAB'] / item_pairs['supportA']
    item_pairs['confidenceBtoA'] = item_pairs['supportAB'] / item_pairs['supportB']
    item_pairs['lift'] = item_pairs['supportAB'] / (item_pairs['supportA'] * item_pairs['supportB'])

    return item_pairs.sort_values('lift', ascending=False)


# In[36]:


rules = association_rules(all_final_df, 0.01)
rules_hid = association_rules(hid_final_df, 0.01)
rules_men = association_rules(men_final_df, 0.01)
rules_mtr = association_rules(mtr_final_df, 0.01)
rules_phy = association_rules(phy_final_df, 0.01)
rules_tec = association_rules(tec_final_df, 0.01)


# In[38]:


rules['key'] = rules['item_A'] + rules['item_B']
rules_hid['key'] = rules['item_A'] + rules['item_B']
rules_men['key'] = rules['item_A'] + rules['item_B']
rules_mtr['key'] = rules['item_A'] + rules['item_B']
rules_phy['key'] = rules['item_A'] + rules['item_B']
rules_tec['key'] = rules['item_A'] + rules['item_B']


# In[43]:


rules = rules[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]
rules_hid = rules_hid[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]
rules_men = rules_men[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]
rules_mtr = rules_mtr[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]
rules_phy = rules_phy[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]
rules_tec = rules_tec[['key', 'item_A', 'item_B', 'freqAB', 'supportAB', 'freqA', 'supportA', 'freqB', 'supportB', 'confidenceAtoB',
               'confidenceBtoA', 'lift']]


# In[44]:


display(rules)
display(rules_hid)
display(rules_men)
display(rules_mtr)
display(rules_phy)
display(rules_tec)


# In[ ]:


rules.to_csv("rules_temp.csv")


# In[ ]:


rules


# In[ ]:




