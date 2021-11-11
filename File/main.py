import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.111", 13000))

while True:
    s.listen(20)
    c, addr = s.accept()
    text = input("What to send:")
    c.send(text.encode('utf-8'))