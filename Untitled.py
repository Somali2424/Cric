#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import necessary libraries
import pandas as pd
import json


# In[3]:


with open ('t20_wc_match_results.json') as f:
    data=json.load(f)


# In[4]:


data


# In[5]:


data[0]['matchSummary']


# In[6]:


df_match=pd.DataFrame(data[0]['matchSummary'])


# In[7]:


df_match.head()


# In[8]:


df_match.shape


# In[9]:


df_match.rename({'scorecard':'match_id'}, axis=1, inplace=True)


# In[10]:


df_match.head()


# In[34]:


match_ids_dict={}

for index,row in df_match.iterrows():
    key1=row['team1']+' Vs '+row['team2']
    key2=row['team2']+' Vs '+row['team1']
    
    match_ids_dict[key1]=row["match_id"]
    match_ids_dict[key2]=row["match_id"]
match_ids_dict


# In[55]:


df_match.to_csv('t20_wc_match_results.csv', index=False)


# **Batting Summary**

# In[13]:


with open('t20_wc_batting_summary.json') as f:
    data=json.load(f)
    all_rec=[]
    for rec in data:
        all_rec.extend(rec["battingSummary"])
df_batting=pd.DataFrame(all_rec)
df_batting.head()


# In[12]:


all_rec


# In[16]:


df_batting["out/not_out"]=df_batting.dismissal.apply(lambda x: "out" if len(x)>0 else "not out")


# In[17]:


df_batting


# In[18]:


df_batting.drop(columns=["dismissal"], inplace=True)


# In[29]:


df_batting.tail(60)


# In[32]:


df_batting['batsmanName']=df_batting['batsmanName'].apply(lambda x: x.replace('â€', ''))
df_batting['batsmanName'] =df_batting['batsmanName'].apply(lambda x: x.replace('\\xa0', ''))


# In[40]:


df_batting["match_id"]=df_batting['match'].map(match_ids_dict)


# In[41]:


df_batting.head()


# In[42]:


df_batting.to_csv('t20_wc_batting_summary.csv', index=False)


# In[45]:


with open('t20_wc_bowling_summary.json') as f:
    data=json.load(f)
    all_record=[]
    for record in data:
        all_record.extend(record["bowlingSummary"])
df_bowling=pd.DataFrame(all_record)
df_bowling.head()


# In[46]:


df_bowling['match_id']=df_bowling['match'].map(match_ids_dict)
df_bowling.head()


# In[47]:


df_bowling.to_csv('t20_wc_bowling_summary.csv', index=False)


# In[48]:


with open ('t20_wc_player_info.json') as f:
    data=json.load(f)


# In[49]:


df_players=pd.DataFrame(data)

print(df_players.shape)
df_players.head(10)


# In[50]:


df_players['name'] = df_players['name'].apply(lambda x: x.replace('Ã¢â‚¬', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('â€ ', ''))
df_players['name'] = df_players['name'].apply(lambda x: x.replace('\\xa0', ''))


# In[51]:


df_players.head(10)


# In[52]:


df_players[df_players['team']=='India']


# In[54]:


df_players.to_csv('t20_wc_player_info_no_images.csv',index=False)


# In[ ]:





# In[ ]:





# In[ ]:




