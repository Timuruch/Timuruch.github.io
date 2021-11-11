import socket

s = socket.socket()
s.bind(("192.168.0.111", 13000))

while True:
    m = str(s.recv(1024)).decode('utf-8')
    print(m)