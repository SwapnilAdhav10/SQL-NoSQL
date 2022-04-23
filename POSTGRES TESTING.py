#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install psycopg2


# In[8]:



import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")
cur = conn.cursor()


# In[7]:



cur.execute('''CREATE TABLE COMPANY2
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print ("Table created successfully")

conn.commit()



# In[13]:


cur.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

cur.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");


# In[9]:


cur.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");


# In[14]:


conn.commit()


# In[15]:


cur.execute("select * from COMPANY2")


# In[16]:


rows = cur.fetchall()
for row in rows:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");


# In[17]:


conn.close()


# In[ ]:




