import tkinter as tk
from tkinter import ttk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.resizable(False, False)

        self.title('Feet to meters')
        self.mainframe = ttk.Frame(self, padding='3 3 12 12', relief="sunken")
        self.mainframe.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E+tk.S)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)


        self.feet = tk.StringVar()
        self.meters = tk.StringVar()

        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

        self.label = ttk.Label(self.mainframe, textvariable=self.meters)
        self.label.grid(column=1, row=2, sticky=(tk.W, tk.E))
        self.label.columnconfigure(1, weight=1)
        self.label.rowconfigure(2, weight=1)

        self.button = ttk.Button(self.mainframe, text='Calculate', command=self.calculate)
        self.button.grid(column=3, row=3, sticky=tk.E)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        ttk.Label(self.mainframe, text='feet').grid(column=2, row=1, sticky=tk.E)
        ttk.Label(self.mainframe, text='is equivalent to').grid(column=0, row=2, sticky=tk.E)
        ttk.Label(self.mainframe, text='meters').grid(column=2, row=2, sticky=tk.W)

        self.feet_entry.focus()
        self.bind('<Return>', self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set((0.3048 * value * 10000 + 0.5)/10000)
        except ValueError:
            pass


if __name__ == '__main__':
    Main().mainloop()