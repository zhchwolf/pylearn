#!/usr/bin/env python3
# -*- coding:utf8 -*-

import pymysql

conn = pymysql.connect(host='172.19.50.49',port=3306,user='root',passwd='root',db='lsgold',charset='utf8')
MysqlCursor = conn.cursor()
dblist = ' show databases '
MysqlCursor.execute(dblist)
dbdata = MysqlCursor.fetchall()
print(dbdata)
sql = 'select * from ls_bill; '
MysqlCursor.execute(sql)
alldata = MysqlCursor.fetchall()
print(alldata[0])

MysqlCursor.close()
