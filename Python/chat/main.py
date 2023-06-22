from win10toast import ToastNotifier
from tkinter import *
import threading
import socket
import sys

class Network:
    def __init__(self):
        self.tk = Tk()
        self.tk.resizable(0, 0)
        self.tk.title("Chat")
        self.tk.geometry("500x500")
        self.nick = "User"
        self.run = False
        self.users = []
        self.list = []
        self.x = 10
        self.y = 40
        self.i = 0
        self.e = Entry(self.tk, width=45, font=("Arial", 13))
        self.e.place(x=10, y=465)
        self.b = Button(self.tk, text="Send", font=("Arial", 9), command=self.send)
        self.b.place(x=420, y=465)

    def connect(self, ip, port):
        self.ip = ip
        self.port = port 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.l = Label(self.tk, text=str(str(ip) + ":" + str(port)), font=("Arial", 20))
        self.l.place(x=10, y=10)
        self.run = True

    def notification(self, text):
        toast = ToastNotifier()
        toast.show_toast("You have a message", text, duration = 10, icon_path = "icon.ico", threaded = True)
    
    def send(self):
        text = self.e.get()
        self.e.delete(first=0, last=10000)
        if text == "e":
            self.run = False
            self.s.close()
            sys.exit()
        if self.run:
            text = str("[" + self.nick + "] " + text)
            self.s.sendall(text.encode())
    
    def check(self):
        while self.run:
            if self.i == 20:
                last = self.list[int(len(self.list))-1]
                for x in range(len(self.list) - 1):
                    self.list[x].destroy()
                self.i = 1
                self.y = 60
                self.list = []
                self.list.append(last)
                last.place(x=self.x, y=40)
    
    def client_show(self):
        while self.run:
            data = self.s.recv(1024)
            l = Label(self.tk, text=data.decode())
            l.place(x=self.x, y=self.y)
            self.y += 20
            self.i += 1
            self.list.append(l)
            if self.tk.state()=="iconic":
                threading.Thread(target=self.notification, args = (data.decode(), )).start()
    
    def create_server(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, port))
        self.s.listen()
        self.run = True
    
    def listener(self):
        while self.run:
            conn, addr = self.s.accept()
            self.users.append((conn, addr))

n = Network()
n.connect("127.0.0.1", 25000)
threading.Thread(target=n.client_show).start()
threading.Thread(target=n.check).start()

n.tk.mainloop()