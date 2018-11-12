import pymysql

#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
conn=pymysql.connect(host='172.19.50.49',user='root',passwd='root',db='hdjjq',port=3306,charset='utf8')
cur=conn.cursor()#获取一个游标
cur.execute('select * from ls_bill')
data=cur.fetchall()
for d in data :
    #注意int类型需要使用str函数转义
    #print("bill_id: "+str(d[0])+'    bill_name： '+d[1]+"    bill_code： "+d[2])
    print(d)
cur.close()#关闭游标
conn.close()#释放数据库资源

