class KeyBinds:
    def __init__(self, tk, c, h):
        self.tk = tk
        self.c = c
        self.c.bind_all('<KeyPress-Escape>', self.keybinds)
        self.c.bind_all('<Motion>', self.mouse_keybinds)
        self.mouse_coord = self.c.create_text(30, h-10, text='0 | 0')
    
    def keybinds(self, event):
        if event.keysym == 'Escape':
            self.c.destroy()
    
    def mouse_keybinds(self, event):
        txt = str('%s | %s' % (event.x, event.y))
        self.c.itemconfig(self.mouse_coord, text=txt)
    
    