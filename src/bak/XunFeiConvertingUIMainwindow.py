# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_coaching4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
# import subprocess #用于显示调用讯飞过程中在cmd中打印的信息
#from XunFeiConvertingUIMainwindow import XunFeiConvertingUIMainWindow

'''
修改记录：
06-28 从qt_coaching4_modify_to_Run_4.6.py另存为本文件
2020-06-13 添加按钮：提交讯飞原始转换
2020-06-12 实现功能：radiobutton选择教练/客户

'''


# Jets: 主窗口
class ParentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = XunFeiConvertingUIMainWindow()


# Jets: 子窗口，讯飞转写监控（显示进度和提示信息）
class ChildWindow(QDialog):
    def __init__(self, audio_file, raw_txt_file):
        QDialog.__init__(self)
        self.child = XunFeiConvertingUIMainWindow()
        self.child.setupUi(self)
        # 在主窗口已经选择好了
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file
        #
        self.child.xunfei_converting(self.audio_file, self.raw_txt_file)


# Jets：从ui文件生成py文件之后，需要作相应的修改（见相应注释）
# class Ui_MainWindow(object):#ui自动生成的
class XunFeiConvertingUIMainWindow(QMainWindow):  # 手工修改成这样

    # Jet：这是需要增加的
    def __init__(self):
        super().__init__()
        self.initUI()  # Jet：这是需要增加的,在下面编写具体代码

    # 根据用户选择Speaker1的Radiobutton, 确定speaker1和speaker2的身分
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

    # 根据用户选择Speaker2的Radiobutton, 确定speaker1和speaker2的身分
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

    # Jets: 生成界面。需要修改：ui默认生成的是 def setupUi(self, self):
    def initUI(self):
        # Jet：需要把MainWindow替代为self
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1284, 982)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.setObjectName("MainWindow")
        self.resize(1284, 950)

        # 初始化要选择的音频文件和要保存的原始转写文件
        self.audio_file = ""
        self.raw_txt_file = ""
        # self.cwd = os.getcwd()  # 获取当前程序文件位置

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1261, 911))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")

        # 第一行的控件
        self.btn_locate_audio_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_locate_audio_file.setObjectName("btn_locate_audio_file")
        self.gridLayout.addWidget(self.btn_locate_audio_file, 0, 0, 1, 1)

        self.lineEdit_audio_file = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_audio_file.setObjectName("lineEdit_audio_file")
        self.gridLayout.addWidget(self.lineEdit_audio_file, 0, 1, 1, 3)

        # 此按钮：打开对话框，设置原始转换的结果另存为的文件名（全路径+默认文件名）
        self.btn_set_raw_output_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_set_raw_output_file.setObjectName("btn_set_raw_output_file")
        # Jet:参数说明：gridLayout.addWidget(widget, row, column, columnspan, alignment)
        self.gridLayout.addWidget(self.btn_set_raw_output_file, 0, 4, 1, 1)

        # btn提交讯飞原始转换
        self.btn_xunfei2txt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_xunfei2txt.setObjectName("btn_xunfei2txt")
        self.gridLayout.addWidget(self.btn_xunfei2txt, 0, 5, 1, 1)

        # 第二行的控件
        # 对RadioButton分组
        self.radioButtonGroup1 = QtWidgets.QButtonGroup(self.gridLayoutWidget)
        self.radioButton_s1iscoach = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButtonGroup1.addButton(self.radioButton_s1iscoach, 1)

        self.radioButton_s1iscoach.setChecked(True)
        self.radioButton_s1iscoach.setObjectName("radioButton_s1iscoach")

        self.gridLayout.addWidget(self.radioButton_s1iscoach, 2, 1, 1, 1)

        # self.radioButton_s1iscoach.toggled.connect(self.onRadioButtonClicked)#Jet:注意，函数调用不能加()

        self.radioButton_s1isclient = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.radioButton_s1isclient.setChecked(False)
        # self.radioButton_s1isclient.setCheckable(True)
        self.radioButton_s1isclient.setObjectName("radioButton_s1isclient")
        self.gridLayout.addWidget(self.radioButton_s1isclient, 2, 2, 1, 1)
        self.radioButtonGroup1.addButton(self.radioButton_s1isclient, 2)

        # self.radioButton_s1isclient.toggled.connect(self.onRadioButtonClicked)

        # 对RadioButton分组
        self.radioButtonGroup2 = QtWidgets.QButtonGroup(self.gridLayoutWidget)

        self.radioButton_s2isclient = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.radioButton_s2isclient.setCheckable(False)
        self.radioButton_s2isclient.setChecked(True)
        self.radioButton_s2isclient.setObjectName("radioButton_s2isclient")
        self.gridLayout.addWidget(self.radioButton_s2isclient, 2, 4, 1, 1)

        # self.radioButton_s2isclient.toggled.connect(self.onRadioButtonClicked2)

        self.radioButton_s2iscoach = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.radioButton_s2iscoach.setCheckable(False)
        self.radioButton_s2iscoach.setChecked(False)
        self.radioButton_s2iscoach.setObjectName("radioButton_s2iscoach")
        self.gridLayout.addWidget(self.radioButton_s2iscoach, 2, 5, 1, 1)

        # self.radioButton_s2iscoach.toggled.connect(self.onRadioButtonClicked2)

        self.radioButtonGroup2.addButton(self.radioButton_s2iscoach, 1)
        self.radioButtonGroup2.addButton(self.radioButton_s2isclient, 2)

        self.btn_save_raw_to_txt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save_raw_to_txt.setObjectName("btn_save_raw_to_txt")
        self.gridLayout.addWidget(self.btn_save_raw_to_txt, 9, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.tableWidget_raw = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_raw.setObjectName("tableWidget_raw")
        self.tableWidget_raw.setColumnCount(0)
        self.tableWidget_raw.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_raw, 7, 0, 1, 3)

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)

        self.btn_stop_audio = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_stop_audio.setObjectName("btn_stop_audio")
        self.gridLayout.addWidget(self.btn_stop_audio, 9, 1, 1, 1)

        self.horizontalSlider_audio = QtWidgets.QSlider(self.gridLayoutWidget)
        self.horizontalSlider_audio.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_audio.setObjectName("horizontalSlider_audio")
        self.gridLayout.addWidget(self.horizontalSlider_audio, 8, 0, 1, 3)

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

        # self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        # self.label_7.setObjectName("label_7")
        # self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)
        self.tableWidget_icf = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_icf.setObjectName("tableWidget_icf")
        self.tableWidget_icf.setColumnCount(0)
        self.tableWidget_icf.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_icf, 7, 3, 1, 3)
        self.btn_locate_output_path = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_locate_output_path.setObjectName("btn_locate_output_path")
        self.gridLayout.addWidget(self.btn_locate_output_path, 10, 0, 1, 1)

        # self.radioButton_export_stat = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.radioButton_export_stat.setObjectName("radioButton_export_stat")
        self.ckbox_export_stat = QtWidgets.QCheckBox(self.gridLayoutWidget)
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

        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setRowStretch(7, 12)
        self.gridLayout.setRowStretch(8, 2)
        self.setCentralWidget(self.centralwidget)

        ''' #取消菜单栏
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1284, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        '''
        # Jet: 添加状态栏
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setEnabled(True)
        # self.statusBar()  #Jet：修改，添加状态栏
        font = QtGui.QFont()
        font.setPointSize(10)

        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        # self.statusbar.showMessage('here is statusbar') # 在状态栏显示指定消息

        # self.retranslateUi(MainWindow)
        self.retranslateUi()

        # self.radioButton_s1iscoach.toggled['bool'].connect(self.radioButton_s1isclient.setChecked)

        QtCore.QMetaObject.connectSlotsByName(self)
        # print('here3.')

        # Jet: 按钮绑定相应事件,必须调用此函数！
        self.bind_events()

        # Jet: 添加以下这句，很关键，否则不显示窗口！
        self.show()

    # Jets：显示界面的文字。 从def retranslateUi(self, MainWindow)改写为:
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Jet's 音频转写-文字转换ICF格式"))

        self.btn_locate_audio_file.setText(_translate("MainWindow", "1、请选择录音文件(mp3/wav)"))
        self.btn_set_raw_output_file.setText(_translate("MainWindow", "2、设置原始文稿目录及文件名txt"))
        # btn提交讯飞原始转换
        self.btn_xunfei2txt.setText(_translate("MainWindow", "3、提交讯飞开始语音转换"))

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
        # self.label_7.setText(_translate("MainWindow", "Logo Empower All"))
        self.btn_locate_output_path.setText(_translate("MainWindow", "请选择默认保存目录"))

        self.ckbox_export_stat.setText(_translate("MainWindow", "输出包含统计信息"))

        self.btn_save_icf_to_txt.setText(_translate("MainWindow", "保存教练文稿到txt文档"))
        self.btn_save_icf_to_word.setText(_translate("MainWindow", "保存教练文稿到Word文档"))
        self.label_6.setText(_translate("MainWindow", "（注：讯飞转写可能存在少量错误，请根据实际录音编辑，满意之后再保存)"))
        self.btn_save_raw_to_txt.setText(_translate("MainWindow", "保存原始文稿到txt文档"))

        # self.menu.setTitle(_translate("MainWindow", "教练录音转写助手"))

    # Jet: 用户选择用于转写文字的音频文件
    def btn_locate_audio_file_clicked(self):
        print("btn locate audio clicked.")
        # show open file dialog
        self.cwd = os.getcwd()  # 获取当前程序文件位置

        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "音频文件 (*.wav;*.mp3)")  # 设置文件扩展名过滤,用双分号间隔;目前只支持这两种音频格式

        if fileName_choose == "":
            # print("\n取消选择")
            # 警告：未选择音频文件
            QMessageBox.warning(self, '温馨提示', '您还没选择要转写的音频文件！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        # 修改当前路径为用户选择的音频文件目录
        # self.cwd = fileName_choose[0:-4] #不对，只是去年了后缀名！
        # 以上返回的是QString类型的对象，若想不出现编码问题，建议用如下语句将QString转换为python的string对象
        # fileName_choose = unicode(fileName_choose.toUtf8(), 'utf-8', 'ignore')

        print("file:", fileName_choose)

        self.cwd, tempfilename = os.path.split(fileName_choose)  # 分享文件路径和文件名
        self.filename_withoutextension, extension = os.path.splitext(tempfilename)  # 分享文件名和后缀
        '''
        import os
        file_path = "D:/test/test.py"
        (filepath, tempfilename) = os.path.split(file_path)
        (filename, extension) = os.path.splitext(tempfilename)
        '''

        print("\n你选择的文件所在目录为:%s, 文件名为%s" % (self.cwd, self.filename_withoutextension))
        # print("文件筛选器类型: ",filetype)

        # 后续函数调用需用
        self.audio_file = fileName_choose

        # show the file path and name in the lineEdit
        self.lineEdit_audio_file.setText(fileName_choose)
        self.lineEdit_audio_file.setEnabled(False)

        self.statusbar.showMessage("您选择要转写的音频文件是" + fileName_choose)

        QMessageBox.information(self, '下一步', '请选择第2步：设置保存原始转写文件的目录和文件名', QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)

    # 用户选择保存原始转写结果的目录和文件名
    def btn_set_raw_output_file_clicked(self):
        # show save as dialog
        if self.cwd == "":
            self.cwd = os.getcwd()  # 获取当前程序文件位置
        # 否则使用和所选定音频文件所在的目录（见上一个函数）

        #self.filename_withoutextension
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                                                "文件保存为",
                                                                self.cwd,  # 起始路径
                                                                "Text Files (*.txt);;All Files (*)")  # 默认为txt格式
        # set default file name:

        if fileName_choose == "":
            # 警告：未选择文件名
            QMessageBox.warning(self, '温馨提示', '您还没选择要保存的文件名！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return

        # 后续函数调用需用
        self.raw_txt_file = fileName_choose  # 修改为用户输入的内容

        # show the file path and name in the lineEdit
        self.lineEdit_audio_file.setText(fileName_choose)
        self.lineEdit_audio_file.setEnabled(False)

        self.statusbar.showMessage("您选择要保存的原始转写的文件是" + fileName_choose)

    # 调用Jet的讯飞转写函数，开始转写，显示转写进度的GUI, 存入用户指定的原始文件名
    def btn_xunfei2txt_clicked(self):

        if self.audio_file == "":
            # 警告：未选择文件名
            QMessageBox.warning(self, '温馨提示', '您还没选择要转写的音频文件！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return

        if self.raw_txt_file == "":
            # 警告：未选择文件名
            QMessageBox.warning(self, '温馨提示', '您还没选择要保存的文件名！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return

        self.statusbar.showMessage("开始转写音频文件" + self.audio_file)

        print("start call new Dialog:显示转写进度对话框，实时刷新转写情况")
        # 传递参数到子窗口
        child = ChildWindow(window.main_ui.audio_file, window.main_ui.raw_txt_file) # 这两个参数由前两个函数调用时设置值
        child.exec_() #显示为model dialog模式对话框，未完成之前不得回到主窗口
        '''
        child_window = QDialog()  # Jet: 这里很关键
        child_window_ui = convert_info_dialog.XunfeiConvertingDialog()
        child_window_ui.setupUi(child_window)
        child_window.show()

        child_window_ui.convert_to_file(self.audio_file, self.raw_txt_file)  # 这两个参数由前两个函数调用时设置值
        '''
        #print("end call new Dialog")
        self.statusbar.showMessage("转写音频文件%s成功" %self.audio_file)

        # clear status bar msg

    # 绑定按钮事件，
    # 需要被函数initUI调用
    def bind_events(self):

        self.btn_locate_audio_file.clicked.connect(self.btn_locate_audio_file_clicked)
        self.btn_set_raw_output_file.clicked.connect(self.btn_set_raw_output_file_clicked)
        self.btn_xunfei2txt.clicked.connect(self.btn_xunfei2txt_clicked)

        self.radioButton_s1iscoach.toggled.connect(self.onRadioButtonClicked)  # Jet:注意，函数调用不能加()
        self.radioButton_s1isclient.toggled.connect(self.onRadioButtonClicked)
        self.radioButton_s2iscoach.toggled.connect(self.onRadioButtonClicked2)
        self.radioButton_s2isclient.toggled.connect(self.onRadioButtonClicked2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Jet: 这里改写
    window = ParentWindow()
    '''
    #传递参数到子窗口
    child = ChildWindow(window.main_ui.audio_file, window.main_ui.raw_txt_file)

    # 通过toolButton将两个窗体关联
    btn = window.main_ui.btn_xunfei2txt
    btn.clicked.connect(child.show)  #显示转写状态的子窗口
    '''
    #window.show()  # Jet:有此句会多出现一个窗口！
    # ex = Ui_MainWindow()
    sys.exit(app.exec_())
