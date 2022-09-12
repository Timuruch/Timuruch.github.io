from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from sudoku import *
from settings import *
import json

canvas = 0
tk = 0
s = 0

def set_vars(c, t):
    global canvas, tk, label
    canvas = c
    tk = t
    label = Label(tk, text="", bd=1, relief=SUNKEN, anchor=E)
    label.pack(fill=X, side=BOTTOM, ipady=2)

def start_enter(e):
    label["text"] = "Press to start"

def pause_enter(e):
    label["text"] = "Press to pause"

def load_enter(e):
    label["text"] = "Press to load your sudoku"

def load():
    global s
    sudoku_file = filedialog.askopenfilename(initialdir='/', title='Open file', 
        filetypes=(('SUDOKU file', '*.SUDOKU'), ('All files', '*.*')))
    if not sudoku_file:
        messagebox.showinfo('Error', 'You must to choose file!')
    else:
        sudoku = json.load(open(sudoku_file))
        s = Sudoku(canvas, tk, sudoku)
        s.draw_sudoku()

def save_enter(e):
    label["text"] = "Press to save your sudoku"

def test_enter(e):
    label["text"] = "Press to test your sudoku"

def test():
    try:
        s.test_sudoku()
    except:
        pass

def solve_enter(e):
    label["text"] = "Press to solve your sudoku"

def leave(e):
    label["text"] = ""