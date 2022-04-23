#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install cassandra-driver


# In[7]:


import cassandra;


# In[8]:


from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'],port=9042)
session = cluster.connect('sarvesh')
session.execute('USE sarvesh')


# In[9]:


session.execute("create table student2(id int primary key,age int)")


# In[10]:


session.execute("insert into student2(id,age) values (2,24)")


# In[11]:


rows=session.execute('select * from student')
for row in rows:
    print(row.id,row.age)


# In[ ]:




