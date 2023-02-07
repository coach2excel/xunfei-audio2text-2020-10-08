# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xxx.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCursor
import sys


class Ui_MainWindow(QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 480)
        MainWindow.setMinimumSize(QtCore.QSize(690, 480))
        MainWindow.setMaximumSize(QtCore.QSize(690, 480))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 170, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.min_button = QtWidgets.QPushButton(self.centralwidget)
        self.min_button.setGeometry(QtCore.QRect(20, 20, 21, 21))
        self.min_button.setAutoFillBackground(False)
        self.min_button.setStyleSheet("background-color: rgb(28, 255, 3);")
        self.min_button.setText("")
        self.min_button.setAutoDefault(False)
        self.min_button.setDefault(False)
        self.min_button.setFlat(False)
        self.min_button.setObjectName("min_button")

        self.max_button = QtWidgets.QPushButton(self.centralwidget)
        self.max_button.setGeometry(QtCore.QRect(50, 20, 21, 21))
        self.max_button.setStyleSheet("background-color: rgb(255, 243, 75);")
        self.max_button.setText("")
        self.max_button.setObjectName("max_button")

        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(80, 20, 21, 21))
        self.close_button.setStyleSheet("background-color: rgb(255, 12, 12);")
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 441))
        self.label.setAutoFillBackground(True)
        self.label.setStyleSheet("background-color: rgb(209, 255, 171);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label.raise_()
        self.pushButton.raise_()
        self.min_button.raise_()
        self.max_button.raise_()
        self.close_button.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.close_button.clicked.connect(MainWindow.close)
        self.min_button.clicked.connect(MainWindow.showMinimized)
        # self.max_button.clicked.connect(MainWindow.showMaximized)  因为窗口固定，放大功能暂时关闭

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "->点击<-"))


class XX(QMainWindow):
    def __init__(self):
        super().__init__()

    # def keyPressEvent(self, event):
    #     print("12345")
    # def mousePressEvent(self,event):
    #     if event.button() == Qt.LeftButton:
    #         print("鼠标左键点击！")
    #         # print(event.pos().x(),event.pos().y())
    #     if event.button() == Qt.RightButton:
    #         print("鼠标右键点击！")
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = XX()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    with open("./QSS/自定义.qss") as f:
        MainWindow.setStyleSheet(f.read())
    MainWindow.show()
    sys.exit(app.exec_())
'''————————————————
版权声明：本文为CSDN博主「Kuoa」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / qq_42292831 / article / details / 94059218
'''
