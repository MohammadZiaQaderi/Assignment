import mysql.connector as dbconn
from datetime import datetime
#put your values instead of localhost,username,password...
hostName='localhost'
username='root'
password=''
databaseName='company_user'
conn=dbconn.connect(host=hostName, user=username, password=password, database=databaseName)
if conn.is_connected()==False:
    print("database connection failed ....")
db_cursor=conn.cursor()
def orders_in_last7_days():
    x = datetime.today()
    x=x.timestamp()-7*24*60*60
    dt=datetime.fromtimestamp(x)
    dt2=str(dt.year)+'-'+str(dt.month)+'-'+str(dt.day)
    db_cursor.execute("select * from orders where createdAt>='{}'".format(dt2))
    
    return db_cursor.fetchall()
for order in orders_in_last7_days():
    print(order)   
