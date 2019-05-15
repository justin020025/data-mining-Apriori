#!/usr/bin/env python
# coding: utf-8

# In[67]:


import sys
import re
import numpy as np
from collections import Counter


# In[ ]:


arg = sys.argv
in_file, out_file, min_sup = arg[1], arg[2], arg[3]


# In[3]:


inp = []


# In[4]:


with open(in_file,'r',encoding = 'utf8') as Input:
    inp = Input.readlines()
Input.close()


# In[61]:


sentences = []
for line in inp:
    sentences.extend(re.split('[.,?]+',re.sub('[!@#$%^&*()\\n$:;]','',line)))


# In[63]:


sentences = [e.lower().split() for e in sentences]


# In[58]:


stop = []
with open('stop_words.txt','r',encoding = 'utf8') as s:
    stop = re.split('\n',s.read())
s.close()


# In[65]:


clean_sentences = []
for i in range(len(sentences)):
    if sentences[i] == []:
        continue
    temp = []
    for j in range(len(sentences[i])):
        if not (sentences[i][j] in stop):
            temp.append(sentences[i][j])
    if temp != []:        
        clean_sentences.append(temp)
    
    


# In[154]:


def is_sublist(lst1, lst2):
    return set(lst1).issubset(set(lst2))


# In[115]:


def new_itemset(table):
    itemset = [e[0] for e in table]
    Len = len(itemset[0])+1
    new_itemset_=[]
    for i in range(len(itemset)-1):
        for j in range(i+1,len(itemset)):
            temp = list(set(itemset[i]).union(set(itemset[j])))
            if len(temp) == Len:
                if not (temp in new_itemset_):
                    new_itemset_.append(temp)
        
    return new_itemset_


# In[123]:


def new_table(data, itemset):
    table = [[e,0] for e in itemset]
    for i in range(len(itemset)):
        for sentence in data:
            if is_sublist(itemset[i],sentence):
                table[i][1]+=1
    return table
    
    


# In[158]:


def apriori(data, min_sup_):
    #initialize the itemset
    import numpy as np
    itemset0  = set()
    for sentence in data:
        itemset0 = itemset0.union(np.unique(sentence))
    itemset0 = [[e] for e in itemset0]
    cur_itemset = itemset0
    
    itemset_maxlen = max([len(sentence) for sentence in data])
    
    result = []
    for i in range(itemset_maxlen-1):
        
        if len(cur_itemset)>1:
            #creat table
            cur_table = new_table(data, cur_itemset)
            
            #delete entry in table if support < min support
            clean_table = []
            for e in cur_table:
                if e[1]>=min_sup_:
                    clean_table.append(e)
            del cur_table
            cur_table = clean_table
            
            #push to result
            result.extend(cur_table)
    
            cur_itemset = new_itemset(cur_table)
    
    return result
            
                
    
    


# In[169]:


result = apriori(clean_sentences, int(min_sup))


# In[188]:


result


# In[202]:


result_sort = sorted([(sorted(row[0]),row[1]) for row in result], key = lambda x:x[0][0])


# In[207]:


with open(out_file,'w',encoding = 'utf8') as out:
    for e in result_sort:
        for word in e[0]:
            out.write(word+' ')
        out.write(str(e[1]))   
        out.write('\n')
out.close()    


# In[ ]:




