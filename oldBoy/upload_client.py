import socket
import os

sk = socket.socket()

address =('127.0.0.1',8000)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>>') #   post|123.jpg


    cmd,path = inp.split('|')

    path = os.path.join(BASE_DIR,path)
    filename = os.path.basename(path)
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s' % (filename,file_size)
    sk.sendall(bytes(file_info,'utf8'))
    with open(path,'rb') as f:
        has_send = 0
        while has_send != file_size:
            data = f.read(1024)
            sk.sendall(data)
            has_send += len(data)
        f.close()
        print('upload finished.')

sk.close()