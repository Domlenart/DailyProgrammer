import tkinter as tk


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if tasks:
            self.tasks = tasks
        else:
            self.tasks = []

        self.title('TODO app v1')
        self.geometry('300x400')

        todol = tk.Label(self, text='--Add items here--', bg='lightgrey', fg='black', pady=10)
        self.tasks.append(todol)

        for task in self.tasks:
            task.pack(side='top', fill='x')

        self.task_create = tk.Text(self, height=3, bg='white', fg='black')
        self.task_create.pack(side=tk.BOTTOM, fill='x')
        self.task_create.focus_set()

        self.bind('<Return>', self.add_task)

        self.colour_schemes = [{'bg': 'lightgrey', 'fg': 'black'}, {'bg': 'grey', 'fg': 'white'}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, 'end').strip()

        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)

            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice['bg'])
            new_task.configure(fg=my_scheme_choice['fg'])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

if __name__ == '__main__':
    Todo().mainloop()
