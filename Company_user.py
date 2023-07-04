import mysql.connector as dbconn
conn=dbconn.connect(host='localhost',user='root',password='', database='company_user')
if conn.is_connected()==False:
    print("database connection failed ....")
    exit()
db_cursor=conn.cursor()
def userDetails(companyID):
    db_cursor.execute("select * from user where companyId={}".format(companyID))
    return db_cursor.fetchall()
db_cursor.execute("select companyId from company")
company_id=db_cursor.fetchall()
users=userDetails(company_id[0][0])
print(users)
conn.close()
