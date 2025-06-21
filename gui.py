import tkinter as tk


class window(tk.Tk):

    def __init__(self, title, width, height):
        super().__init__()
        self.title(title)
        self.minsize(width=width, height=height)
        self.maxsize(width=width, height=height)

    def add_label(self, text, x, y):
        label = tk.Label(self, text=text, wraplength=350)
        label.place(x=x, y=y)
    
    def add_button(self, text, x, y, command):
        button = tk.Button(self, text=text, command=command)
        button.place(x=x, y=y)
        return button
    
    def add_text_input(self):
        entry = tk.Entry(self, width=16)
        entry.place(x=85, y=53)
        return entry

    def close_window(self):
        self.destroy()

