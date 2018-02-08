import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.make_label()

    def make_label(self):
        label = tk.Label(self, text='Hello').pack()


if __name__=='__main__':
    root = MainWindow()
    root.mainloop()