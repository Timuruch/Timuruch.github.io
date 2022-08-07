from tkinter import *
from game import *
from settings import *

tk = Tk()
tk.title(TITLE)
tk.resizable(0, 0)

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=BG)
canvas.pack()

g = Game(tk, canvas)
g.draw_table()
g.draw_interface()

tk.mainloop()