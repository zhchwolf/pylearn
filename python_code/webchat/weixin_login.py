#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import itchat,time
from itchat.content import *
def lc():
    print("Finish login!")
def ec():
    print("exit")
itchat.auto_login(loginCallback=lc,exitCallback=ec)

@itchat.msg_register(TEXT, isFriendChat = True, isGroupChat= True, isMpChat= True)
def text_reply(msg):
    msg.user.send("%s : %s" % (msg.type, msg.text))

@itchat.msg_register(TEXT) #TEXT表示如果有人发送文本消息，就调用下面的方法。
def simple_reply(msg):
    itchat.send_msg('已经收到，内容是%s' % msg['Text'],toUserName=msg['FromUserName'])
    return "T reveived: %s" % msg["Text"]



time.sleep(5)
itchat.logout()


'''
itchat.send(msg = "Text Message", toUserName = None)
msg : 文本消息内容
@fil@path_to_file : 发送文件
@img@path_to_img : 发送图片
@vid@path_to_video : 发送视频
toUserName : 发送对象，如果留空，将发送给自己

itchat.send_msg("Hello world.")
itchat.send_file("E:\\Projects\\python\\webchat\\files\\test.text")
itchat.send_video("E:\\Projects\\python\\webchat\\files\\test.mp4")
itchat.send_image("E:\\Projects\\python\\webchat\\files\\test.png")

itchat.send("Hello world!")
itchat.send("@fil@%s" %  'E:\\Projects\\python\\webchat\\files\\test.text')
itchat.send("@img@%s" %  'E:\\Projects\\python\\webchat\\files\\test.png')
itchat.send("@vid@%s" %  'E:\\Projects\\python\\webchat\\files\\test.mp4')

'''


