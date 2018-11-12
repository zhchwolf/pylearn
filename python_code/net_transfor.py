# -*- coding: cp936 -*-
from socket import *
import struct


ADDR = ('127.0.0.1',8008)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')

recvSock = socket(AF_INET,SOCK_STREAM)

recvSock.bind(ADDR)

recvSock.listen(True)

print ("等待连接...")


conn,addr = recvSock.accept()


print ("客户端已连接—> ",addr)


fhead = conn.recv(FILEINFO_SIZE)


filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)


#print filename,temp1,filesize,temp2


print ("文件名:",str(filename,encoding="utf-8")),len(filename),type(filename)


print ("文件大小:",filesize,"字节")


filename = 'new_'+filename.strip("\00")


fp = open(filename,'wb')


restsize = filesize


print ("正在接收文件... ",)


while 1:


    if restsize > BUFSIZE:


        filedata = conn.recv(BUFSIZE)


    else:


        filedata = conn.recv(restsize)


    if not filedata: break


    fp.write(filedata)


    restsize = restsize-len(filedata)


    if restsize == 0:


     break


print ("接收文件完毕，正在断开连接...")


fp.close()


conn.close()


recvSock.close()


print ("连接已关闭...")

#发送端：


 # -*- coding: cp936 -*-

from socket import *

import os

import struct

ADDR = ('127.0.0.1',8008)

BUFSIZE = 1024

filename = "VS.txt"

filename = bytes(filename,encoding="utf-8")

FILEINFO_SIZE=struct.calcsize('128s32sI8s')

sendSock = socket(AF_INET,SOCK_STREAM)

sendSock.connect(ADDR)

fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)

sendSock.send(fhead)

fp = open(filename,'rb')

while 1:

    filedata = fp.read(BUFSIZE)

    if not filedata: break

    sendSock.send(filedata)

print ("文件传送完毕，正在断开连接...")

fp.close()

sendSock.close()

print ("连接已关闭...")
