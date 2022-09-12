from tkinter import *
from settings import *
import commands

#Sudoku Game Class
#By Timuruch
#timuruch.github.io/Python/sudoku/
#Version: Alpha 1.0

class Game:
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
    
    def draw_interface(self):
        commands.set_vars(self.canvas, self.tk)
        self.start_btn = Button(self.tk, text="Start",  bd=1, width=5, bg="white")
        self.start_btn.place(x=WIDTH-50, y=10)
        self.start_btn.bind("<Enter>", commands.start_enter)
        self.start_btn.bind("<Leave>", commands.leave)

        self.pause_btn = Button(self.tk, text="Pause",  bd=1, width=5, bg="white")
        self.pause_btn.place(x=WIDTH-50, y=40)
        self.pause_btn.bind("<Enter>", commands.pause_enter)
        self.pause_btn.bind("<Leave>", commands.leave)

        self.load_btn = Button(self.tk, text="Load",  bd=1, width=5, bg="white", command=commands.load)
        self.load_btn.place(x=WIDTH-50, y=70)
        self.load_btn.bind("<Enter>", commands.load_enter)
        self.load_btn.bind("<Leave>", commands.leave)

        self.save_btn = Button(self.tk, text="Save",  bd=1, width=5, bg="white")
        self.save_btn.place(x=WIDTH-50, y=100)
        self.save_btn.bind("<Enter>", commands.save_enter)
        self.save_btn.bind("<Leave>", commands.leave)

        self.test_btn = Button(self.tk, text="Test",  bd=1, width=5, bg="white", command=commands.test)
        self.test_btn.place(x=WIDTH-50, y=130)
        self.test_btn.bind("<Enter>", commands.test_enter)
        self.test_btn.bind("<Leave>", commands.leave)    

        self.solve_btn = Button(self.tk, text="Solve",  bd=1, width=5, bg="white")
        self.solve_btn.place(x=WIDTH-50, y=160)
        self.solve_btn.bind("<Enter>", commands.solve_enter)
        self.solve_btn.bind("<Leave>", commands.leave)
    
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
            
                