#!/usr/bin/env python3
# -*- coding:utf8 -*-

import sys
import email
import cx_Oracle

user=''
pw=''
dbName=''

# def send_mail():


def test_db_stauts(user,pw,dbName):
    ns_conn = cx_Oracle.connect(user, pw, dbName)
    ns_cursor = ns_conn.cursor()
    #sqa_sql= 'select * from DM1_DM_BATCH_JOB'
    sqa_sql= 'select * from dual'
    ns_cursor.execute(sqa_sql)
    #rs=ns_cursor.fetchall()
    while 1:
        rs = ns_cursor.fetchone()
        if rs == None:break
        #print(rs)
        if 'X' in rs:
            print(user,' on ',dbName,' db connection is OK.')
    ns_cursor.close()

dns_list =[
('sdm_read','n00#sh!23','SDM'),
('spd_read','n00#sh!23','ODA2'),
('spd_read','n00#sh!23','AWSODA'),
('dvf_app','dvf','DVF_NEW'),
('dvf_datamart','dvf','DVF_NEW'),
('sdm_app','scdeu','SCDEU'),
('sdm_datamart','scdeu','SCDEU'),
('spd_app','sqa','SQA2'),
('spd_datamart','sqa','SQA2'),
('spd_cdm','sqa','SQA2'),
('spd_dfs','sqa','SQA2'),
('spd_ergo','sqa','SQA2'),
('spd_app','sqa','SQA'),
('spd_datamart','sqa','SQA'),
('spd_cdm','sqa','SQA'),
('spd_dfs','sqa','SQA'),
#('sqa_victor','victor','SQA'),
('spd_ergo','sqa','SQA'),
('spd_app','scd','SCD'),
('spd_datamart','scd','SCD'),
('spd_cdm','scd','SCD'),
('spd_dfs','scd','SCD'),
('spd_ergo','scd','SCD')
]

#test_db_stauts('spd_ergo','sqa','SQA')
for dns_one in dns_list:
    print(dns_one)
    try:
        test_db_stauts(*dns_one)
    except:
        error_msg = dns_one[0]+' on '+dns_one[2]+' can not connect. '
        #+ list(sys.exc_info())[0]
        print(error_msg)



