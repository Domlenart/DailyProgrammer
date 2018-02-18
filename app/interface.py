import operator
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from app import file_tasks


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.make_and_configure_tree()
        self.get_challenges()
        self.add_buttons()
        self.add_combobox()
        self.add_textfield()

    def make_and_configure_tree(self):
        self.tree = ttk.Treeview(self)
        self.tree.configure(columns=['id', 'diff'], show='headings')
        self.tree.heading('id', text='#', anchor=tk.CENTER, command=self.sort_by_id)
        self.tree.column('id', width=60, anchor=tk.CENTER)
        self.tree.heading('diff', text='Difficulty')
        self.tree.tag_configure('not_completed', background='yellow')
        self.tree.tag_configure('completed', background='green')
        self.tree.bind('<ButtonRelease-1>', self.display_challenge_text)
        self.tree.grid(sticky=tk.N+tk.S)

    def add_combobox(self):
        self.combobox = ttk.Combobox(values='easy intermediate difficult/hard weekly')
        self.combobox.bind('<<ComboboxSelected>>', self.display_diff)
        self.combobox.grid()

    def add_buttons(self):
        self.complete_button = ttk.Button(text='Complete', command=self.complete_challenge).grid()
        self.update_button = ttk.Button(text='Update', command=self.update_challenges).grid()

    def add_textfield(self):
        self.textvar = tk.StringVar(value='Challenge text will appear here')
        self.textfield = ScrolledText(wrap=tk.WORD, state='normal')
        self.textfield.insert(tk.END, 'Challenge text will display here')
        self.textfield.configure(state='disabled')
        self.textfield.grid(column=1, row=0)

    def get_challenges(self):
        for challenge in file_tasks.get_challenge_status():
            completion = 'not_completed'
            tested = 'not_tested'

            if challenge.completed:
                completion = 'completed'
            if challenge.tested:
                tested = 'tested'

            self.tree.insert('', 0, text='', values=[challenge.id, challenge.difficulty, challenge.text], tags=(completion, tested))

    def complete_challenge(self):
        print(self.tree.item(self.tree.focus(), tags=('completed', 'tested')))

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


if __name__ == '__main__':
    MainWindow().mainloop()
