# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert_info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
'''
Jet: for testing only!
放弃使用！有参考价值

当程序开始调用讯飞API转写语音时，打开此子窗口，显示转写进度
应当选择模式对话框锁定程序！

模式对话框 与 非模式对话框 （modeless dialog | modal dialog）

模式对话框，就是在弹出窗口的时候，整个程序就被锁定了，处于等待状态，直到对话框被关闭。这时往往是需要对话框的返回值进行下面的操作。如：确认窗口（选择“是”或“否”）。
非模式对话框，在调用弹出窗口之后，调用即刻返回，继续下面的操作。这里只是一个调用指令的发出，不等待也不做任何处理。如：查找框。

show() ------  modeless dialog

exec() ------- modal dialog
————————————————
版权声明：本文为CSDN博主「jianglz-gz」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_40520077/article/details/104040414
'''

from PyQt5 import QtCore, QtGui, QtWidgets
#Tip： 在项目src目录上右键，选择“Mark Directory as”为“Sources Root”，以下导入时就不会显示红色波浪线了
#from JetsXunfeiApi  import *
import JetsXunfeiApi # 用于调用Jet自己开发的讯飞转写函数
import subprocess  # 用于显示调用讯飞过程中在cmd中打印的信息


# 这是从QT Designer生成的uc 转成的.py文件
'''
控制台输出定向到QtextBrowser中,以便用户查看讯飞转写的进度...
'''

class XunfeiConvertingDialog(object):

    # def __init__(self):

    def setupUi(self, Dialog):
        print("in ConvertingDialog setupUi")
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 455)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 420, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 601, 321))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 391, 16))
        self.label.setObjectName("label")

        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 380, 581, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "讯飞语音转写文字"))
        self.label.setText(_translate("Dialog", "请耐心等待文件上传并转写完成。转写过程提示信息如下："))

    #Jet:自定义的打印函数，把print的信息打印到textBrowser上
    # 参考：https: // blog.csdn.net / weixin_43097265 / article / details / 92830565
    def print_info(self, content):
        #print("调用print_info 1")
        self.textBrowser.append(content)# 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿


    def xunfei_converting(self, audio_file, raw_txt_file):
        # 此处调用Jet定义的函数
        print("调用child window中的讯飞转写函数成功")
        self.print_info("Start：调用讯飞转写语音。")

        # self参数传给JetsXunfeiApi,以便在其中函数中调用本类中定义的print_info函数， 打印信息到UI TextBrowser中
        JetsXunfeiApi.convert_to_file(self, audio_file, raw_txt_file)  # 这两个参数由前两个函数调用时设置值
        self.print_info("Finish: 调用讯飞转写函数完成。")

        # show status in status bar every 10 seconds...
        # 可在新窗口中加一个进度条（大致估算一下时间，按转写时长，audio文件大写（与上传时间有关）
        # 否则用户不知道程序在干什么！！！
        # 参考https://blog.csdn.net/ccj15010192778/article/details/102704301?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
