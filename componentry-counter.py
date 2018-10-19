#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit,
                             QGridLayout, QApplication, QDesktopWidget,
                             QPushButton, QShortcut, qApp, QAction)
from PyQt5.QtGui import QIcon, QKeySequence


class Example(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.tb0 = QLineEdit('A')
        self.tb1 = QLineEdit('B')
        self.tb2 = QLineEdit('C')
        self.tb3 = QLineEdit('D')

        add0 = QPushButton('+1')
        add1 = QPushButton('+1')
        add2 = QPushButton('+1')
        add3 = QPushButton('+1')

        sub0 = QPushButton('-1')
        sub1 = QPushButton('-1')
        sub2 = QPushButton('-1')
        sub3 = QPushButton('-1')

        self.tot0 = QLabel('0')
        self.tot1 = QLabel('0')
        self.tot2 = QLabel('0')
        self.tot3 = QLabel('0')

        self.total = QLabel('0')

        add0.setShortcut('Ctrl+Alt+A')
        add1.setShortcut('Ctrl+Alt+S')
        add2.setShortcut('Ctrl+Alt+D')
        add3.setShortcut('Ctrl+Alt+F')

        add0.clicked.connect(self.add0_one)
        sub0.clicked.connect(self.sub0_one)
        add1.clicked.connect(self.add1_one)
        sub1.clicked.connect(self.sub1_one)
        add2.clicked.connect(self.add2_one)
        sub2.clicked.connect(self.sub2_one)
        add3.clicked.connect(self.add3_one)
        sub3.clicked.connect(self.sub3_one)

        # label = QLabel('Enter a number:')
        # self.input = QLineEdit()
        # btn = QPushButton('Square')
        # self.answer = QLabel('')

        # btn.clicked.connect(self.btnClicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.tb0, 0, 0)
        grid.addWidget(self.tb1, 0, 1)
        grid.addWidget(self.tb2, 0, 2)
        grid.addWidget(self.tb3, 0, 3)

        grid.addWidget(add0, 1, 0)
        grid.addWidget(add1, 1, 1)
        grid.addWidget(add2, 1, 2)
        grid.addWidget(add3, 1, 3)

        grid.addWidget(sub0, 2, 0)
        grid.addWidget(sub1, 2, 1)
        grid.addWidget(sub2, 2, 2)
        grid.addWidget(sub3, 2, 3)

        grid.addWidget(self.tot0, 3, 0)
        grid.addWidget(self.tot1, 3, 1)
        grid.addWidget(self.tot2, 3, 2)
        grid.addWidget(self.tot3, 3, 3)

        grid.addWidget(self.total, 4, 0)

        self.setLayout(grid)
        self.center()
        self.setWindowTitle('Component Counter')
        self.setWindowIcon(QIcon.fromTheme('face-cool'))
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def update_total(self):
        t0 = int(self.tot0.text())
        t1 = int(self.tot1.text())
        t2 = int(self.tot2.text())
        t3 = int(self.tot3.text())
        total = str(t0 + t1 + t2 + t3)
        self.total.setText(total)


    def add0_one(self):
        input = self.tot0.text()
        output = str(int(input) + 1)
        self.tot0.setText(output)
        self.update_total()


    def sub0_one(self):
        input = self.tot0.text()
        output = str(int(input) - 1)
        self.tot0.setText(output)
        self.update_total()


    def add1_one(self):
        input = self.tot1.text()
        output = str(int(input) + 1)
        self.tot1.setText(output)
        self.update_total()


    def sub1_one(self):
        input = self.tot1.text()
        output = str(int(input) - 1)
        self.tot1.setText(output)
        self.update_total()


    def add2_one(self):
        input = self.tot2.text()
        output = str(int(input) + 1)
        self.tot2.setText(output)
        self.update_total()


    def sub2_one(self):
        input = self.tot2.text()
        output = str(int(input) - 1)
        self.tot2.setText(output)
        self.update_total()


    def add3_one(self):
        input = self.tot3.text()
        output = str(int(input) + 1)
        self.tot3.setText(output)
        self.update_total()


    def sub3_one(self):
        input = self.tot3.text()
        output = str(int(input) - 1)
        self.tot3.setText(output)
        self.update_total()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
sys.exit(app.exec_())
