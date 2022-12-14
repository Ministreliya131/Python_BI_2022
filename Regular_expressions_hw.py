#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import re
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


os.chdir("/home/ministreliya/IB/")
os.listdir()
#os.mkdir("regexp")
os.chdir("/home/ministreliya/IB/regexp/")
os.listdir()


# TASK 1

# In[10]:


get_ipython().system('wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references')


# In[30]:


get_ipython().system('head -n 3 references')


# In[3]:


with open('references') as ref:
    whole = ref.read()

ftp = re.findall(r'ftp\.[./#\w]*', whole)

with open('ftps', 'w') as ftps:
    for link in ftp:
        print(link, file=ftps, sep = '\n')


# TASK 2

# In[19]:


get_ipython().system('wget https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD')


# In[20]:


get_ipython().system('head 2430AD')


# In[4]:


with open('2430AD') as AD2430:
    text = AD2430.read()
    
print("All numbers in text: ", *re.findall(r'\d{1,}\S\d{1,}|\d{1,}', text))

print("Unique numbers in text: ", *set(re.findall(r'\d{1,}\S\d{1,}|\d{1,}', text)))


# TASK 3

# In[45]:


print(re.findall(r'\w*[aA]\w*', text))


# TASK 4 

# In[6]:


print(re.findall(r'[A-Z][\w\s]*!', text))


# TASK 5

# In[7]:


all_words = re.findall(r'[a-zA-Z]\w*', text)
print(f"I found {len(all_words)} words in text")

unique_words = list(set([x.lower() for x in all_words]))
print(f"I found {len(unique_words)} unique words in text")

len_words = [len(x) for x in unique_words]


# In[39]:


plt.figure(figsize=(10,8))
cm = plt.cm.get_cmap('RdYlBu_r')

n, bins, patches = plt.hist(len_words, 15, color='green')

col = (n-n.min())/(n.max()-n.min())
for c, p in zip(col, patches):
    plt.setp(p, 'facecolor', cm(c))
    
plt.title("Distribution of words' length" , size = 20)
plt.xlabel("Words' Length", size = 15)
plt.ylabel('Frequency', size = 15)

ticks = [(patch.get_x() + (patch.get_x() + patch.get_width()))/2 for patch in patches]

ticklabels = range(1, 16)

plt.xticks(ticks, ticklabels)

plt.show()


# TASK 6

# In[42]:


GLASN = 'АЕЁИОУЭЫЮЯаеёиоуэыюя'

def translator(my_str):
    for char in GLASN:
        my_str = re.sub(f'{char}', f'{char}К{char.upper()}', my_str)
    return my_str


# In[44]:


#i'm sorry, but not sorry...

letov = '''
Пластмассовый мир победил. 
Макет оказался сильней. 
Последний кораблик остыл. 
Последний фонарик устал, 
а в горле сопят комья воспоминаний... 
Оо- моя оборона!

'''
print(translator(letov))

