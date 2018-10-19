#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit,
                             QGridLayout, QApplication, QDesktopWidget,
                             QPushButton)
from PyQt5.QtGui import QIcon


class Example(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        label = QLabel('Enter a number:')
        self.input = QLineEdit()
        btn = QPushButton('Square')
        self.answer = QLabel('')

        btn.clicked.connect(self.btnClicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(label, 0, 0)
        grid.addWidget(self.input, 0, 1)
        grid.addWidget(btn, 0, 2)
        grid.addWidget(self.answer, 1, 1)

        self.setLayout(grid)
        self.center()
        self.setWindowTitle('GUI MWE')
        self.setWindowIcon(QIcon.fromTheme('face-cool'))
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def btnClicked(self):
        input = self.input.text()
        output = myfunc.myfunc(input)
        self.answer.setText('{} squared is {}'.format(input, output))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
sys.exit(app.exec_())
