from tkinter import *

tk = Tk()
tk.title("Monopoly online!")
tk.resizable(0, 0)
c = Canvas(tk, width=(11*50)+20, height=(11*50)+20, bg="white")
c.pack()
c.focus_set()

c.create_rectangle(10, 10, 560, 560, width=3)
c.create_rectangle(60, 60, 510, 510, width=3)
c.create_rectangle(10, 10, 60, 60, width=3)
c.create_rectangle(510, 10, 560, 60, width=3)
c.create_rectangle(10, 510, 60, 560, width=3)
c.create_rectangle(510, 510, 560, 560, width=3)

x = 60
y = 10

for i in range(9):
    c.create_rectangle(x, y, x+50, y+50, width=3)
    x += 50

x = 510
y = 60

for i in range(9):
    c.create_rectangle(x, y, x+50, y+50, width=3)
    y += 50

x = 10
y = 60

for i in range(9):
    c.create_rectangle(x, y, x+50, y+50, width=3)
    y += 50

x = 10
y = 510

for i in range(9):
    c.create_rectangle(x, y, x+50, y+50, width=3)
    x += 50

#the end of the drawing
#hahahahhaha i'm joking 

#color_lists
color_list = ["brown", "white", "brown", "white", "white", "pink", "pink", "pink"]

x = 60
y = 60

for i in range(0, 9):
    color = color_list[i]
    c.create_rectangle(x, y, x+50, y+10, fill=color, width=3)
    x += 50
    
x = 500
y = 60

for i in range(9):
    c.create_rectangle(x, y, x+10, y+50, fill="yellow", width=3)
    y += 50

x = 60
y = 500

for i in range(9):
    c.create_rectangle(x, y, x+50, y+10, fill="yellow", width=3)
    x += 50

x = 60
y = 60

for i in range(9):
    c.create_rectangle(x, y, x+10, y+50, fill="yellow", width=3)
    y += 50

tk.mainloop()