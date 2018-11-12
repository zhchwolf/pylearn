import socket
import select

sk = socket.socket()
address =('127.0.0.1',8000)

sk.bind(address)
sk.listen(3)
inp = [sk,]
while 1:
    inputs,outputs,errors = select.select(inp,[],[],)
    for i in inputs:
        if i == sk:
            conn,addr = i.accept()
            print(conn)
            inp.append(conn)
        else:
            data = i.recv(1024)
            print(data.decode('utf8'))
            res = input('response %s>>>' % inp.index(i))
            i.sendall(res.encode('utf8'))

# conn,addr = sk.accept()
# while True:
#     client_data = conn.recv(1024)
#     print(str(client_data,'utf8'))
#     if not client_data:
#         conn.close()
#         conn,addr = sk.accept()
#         continue
#     inp = input('>>>')
#     conn.send(bytes(inp,'utf8'))

# while 1:
#     conn, addr = sk.accept()
#     print(conn,addr)
#     while 1:
#         try:
#             client_data = conn.recv(1024)
#         except Exception as e:
#             print(e)
#             break
#         print(str(client_data,'utf8'))
#         if not client_data:break
#         inp = input('>>>')
#         conn.send(bytes(inp,'utf8'))
#
#
# sk.close()
