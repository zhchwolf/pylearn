import socket
import subprocess

sk = socket.socket()
address =('127.0.0.1',8000)

sk.bind(address)

sk.listen(3)
print('listen ......')

while 1:
    conn, addr = sk.accept()
    print(conn,addr)
    while 1:
        try:
            client_data = conn.recv(1024)
        except Exception as e:
            print(e)
            break
        print(str(client_data,'utf8'))
        if not client_data:break
        obj = subprocess.Popen(str(client_data,'utf8'),shell=True,stdout=subprocess.PIPE)
        print(obj)
        res_obj = obj.stdout.read()
        print(res_obj)
        obj_size = bytes(str(len(res_obj)),'utf8')
        conn.sendall(obj_size)
        conn.recv(1024)#解决粘包问题
        conn.sendall(res_obj)

sk.close()
