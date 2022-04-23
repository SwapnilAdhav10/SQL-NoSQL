import psycopg2
conn = psycopg2.connect(database="dbda_2022", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5433")
cur = conn.cursor()
cur.callproc('get_company', [3, ])
print("fechting Employee details who pushed changes to the production from function")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
print ("Operation done successfully");
conn.close()

