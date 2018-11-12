import socket

sk = socket.socket()

address =('127.0.0.1',8000)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.sendall(bytes(inp,'utf8'))
    server_reply = sk.recv(1024)
    print(str(server_reply, 'utf8'))





