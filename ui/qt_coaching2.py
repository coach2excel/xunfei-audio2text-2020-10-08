# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_coaching2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

#Jet: 修改自动生成的.py程序，能正常运行了

#class Ui_MainWindow(object):
class Ui_MainWindow(QMainWindow):


    #Jet:定义呼应radiobtn的事件，确定用户选择speaker1是教练/客户
    def on_radio_button_toggled(self):
        sender = self.sender()
        self.speaker1 = sender.text() #根据用户选择的speaker1,决定是教练还是客户

        self.statusBar().showMessage("Selected speaker1 is %s" % sender.text() )

        #to add:
        #automatically set speaker2 to 客户/教练:



    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

    #def setupUi(self, MainWindow):
        #self.statusBar()  # Jet 这个会用上！

        #self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.centralwidget = QtWidgets.QWidget(self)

        self.centralwidget.setObjectName("centralwidget")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(170, 120, 89, 16))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 120, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        #'''
        self.radioButton.setChecked(True)
        self.radioButton.speaker = "教练"
        self.radioButton_2.setChecked(False)
        self.radioButton_2.speaker = "客户"
        #'''
        '''
        self.layout = QGridLayout()
        self.setLayout(layout)

        self.radiobutton = QRadioButton("教练")
        self.radiobutton.setChecked(True)
        self.radiobutton.speaker = "教练"
        self.radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.layout.addWidget(radiobutton, 0, 0)

        self.radiobutton = QRadioButton("客户")
        self.radiobutton.country = "客户"
        self.radiobutton.toggled.connect(self.on_radio_button_toggled)
        self.layout.addWidget(radiobutton, 0, 1)
        '''

        self.btn_selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.btn_selectAll.setGeometry(QtCore.QRect(210, 420, 75, 23))
        self.btn_selectAll.setObjectName("btn_selectAll")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 120, 54, 12))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 190, 256, 192))

        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(50, 380, 251, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy.setGeometry(QtCore.QRect(70, 420, 75, 23))
        self.btn_copy.setObjectName("btn_copy")

        self.setCentralWidget(self.centralwidget)

        #self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar = QtWidgets.QMenuBar(self)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")

        self.setMenuBar(self.menubar)

        #self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar = QtWidgets.QStatusBar(self)

        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)

        self.retranslateUi()

        #self.radioButton.toggled['bool'].connect(self.radioButton_2.setChecked) #Jet：这里如何变成setChecked(False)?

        self.radioButton.toggled.connect(self.on_radio_button_toggled)
        self.radioButton_2.toggled.connect(self.on_radio_button_toggled)

        self.btn_selectAll.clicked.connect(self.textBrowser.selectAll)
        self.btn_copy.clicked.connect(self.textBrowser.copy)

        QtCore.QMetaObject.connectSlotsByName(self)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "教练"))
        self.btn_selectAll.setText(_translate("MainWindow", "Select All"))
        self.label.setText(_translate("MainWindow", "Speaker1："))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'隶书\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这里是显示的文字</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示的文字</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示的文字</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示的文字</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示的文字</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示的文字</p></body></html>"))
        self.radioButton_2.setText(_translate("MainWindow", "客户"))
        self.btn_copy.setText(_translate("MainWindow", "Copy"))


if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
