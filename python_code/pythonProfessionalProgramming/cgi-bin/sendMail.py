#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate, parseaddr, formataddr
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from email import encoders

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8').encode(), addr)

def sendmail(subject,content):
    email_host = 'smtp.163.com'
    email_user = 'zhchwolf@163.com'
    email_pwd = '1q2w3e4r'
    maillist = '71902675@qq.com'
    me = email_user
    # msg = MIMEText(content,'plain','utf-8')
    msg = MIMEText('<html><body><h1>Hello</h1><p>send by <a herf="http://www.python.org">Python</a>...</p></body></html>', 'html', 'utf-8')
    msg['Subject'] = Header('mail by Python.','utf-8').encode()
    msg['From'] = me
    msg['To'] = maillist
    server = smtplib.SMTP(email_host)
    server.set_debuglevel(1)
    server.login(email_user, email_pwd)
    server.sendmail(me,maillist,msg.as_string())
    server.quit()

sendmail('Html mail by Python','Just test!')
# from_addr = input('from:')
# password = input('password:')
# to_addr = input('to:')
# smtp_server = input('SMTP server:')


