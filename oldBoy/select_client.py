# import time
# import socket
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# while True:
#     sk.connect(('127.0.0.1',6667))
#     print("hello")
#     sk.sendall(bytes("hello","utf8"))
#     time.sleep(2)
#     break

import socket

sk=socket.socket()

sk.connect(("127.0.0.1",9904))

while 1:
    inp=input(">>").strip()
    sk.send(inp.encode("utf8"))
    data=sk.recv(1024)
    print(data.decode("utf8"))