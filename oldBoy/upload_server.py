import socket
import os

sk = socket.socket()
address =('127.0.0.1',8000)

sk.bind(address)

sk.listen(3)
print('listen ......')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = sk.accept()
    print(conn,addr)
    while 1:
        data = conn.recv(1024)
        cmd,filename,filesize = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'upload',filename)
        filesize = int(filesize)
        print(filesize)
        with open(path,'ab') as f:
            has_receive = 0
            while has_receive != filesize:
                data = conn.recv(1024)
                f.write(data)
                has_receive += len(data)
                print(has_receive)
            print('received finished.')

sk.close()
