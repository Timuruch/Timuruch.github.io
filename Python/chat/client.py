import socket 
import threading
try:
    from win10toast import ToastNotifier
except:
    import pip
    pip.main(['install', 'win10toast'])
    #pip install pypiwin32
    from win10toast import ToastNotifier

IP = "127.0.0.1"
HOST = 25000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, HOST))
toast = ToastNotifier()

nick = input("Enter your nick: ")

def notification(text):
    toast = ToastNotifier()
    toast.show_toast("You have a message", text, duration = 10, icon_path = "icon.ico", threaded = True)

while True:
    text = input(":")
    if text == "e":
        break
    text = str("[" + nick + "] " + text)
    s.sendall(text.encode())
    data = s.recv(1024)
    print(data.decode())
    threading.Thread(target=notification, args = (data.decode(), )).start()