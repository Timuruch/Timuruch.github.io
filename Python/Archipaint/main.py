from tkinter import *
from keybinds import *

tk = Tk()
tk.title("Arcipaint A.1.0")
tk.resizable(0, 0)
tk.attributes('-fullscreen',True)

width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()

c = Canvas(tk, width=width, height=height, bg="white")
c.pack()

ky = KeyBinds(tk, c, height)

tk.mainloop()