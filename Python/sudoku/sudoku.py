from settings import *
from tkinter import *

class Sudoku:
    def __init__(self, canvas, tk, sudoku):
        self.canvas = canvas
        self.tk = tk
        self.sudoku = sudoku
        self.buffer = []
    
    def test_sudoku(self):
        memory = []
        r_line = ""
        print("Row test.")
        for l in self.sudoku:
            for c in l:
                for x in memory:
                    if x == c:
                        r_line += "!"
                        break
                else:
                    r_line += "."
                    memory.append(c)

            memory = []
            print(r_line)
            r_line = ""
        print("")

        print("Column test.")
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
        for v in range(len(self.sudoku)):           
            for i in range(len(self.sudoku)):
                l = self.sudoku[i]
                c = l[v]
                for x in memory:
                    if x == c:
                        r_line[i] += "!"
                        break
                else:
                    r_line[i] += "."
                    memory.append(c)
            memory = []
        
        for x in r_line:
            print(x)

    def draw_sudoku(self):
        for x in self.buffer:
            self.canvas.delete(x)
        self.buffer = []
        x = START_X + (SIZE // 2)
        y = START_Y + (SIZE // 2)
        for line in self.sudoku:
            for char in line:
                self.buffer.append(self.canvas.create_text(x, y, text=char, font=("Verdana", 9)))
                x += SIZE
            x = START_X + (SIZE // 2)
            y += SIZE