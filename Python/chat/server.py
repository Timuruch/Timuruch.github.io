import socket
import threading

IP = "127.0.0.1"
HOST = 25000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, HOST))
s.listen()

clients = []

def broadcast(message):
    global clients
    for client in clients:
        client.send(message)

def handle(client):
    global clients
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
            print(clients)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    global clients
    while True:
        client, address = s.accept()
        print("Connected with {}".format(str(address)))
        client.send('Connected to server!'.encode())
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()