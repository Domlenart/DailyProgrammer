import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)

        self.tree = ttk.Treeview(self)
        self.tree.configure(columns=['title', 'diff'])
        self.tree.heading('#0', text='#', anchor=tk.CENTER)
        self.tree.column('#0', width=30, anchor=tk.CENTER)
        self.tree.heading('title', text='Title', anchor=tk.CENTER)
        self.tree.column('title', anchor=tk.W)
        self.tree.heading('diff', text='Difficulty')
        self.tree.grid()

        self.tree.insert('', 0, text='1', values=['one'])
        self.tree.insert('', 1, text='2', values=['one'])
        self.tree.insert('', 2, text='3', values=['one'])
        self.tree.insert('', 3, text='4', values=['one'])



if __name__=='__main__':
    MainWindow().mainloop()