import operator
import tkinter as tk
import webbrowser

from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


from app import file_tasks


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Daily Programmer')

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.make_and_configure_tree()
        self.get_challenges()
        self.add_buttons()
        self.add_combobox()
        self.add_textfield()

    def make_and_configure_tree(self):
        self.treeframe = tk.Frame()
        self.treeframe.grid(row=0, column=0, sticky=tk.N+tk.S)

        self.tree = ttk.Treeview(self.treeframe)
        self.treescroll = ttk.Scrollbar(self.treeframe, command=self.tree.yview)
        self.tree.pack(side='left', fill='y')
        self.treescroll.pack(side='right', fill='y')

        self.tree.configure(columns=['id', 'diff'], show='headings', yscrollcommand=self.treescroll.set)

        self.tree.heading('id', text='#', anchor=tk.CENTER, command=self.sort_by_id)
        self.tree.column('id', width=60, anchor=tk.CENTER)
        self.tree.heading('diff', text='Difficulty')

        self.tree.tag_configure('not_completed', background='yellow')
        self.tree.tag_configure('completed', background='green')

        self.tree.bind('<ButtonRelease-1>', self.display_challenge_text)
        self.tree.bind('<Double-Button-1>', self.open_reddit_thread)

    def add_combobox(self):
        self.start_var = tk.StringVar()
        self.start_var.set('Pick difficulty')
        self.combobox = ttk.Combobox(textvariable=self.start_var, values='easy intermediate difficult/hard weekly',
                                     state='readonly')
        self.combobox.bind('<<ComboboxSelected>>', self.display_diff)
        self.combobox.grid(row=1, column=0)

    def add_buttons(self):
        self.update_button = ttk.Button(text='Update', command=self.update_challenges)
        self.update_button.grid(row=2, column=0)

    def add_textfield(self):
        self.textvar = tk.StringVar()
        self.textvar.set('Pick a challenge to see its text here')
        self.textfield = ScrolledText(wrap=tk.WORD, state='normal')
        self.textfield.insert(tk.END, self.textvar.get())
        self.textfield.configure(state='disabled')
        self.textfield.grid(column=1, row=0, sticky=(tk.E, tk.W, tk.N, tk.S), rowspan=3)

    def get_challenges(self):
        for challenge in file_tasks.get_challenge_status():
            completion = 'not_completed'
            tested = 'not_tested'

            if challenge.completed:
                completion = 'completed'
            if challenge.tested:
                tested = 'tested'

            self.tree.insert('', 0, text='', values=[challenge.id, challenge.difficulty, challenge.text, challenge.link],
                             tags=(completion, tested))

    def update_challenges(self):
        self.tree.delete(*self.tree.get_children())
        self.get_challenges()
        self.sort_by_id()

    def sort_by_id(self):
        challenges = [[k, int(self.tree.set(k, 'id'))] for k in self.tree.get_children()]
        challenges = sorted(challenges, key=(operator.itemgetter(1)))
        for index, (challenge, _) in enumerate(challenges):
            self.tree.move(challenge, '', index)

    def display_diff(self, _):
        diff_map = {'easy': ['easy'],
                    'intermediate': ['intermediate'],
                    'difficult/hard': ['hard', 'difficult'],
                    'weekly': ['weekly']}
        diff_to_show = diff_map[self.combobox.get()]

        self.update_challenges()
        self.sort_by_id()
        challenges_to_delete = [k for k in self.tree.get_children()
                                if not any(diff in self.tree.set(k, 'diff') for diff in diff_to_show)]

        self.tree.delete(*challenges_to_delete)

    def display_challenge_text(self, _):
        self.textfield.configure(state='normal')
        self.textfield.delete('1.0', tk.END)
        self.textfield.insert('1.0', f'{self.tree.item(self.tree.selection())["values"][2]}')
        self.textfield.configure(state='disabled')

    def open_reddit_thread(self, _):
        webbrowser.open(self.tree.item(self.tree.selection())['values'][3])

if __name__ == '__main__':
    MainWindow().mainloop()
