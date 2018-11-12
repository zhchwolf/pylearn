import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='biog',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 游标设置为字典类型
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# n = 2
# 获取最新自增ID
# new_id = cursor.lastrowid
# rows = cursor.execute("insert into c_person (p_name,p_last_name,p_gender) VALUES('张无忌', '张',1 )")
# rows = cursor.execute("delete from c_person where p_id = %s", (n,))
# rows = cursor.executemany("insert into c_person (p_name,p_last_name,p_gender) VALUES(%s,%s,%s)", [('谢逊', '谢',1 ),('宋玉', '宋',1 )])
# conn.commit()

cursor.execute("select * from c_person")
# row_1 = cursor.fetchone()
row_2 = cursor.fetchmany(3)
# row_3 = cursor.fetchall()
print(row_2)

cursor.close()
conn.close()

