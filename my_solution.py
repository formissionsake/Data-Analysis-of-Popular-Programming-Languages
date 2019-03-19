#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import matplotlib.pyplot as plt
import string


# In[194]:


dataframe = pd.read_json('tweets.json', lines=True)
dataframe.head()


# In[3]:


dataframe.shape[0]


# In[4]:


df1 = dataframe[['lang', 'text']]
df1.head()


# In[5]:


locations = []
for i in dataframe['user']:
    location = i['location']
    locations.append(location)
df2 = pd.DataFrame(locations, columns = ['location'])
df2.head()


# In[79]:


df = pd.concat([df1, df2], axis=1)
df.loc[2993]['text']


# In[7]:


df['lang'].unique()


# In[43]:


df['lang'].nunique()


# In[64]:


top_lang = df['lang'].value_counts()
top5_lang = dict(top_lang[:5])
top5_lang_hist = pd.DataFrame.from_dict(top5_lang, orient='index')
top5_lang_hist.plot(kind='bar')
plt.title("Top 5 languages")
plt.xlabel("Languages")
plt.ylabel("Number of tweets")


# In[129]:


top_location = df['location'].value_counts()
top5_location = dict(top_location[:5])
print(top5_location)
top5_location_hist = pd.DataFrame.from_dict(top5_location, orient='index')
top5_location_hist.plot(kind='bar')
plt.title('Top 5 locations')
plt.xlabel('Locations')
plt.ylabel('Number of tweets')


# In[92]:


df_eng = df[df['lang'] == 'en']
df_eng.shape[0]


# In[141]:


keywords = ['tutorial', 'programming', 'software', 'linux', 
            'winidows', 'mac os', 'data', 'dictionary']
df_rel = df_eng[df_eng['text'].str.contains('|'.join(keywords))]


# In[165]:


df_rel.shape[0]
df_rel


# In[184]:


import re
keywords = ['python', 'java', 'c++', 'golang', 'php']
dicts = {}
for i in keywords:
    df3 = df_rel[df_rel['text'].str.contains(i, regex=False, case=False)]
    if df3.shape[0] != 0:
        file = open("{0}.txt".format(i), "w")
        for tweet in df3['text']:
            for word in tweet.split(' '):
                if word.startswith('http://') or word.startswith('https://'):
                    file.write(word)
            
    dicts[i] = df3.shape[0]    
print(dicts)
num_rel = pd.DataFrame.from_dict(dicts, orient='index')
num_rel.plot(kind='bar')
plt.title('Number of relevant tweets for each language')
plt.xlabel('Programming languages')
plt.ylabel('Number of relevant tweets')


# In[ ]:




