from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QGridLayout, QTextBrowser, QTreeView
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # self.showMaximized()
        grid = QGridLayout()

        self.tasks_view = QTreeView()
        self.task_model = self.create_tasks_model(self)
        self.tasks_view.setModel(self.task_model)

        grid.addWidget(self.tasks_view)

        self.update_tasks_button = QPushButton('Update data')
        self.update_tasks_button.clicked.connect(lambda: self.add_task())
        grid.addWidget(self.update_tasks_button)

        self.remove_task_button = QPushButton('Delete data')
        self.remove_task_button.clicked.connect(lambda: self.delete_task())
        grid.addWidget(self.remove_task_button)

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

    def delete_task(self, task_index='test2', title='test', solved=False, tested=True):
        self.task_model.removeRow(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    sys.exit(app.exec_())