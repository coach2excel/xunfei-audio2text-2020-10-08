# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_coaching4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


#Jet：需要修改
#class Ui_MainWindow(object):
class Ui_MainWindow(QMainWindow):
    # Jet：这是需要增加的
    def __init__(self):
        super().__init__()

        self.initUI() #Jet：这是需要增加的

    #根据用户选择Speaker1的Radiobutton, 确定speaker1和speaker2的身分
    def onRadioButtonClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            if radioBtn.text() == "教练":
                print("speaker1 is:教练")
                self.speaker1 = "教练"
                self.statusbar.showMessage("speaker1 is:" + self.speaker1)
                self.radioButton_s2iscoach.setChecked(False)
                self.radioButton_s2isclient.setChecked(True)

            if radioBtn.text() == "客户":
                print("speaker1 is:客户")
                self.speaker1 = "客户"
                self.statusbar.showMessage("speaker1 is:" + self.speaker1)
                self.radioButton_s2iscoach.setChecked(True)
                self.radioButton_s2isclient.setChecked(False)

    #根据用户选择Speaker2的Radiobutton, 确定speaker1和speaker2的身分
    def onRadioButtonClicked2(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            if radioBtn.text() == "教练":
                print("speaker1 is:客户")
                self.speaker1 = "客户"
                self.statusbar.showMessage("speaker1 is:" + self.speaker1)
                self.radioButton_s1iscoach.setChecked(False)
                self.radioButton_s1isclient.setChecked(True)

            if radioBtn.text() == "客户":
                print("speaker1 is:教练")
                self.speaker1 = "教练"
                self.statusbar.showMessage("speaker1 is:" + self.speaker1)
                self.radioButton_s1iscoach.setChecked(True)
                self.radioButton_s1isclient.setChecked(False)



    #这是需要地修改的：
    #def setupUi(self, self):
    def initUI(self):
        #Jet：需要把MainWindow替代为self
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1284, 982)
        #self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.setObjectName("MainWindow")
        self.resize(1284, 982)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1261, 911))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 2)
        
        #'''
        #对RadioButton分组
        self.radioButtonGroup1 = QtWidgets.QButtonGroup(self.gridLayoutWidget)
        self.radioButton_s1iscoach = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButtonGroup1.addButton(self.radioButton_s1iscoach, 1)
        
        self.radioButton_s1iscoach.setChecked(True)
        #self.radioButton_s1iscoach.setCheckable(True)
        self.radioButton_s1iscoach.setObjectName("radioButton_s1iscoach")
        
        self.gridLayout.addWidget(self.radioButton_s1iscoach, 2, 1, 1, 1)

        self.radioButton_s1iscoach.toggled.connect(self.onRadioButtonClicked)#Jet:注意，函数调用不能加()

        self.radioButton_s1isclient = QtWidgets.QRadioButton(self.gridLayoutWidget)
        #self.radioButton_s1isclient.setChecked(False)
        #self.radioButton_s1isclient.setCheckable(True)
        self.radioButton_s1isclient.setObjectName("radioButton_s1isclient")
        self.gridLayout.addWidget(self.radioButton_s1isclient, 2, 2, 1, 1)
        self.radioButtonGroup1.addButton(self.radioButton_s1isclient, 2)

        self.radioButton_s1isclient.toggled.connect(self.onRadioButtonClicked)
        #'''
        #对RadioButton分组
        self.radioButtonGroup2 = QtWidgets.QButtonGroup(self.gridLayoutWidget)
        
        self.radioButton_s2isclient = QtWidgets.QRadioButton(self.gridLayoutWidget)
        #self.radioButton_s2isclient.setCheckable(False)
        self.radioButton_s2isclient.setChecked(True)
        self.radioButton_s2isclient.setObjectName("radioButton_s2isclient")
        self.gridLayout.addWidget(self.radioButton_s2isclient, 2, 4, 1, 1)
        
        self.radioButton_s2isclient.toggled.connect(self.onRadioButtonClicked2)

        self.radioButton_s2iscoach = QtWidgets.QRadioButton(self.gridLayoutWidget)
        #self.radioButton_s2iscoach.setCheckable(False)
        self.radioButton_s2iscoach.setChecked(False)
        self.radioButton_s2iscoach.setObjectName("radioButton_s2iscoach")
        self.gridLayout.addWidget(self.radioButton_s2iscoach, 2, 5, 1, 1)
        
        self.radioButton_s2iscoach.toggled.connect(self.onRadioButtonClicked2)
        
        self.radioButtonGroup2.addButton(self.radioButton_s2iscoach, 1)
        self.radioButtonGroup2.addButton(self.radioButton_s2isclient, 2)

        
        self.btn_save_raw_to_txt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save_raw_to_txt.setObjectName("btn_save_raw_to_txt")
        self.gridLayout.addWidget(self.btn_save_raw_to_txt, 9, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.tableWidget_raw = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_raw.setObjectName("tableWidget_raw")
        self.tableWidget_raw.setColumnCount(0)
        self.tableWidget_raw.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_raw, 7, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.btn_stop_audio = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_stop_audio.setObjectName("btn_stop_audio")
        self.gridLayout.addWidget(self.btn_stop_audio, 9, 1, 1, 1)
        
        self.horizontalSlider_audio = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_audio.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_audio.setObjectName("horizontalSlider_audio")
        self.gridLayout.addWidget(self.horizontalSlider_audio, 8, 0, 1, 3)
        self.lineEdit_audio_file = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_audio_file.setObjectName("lineEdit_audio_file")
        self.gridLayout.addWidget(self.lineEdit_audio_file, 0, 1, 1, 4)
        self.btn_play_audio = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_play_audio.setObjectName("btn_play_audio")
        self.gridLayout.addWidget(self.btn_play_audio, 9, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)


        self.btn_locate_audio_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_locate_audio_file.setObjectName("btn_locate_audio_file")
        self.gridLayout.addWidget(self.btn_locate_audio_file, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.tableWidget_icf = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_icf.setObjectName("tableWidget_icf")
        self.tableWidget_icf.setColumnCount(0)
        self.tableWidget_icf.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_icf, 7, 3, 1, 3)
        self.btn_locate_output_path = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_locate_output_path.setObjectName("btn_locate_output_path")
        self.gridLayout.addWidget(self.btn_locate_output_path, 10, 0, 1, 1)

        #self.radioButton_export_stat = QtWidgets.QRadioButton(self.gridLayoutWidget)
        #self.radioButton_export_stat.setObjectName("radioButton_export_stat")
        self.ckbox_export_stat =QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.ckbox_export_stat.setObjectName("ckbox_export_stat")
        self.gridLayout.addWidget(self.ckbox_export_stat, 10, 3, 1, 1)

        self.btn_save_icf_to_txt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save_icf_to_txt.setObjectName("btn_save_icf_to_txt")
        self.gridLayout.addWidget(self.btn_save_icf_to_txt, 10, 4, 1, 1)
        self.btn_save_icf_to_word = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save_icf_to_word.setObjectName("btn_save_icf_to_word")
        self.gridLayout.addWidget(self.btn_save_icf_to_word, 10, 5, 1, 1)
        self.tableWidget_stat = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_stat.setObjectName("tableWidget_stat")
        self.tableWidget_stat.setColumnCount(0)
        self.tableWidget_stat.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_stat, 8, 3, 2, 3)
        self.lineEdit_output_path = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_output_path.setObjectName("lineEdit_output_path")
        self.gridLayout.addWidget(self.lineEdit_output_path, 10, 1, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setRowStretch(7, 12)
        self.gridLayout.setRowStretch(8, 2)
        self.setCentralWidget(self.centralwidget)

        '''
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        '''

        #self.setMenuBar(self.menubar)
        #self.menubar.addAction(self.menu.menuAction())

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setEnabled(True)
        #self.statusBar()  #Jet：修改，添加状态栏


        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        #self.statusbar.showMessage('here is statusbar')

        #self.retranslateUi(MainWindow)
        self.retranslateUi()

        #self.radioButton_s1iscoach.toggled['bool'].connect(self.radioButton_s1isclient.setChecked)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        #print('here3.')

        #Jet: 添加以下这句，很关键，否则不显示窗口！
        self.show()

    #def retranslateUi(self, MainWindow):
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "（注：讯飞转写可能存在少量错误，请根据实际录音编辑，满意之后再保存)"))
        self.btn_save_raw_to_txt.setText(_translate("MainWindow", "保存原始文稿到txt文档"))
        self.radioButton_s2isclient.setText(_translate("MainWindow", "客户"))
        self.radioButton_s2iscoach.setText(_translate("MainWindow", "教练"))

        self.radioButton_s1iscoach.setText(_translate("MainWindow", "教练"))

        self.radioButton_s1isclient.setText(_translate("MainWindow", "客户"))

        self.label.setText(_translate("MainWindow", "请按实际情况指定：Speaker1："))
        self.label_2.setText(_translate("MainWindow", "Speaker2："))
        self.btn_stop_audio.setText(_translate("MainWindow", "停止"))
        self.btn_play_audio.setText(_translate("MainWindow", "播放"))
        self.label_5.setText(_translate("MainWindow", "（注：讯飞转写可能存在少量错误，请根据实际录音编辑)"))
        self.label_4.setText(_translate("MainWindow", "ICF教练文稿格式："))
        self.label_3.setText(_translate("MainWindow", "讯飞转写原始文稿："))
        self.btn_locate_audio_file.setText(_translate("MainWindow", "请选择录音文件(mp3/wav)"))
        self.label_7.setText(_translate("MainWindow", "Logo Empower All"))
        self.btn_locate_output_path.setText(_translate("MainWindow", "请选择默认保存目录"))

        self.ckbox_export_stat.setText(_translate("MainWindow", "输出包含统计信息"))

        self.btn_save_icf_to_txt.setText(_translate("MainWindow", "保存教练文稿到txt文档"))
        self.btn_save_icf_to_word.setText(_translate("MainWindow", "保存教练文稿到Word文档"))
        #self.menu.setTitle(_translate("MainWindow", "教练录音转写助手"))




if __name__ =='__main__':

    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    sys.exit(app.exec_())
