import psycopg2
conn = psycopg2.connect(database = "dbda_2022", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")
print ("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE db_student
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print ("Table created successfully")

conn.commit()
conn.close()

