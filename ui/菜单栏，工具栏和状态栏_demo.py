#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction,QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon("exit.png"),"Exit",self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAct)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle("Main Window")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
'''
————————————————
版权声明：本文为CSDN博主「天堂1223」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hongbochen1223/article/details/78883258
'''