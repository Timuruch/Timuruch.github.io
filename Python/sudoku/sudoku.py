from settings import *
from tkinter import *
import threading
import time

#Sudoku Sudoku Class
#By Timuruch
#timuruch.github.io/Python/sudoku/
#Version: Alpha 1.0


class Sudoku:
    def __init__(self, canvas, tk, sudoku):
        self.canvas = canvas
        self.tk = tk
        self.sudok = sudoku.copy()
        self.cop = sudoku.copy()
        self.images = [] 
        self.image_buffer = []
        self.buffer = []
        self.press_per_acess = False
        self.data = ()
        self.char = 0

    def keyevent(self, event):
        if self.press_per_acess:
            char = event.char
            try:
                int(char)
                col = self.data[0]
                row = self.data[1]
                l = self.sudok[row]
                place = (row * 9) + col
                text = self.buffer[place]
                self.canvas.itemconfig(text, text=char)
                p = self.cop[row]
                p = list(p)
                p[col] = char
                p = "".join(p)
                self.cop[row] = p
                self.press_per_acess = False
            except Exception as e:
                self.press_per_acess = False
                
        self.press_per_acess = False

    def click_tester(self, event):
        x = event.x
        y = event.y
        if x > 10 and x < 190:
            if y > 10 and y < 190:
                x -= 10
                y -= 10
                col = x // 20
                row = y // 20
                place = (row * 9) + col
                l = self.sudok[row]
                char = l[col]
                self.data = (col, row)
                if char == " ":
                    self.press_per_acess = True
                    self.canvas.bind_all("<KeyPress>", self.keyevent)
        #When you click on character and press number it changes (space) on number

    def draw_table(self):
        x = START_X
        y = START_Y
        STARTX = x
        STARTY = y
        for i in range(3):
            for c in range(3):
                for ci in range(3):
                    for ii in range(3):
                        self.canvas.create_rectangle(x, y, x+SIZE, y+SIZE, width=2)
                        x += SIZE
                    y += SIZE
                    x = STARTX
                y = STARTY
                x += SIZE * 3
                STARTX = x
            x = START_X
            STARTX = x
            y += SIZE * 3
            STARTY = y
        
        x = START_X
        y = START_Y
        for i in range(3):
            for c in range(3):
                self.canvas.create_rectangle(x, y, x+RED_SIZE, y+RED_SIZE, width=3, outline="red")
                x += RED_SIZE
            x = START_X
            y += RED_SIZE

    def draw_sudoku(self):
        for x in self.buffer:
            x.destroy()
        self.canvas.delete("all")
        self.draw_table()
        x = START_X + (SIZE // 2)
        y = START_Y + (SIZE // 2)
        for line in self.sudok:
            for char in line:
                self.buffer.append(self.canvas.create_text(x, y, text=char, font=("Verdana", 9)))
                self.canvas.bind_all("<Button-1>", self.click_tester)
                x += SIZE
            x = START_X + (SIZE // 2)
            y += SIZE

    def test_sudoku(self):
        memory = []
        r_line = ""
        index = 0
        for j in self.cop:
            for c in j:
                for x in memory:
                    if x == c:
                        r_line += "!"
                        break
                else:
                    r_line += "."
                    memory.append(c)

            memory = []
            for y in range(len(r_line)):
                val = r_line[y]
                if val == "!":
                    place = (index*9) + y
                    text = self.buffer[place]
                    self.canvas.itemconfig(text, fill="red")
                else:
                    place = (index*9) + y
                    text = self.buffer[place]
                    self.canvas.itemconfig(text, fill="black")
            index += 1
            r_line = ""
            

        memory = []
        r_line = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        for v in range(len(self.cop)):           
            for i in range(len(self.cop)):
                l = self.sudok[i]
                c = l[v]
                for x in memory:
                    if x == c:
                        r_line[i] += "!"
                        break
                else:
                    r_line[i] += "."
                    memory.append(c)
            memory = []
        #self.canvas.create_rectangle(x, y, x+RED_SIZE, y+RED_SIZE, width=3, outline="red")
        
