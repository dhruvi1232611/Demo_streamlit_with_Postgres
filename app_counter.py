import psycopg2 as psy
import mysqlx
db_name='inventory '
db_user='postgres'
db_port=5432
db_pass='dhruvi@26'
db_host='localhost'

conn= psy.connect(database=db_name,user=db_user,password=db_pass,host=db_host,port=db_port)

if(conn):
    print("Database connected successfully")
else:
    print("not connected!")


cur =conn.cursor()

cur.execute("select * from customer")
rows=cur.fetchall()
for data in rows:
    print("id:",data[0])
    print("Customer Name:",data[1])
    print("Customer city:",data[2])

conn.close()