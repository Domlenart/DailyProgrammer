from collections import namedtuple
from concurrent import futures

import tkinter as tk
from tkinter import ttk

from app import file_check

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tasks = namedtuple('Task', ['id', 'difficulty', 'solved', 'tested'])
        self.resizable(False, False)

        self.tree = ttk.Treeview(self)
        self.tree.configure(columns=['title', 'diff'])
        self.tree.heading('#0', text='#', anchor=tk.CENTER)
        self.tree.column('#0', width=60, anchor=tk.CENTER)
        self.tree.heading('title', text='Title', anchor=tk.CENTER)
        self.tree.column('title', anchor=tk.W)
        self.tree.heading('diff', text='Difficulty')
        self.tree.grid()

        for challenge in file_check.get_challenge_status():
            self.tree.insert('', 0, text=challenge.id, values=[challenge.difficulty])




if __name__=='__main__':
    MainWindow().mainloop()