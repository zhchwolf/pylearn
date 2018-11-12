import socket

sk = socket.socket()

address =('127.0.0.1',8000)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp,'utf8'))
    result_len = int(str(sk.recv(1024),'utf'))
    print(result_len)
    sk.sendall(bytes('received ok','utf8')) #解决粘包问题
    data = bytes()
    while len(data) != result_len:
        server_reply = sk.recv(1024)
        data += server_reply

    print(str(data, 'gbk'))

sk.close()

