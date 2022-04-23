#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


import pymongo


# In[3]:


myclient = pymongo.MongoClient("mongodb://localhost:27017")


# In[5]:


mydb= myclient["dbda_2022"]


# In[6]:


print(myclient.list_database_names())


# In[7]:


mycol = mydb["customers"]


# In[8]:


mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)


# In[9]:


x


# In[13]:


y=mycol.find_one()


# In[12]:


y


# In[14]:


for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)


# In[24]:


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
z = mycol.insert_many(mylist)


# In[31]:


for z in mycol.find({},{"_id":0, "name": 1, "address": 1 }):
    print(z)


# In[32]:


for z in mycol.find({},{"_id":0, "name": 0, "address": 1 }):
    print(z)
## we cannot field : 0 except primary key
## If dont  want specific field dont mention that field


# In[33]:


for z in mycol.find({},{"_id":0, "address": 1 }):
    print(z)


# In[ ]:




