import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")

print ("Opened database successfully")

cur = conn.cursor()


cur.execute("DELETE from COMPANY where ID=2;")
conn.commit()
print ("Total number of rows updated :", cur.rowcount)

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully");
conn.close()

