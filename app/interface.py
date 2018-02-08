import sys

from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QGridLayout, QTextBrowser, QTreeView
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel
from PyQt5.QtGui import QStandardItemModel

import scrape_reddit_posts

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # self.showMaximized()
        grid = QGridLayout()

        self.tasks_view = QTreeView()
        self.task_model = self.create_tasks_model(self)
        self.selection_model = QItemSelectionModel(self.task_model)
        self.tasks_view.setModel(self.task_model)
        self.tasks_view.setSelectionModel(self.selection_model)

        grid.addWidget(self.tasks_view)

        self.update_tasks_button = QPushButton('Update data')
        self.update_tasks_button.clicked.connect(lambda: self.update_tasks())
        grid.addWidget(self.update_tasks_button)

        self.remove_task_button = QPushButton('Delete data')
        self.remove_task_button.clicked.connect(lambda: self.delete_task())
        grid.addWidget(self.remove_task_button)

        self.tasks_view.setSortingEnabled(True)

        self.setLayout(grid)
        self.show()

    def create_tasks_model(self, parent):
        model = QStandardItemModel(0, 3, parent)
        model.setHorizontalHeaderLabels(['#', 'Title', 'Solved', 'Tested'])
        return model

    def add_task(self, task_index='test2', title='test', solved=False, tested=True):
        self.task_model.insertRow(0)
        self.task_model.setData(self.task_model.index(0, 0), task_index)
        self.task_model.setData(self.task_model.index(0, 1), title)
        self.task_model.setData(self.task_model.index(0, 2), solved)
        self.task_model.setData(self.task_model.index(0, 3), tested)

    def update_tasks(self):
        for challenge_type, challenge_number in scrape_reddit_posts.find_new_challenges():
            self.task_model.insertRow(0)
            self.task_model.setData(self.task_model.index(0, 0), challenge_number)
            self.task_model.setData(self.task_model.index(0, 1), challenge_type)
            self.task_model.setData(self.task_model.index(0, 2), False)
            self.task_model.setData(self.task_model.index(0, 3), False)

    def delete_task(self):
        for selection in self.tasks_view.selectionModel().selectedRows():
            print(selection.row())
            self.task_model.removeRow(selection.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    sys.exit(app.exec_())
