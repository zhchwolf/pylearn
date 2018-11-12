#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql

pyconnection = pymysql.connect(host='172.19.50.150',port = 3306,user='root',password='root',db='baite',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
pycursor = pyconnection.cursor()

# 创建sql 语句，并执行
#sql = "INSERT INTO `users` (`email`, `password`) VALUES ('huzhiheng@itest.info', '123456')"
#pycursor.execute(sql)
# 提交SQL
#pyconnection.commit()

sql1= """SELECT ww_meeting.id,ww_meeting.title,ww_meeting.`type`,ww_meeting.create_time,ww_meeting.start_time,
ww_meeting.end_time,ww_meeting.content,ww_meeting.web_url,ww_meeting.address,ww_meeting.speaker_name,
ww_meeting.speaker_introduction,ww_meeting.speaker_img,ww_meeting.or_code,ww_meeting.survey_url,
ww_meeting.state,ww_meeting.del_flag,ww_meeting.signin_start_time,ww_meeting.survey_start_time,ww_meeting.public_time,
ww_meeting.speaker_sex,ww_meeting.`no`,ww_meeting.survey_end_time,ww_meeting.signin_end_time,ww_meeting.wx_sub,
ww_meeting.can_share,ww_meeting.can_enlist,ww_meeting.can_add_scene,ww_meeting.remark,ww_meeting.province,
ww_meeting.city,ww_meeting.img_resources,ww_meeting.enlist_end_time,ww_meeting.content_table,ww_meeting.content_foot,
ww_meeting.is_card,ww_meeting.bg_img,ww_meeting.is_import,ww_meeting.create_hcp_id,
ww_meeting.egrant_user_account,ww_meeting.sfdc_user_account,ww_meeting.import_meeting_no,ww_meeting.veeva_user_account
FROM ww_meeting where id= '00250afe46ba4b488eaaed2074768312' """

pycursor.execute(sql1)
result1=pycursor.fetchone()
print(result1)
print("-----------华丽分割线------------")

sql = """SELECT ww_meeting.id,ww_meeting.title,ww_meeting.`type`,ww_meeting.create_time,ww_meeting.start_time,
ww_meeting.end_time,ww_meeting.content,ww_meeting.web_url,ww_meeting.address,ww_meeting.speaker_name,
ww_meeting.speaker_introduction,ww_meeting.speaker_img,ww_meeting.or_code,ww_meeting.survey_url,
ww_meeting.state,ww_meeting.del_flag,ww_meeting.signin_start_time,ww_meeting.survey_start_time,ww_meeting.public_time,
ww_meeting.speaker_sex,ww_meeting.`no`,ww_meeting.survey_end_time,ww_meeting.signin_end_time,ww_meeting.wx_sub,
ww_meeting.can_share,ww_meeting.can_enlist,ww_meeting.can_add_scene,ww_meeting.remark,ww_meeting.province,
ww_meeting.city,ww_meeting.img_resources,ww_meeting.enlist_end_time,ww_meeting.content_table,ww_meeting.content_foot,
ww_meeting.is_card,ww_meeting.bg_img,ww_meeting.is_import,ww_meeting.create_hcp_id,
ww_meeting.egrant_user_account,ww_meeting.sfdc_user_account,ww_meeting.import_meeting_no,ww_meeting.veeva_user_account
FROM
ww_meeting"""
pycursor.execute(sql)
result = pycursor.fetchall()
for data in result:
    print(data)
pyconnection.close()