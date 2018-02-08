import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        label = tk.Label(self, text='Hello', padx=50, pady=50)
        label.pack()

if __name__ == '__main__':
    MainWindow().mainloop()