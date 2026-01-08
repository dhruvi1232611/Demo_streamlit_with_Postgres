import psycopg2 as psy
#connection established
db_name='inventory '
db_user='postgres'
db_port=5432
db_pass='dhruvi@26'
db_host='localhost'
conn= psy.connect(database=db_name,user=db_user,password=db_pass,host=db_host,port=db_port)