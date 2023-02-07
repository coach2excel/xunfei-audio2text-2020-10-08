from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
from matplotlib import pyplot as plt
from skimage import transform, data
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# 对应父窗口文件
#from MainWindow import Ui_MainWindow
# 对应子窗口文件
#from getimage import Ui_getimage
import os


# 父窗口
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.vdieo2imagewindow = Vdieo2ImageWindow()
        self.cropimagewindow = CropImageWindow()
        self.labelimagewindow = LabelImageWindow()
        self.labelobjectwindow = LabelObjectWindow()
        self.correctpersonwindow = CorrectPersonWindow()
        self.grouppersonwindow = GroupPersonWindow()

    # 子窗口
    def Video2Image(self):
        self.gridLayout2.addWidget(self.vdieo2imagewindow)  # 将窗口放入girdLayout中
        self.vdieo2imagewindow.show()  # 打开子窗口1


# 子窗口
class Vdieo2ImageWindow(QMainWindow, Ui_getimage):

    def __init__(self):
        super(Vdieo2ImageWindow, self).__init__()
        self.setupUi(self)

    # 退出函数，可以在子窗口的代码中创建指向此函数的事件。
    def Close(self):
        reply = QMessageBox.question(self, '确认框', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.hide()
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1080, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setGeometry(QtCore.QRect(0, 0, 1080, 200))
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(30)
        self.gridLayout.setObjectName("gridLayout")

        # 提取图片按钮
        self.GetImg = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GetImg.setMinimumSize(QtCore.QSize(230, 36))
        self.GetImg.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.GetImg.setFont(font)
        self.GetImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetImg.setObjectName("GetImg")
        self.gridLayout.addWidget(self.GetImg, 0, 0, 1, 1)

        # 目标标注按钮
        self.Label_Object = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Label_Object.setMinimumSize(QtCore.QSize(230, 36))
        self.Label_Object.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.Label_Object.setFont(font)
        self.Label_Object.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Label_Object.setObjectName("Label_Object")
        self.gridLayout.addWidget(self.Label_Object, 0, 1, 1, 1)

        # 对目标标注的纠错按钮
        self.CorrectObject = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CorrectObject.setMinimumSize(QtCore.QSize(230, 36))
        self.CorrectObject.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CorrectObject.setFont(font)
        self.CorrectObject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CorrectObject.setObjectName("CorrectObject")
        self.gridLayout.addWidget(self.CorrectObject, 0, 2, 1, 1)
        self.CorrectPerson = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CorrectPerson.setMinimumSize(QtCore.QSize(230, 36))
        self.CorrectPerson.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CorrectPerson.setFont(font)
        self.CorrectPerson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CorrectPerson.setObjectName("CorrectPerson")
        self.gridLayout.addWidget(self.CorrectPerson, 1, 2, 1, 1)

        # 将行人分类按钮
        self.GroupPerson = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GroupPerson.setMinimumSize(QtCore.QSize(230, 36))
        self.GroupPerson.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.GroupPerson.setFont(font)
        self.GroupPerson.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GroupPerson.setObjectName("GroupPerson")
        self.gridLayout.addWidget(self.GroupPerson, 1, 1, 1, 1)

        # 裁剪图片按钮
        self.CropImg = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CropImg.setMinimumSize(QtCore.QSize(230, 36))
        self.CropImg.setBaseSize(QtCore.QSize(230, 36))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.CropImg.setFont(font)
        self.CropImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CropImg.setObjectName("CropImg")
        self.gridLayout.addWidget(self.CropImg, 1, 0, 1, 1)

        # self.gridLayoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        # self.gridLayoutWidget2.setGeometry(QtCore.QRect(0, 0, 1380, 720))
        # self.gridLayoutWidget2.setObjectName("gridLayoutWidget2")
        self.gridLayout2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout2.setGeometry(QtCore.QRect(0, 0, 1080, 500))
        self.gridLayout2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout2.setSpacing(0)
        self.gridLayout2.setObjectName("gridLayout2")


        # 工具栏
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # 按钮事件
        self.retranslateUi(MainWindow)
        self.GetImg.clicked.connect(MainWindow.Video2Image)
        self.Label_Object.clicked.connect(MainWindow.Video2Image)
        self.CorrectObject.clicked.connect(MainWindow.Video2Image)
        self.CorrectPerson.clicked.connect(MainWindow.Video2Image)
        self.GroupPerson.clicked.connect(MainWindow.Video2Image)
        self.CropImg.clicked.connect(MainWindow.Video2Image)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 文本设置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "行人重识别数据集标注软件"))
        self.GetImg.setText(_translate("MainWindow", "1"))
        self.Label_Object.setText(_translate("MainWindow", "2"))
        self.CorrectObject.setText(_translate("MainWindow", "3"))
        self.CorrectPerson.setText(_translate("MainWindow", "4"))
        self.GroupPerson.setText(_translate("MainWindow", "5"))
        self.CropImg.setText(_translate("MainWindow", "6"))

class Ui_getimage(object):
    def setupUi(self, getimage):
        getimage.setObjectName("getimage")
        getimage.resize(900, 700)
        # 栅格化布局
        self.gridLayoutWidget = QtWidgets.QWidget(getimage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(100, 50, 100, 30)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        # 选择视频按钮
        self.SelectVideo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SelectVideo.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SelectVideo.setFont(font)
        self.SelectVideo.setObjectName("SelectVideo")
        self.gridLayout.addWidget(self.SelectVideo, 0, 2, 1, 1)
        # 保存图片的路径按钮
        self.SavePicPath = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SavePicPath.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SavePicPath.setFont(font)
        self.SavePicPath.setObjectName("SavePicPath")
        self.gridLayout.addWidget(self.SavePicPath, 1, 2, 1, 1)
        # 标签
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(130, 30))
        self.label.setBaseSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        # 视频路径文本框
        self.videopath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.videopath.setMinimumSize(QtCore.QSize(246, 30))
        self.videopath.setObjectName("videopath")
        self.gridLayout.addWidget(self.videopath, 0, 1, 1, 1)
        # 保存图片路径文本框
        self.savepicpath = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.savepicpath.setMinimumSize(QtCore.QSize(246, 30))
        self.savepicpath.setObjectName("savepicpath")
        self.gridLayout.addWidget(self.savepicpath, 1, 1, 1, 1)
        # 标签
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(130, 30))
        self.label_2.setBaseSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        # 帧数间隔文本框
        self.framenum = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.framenum.setMinimumSize(QtCore.QSize(246, 30))
        self.framenum.setObjectName("framenum")
        self.gridLayout.addWidget(self.framenum, 2, 1, 1, 1)
        # 标签
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(130, 30))
        self.label_3.setBaseSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        # 底部横向布局
        self.horizontalLayoutWidget = QtWidgets.QWidget(getimage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 600, 901, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(600, 20, 30, 20)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 确定以及退出按钮
        self.Confirm_get = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Confirm_get.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Confirm_get.setFont(font)
        self.Confirm_get.setObjectName("Confirm_get")
        self.horizontalLayout.addWidget(self.Confirm_get)
        self.Quit_get = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Quit_get.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Quit_get.setFont(font)
        self.Quit_get.setObjectName("Quit_get")
        self.horizontalLayout.addWidget(self.Quit_get)

        # 按钮点击事件指向
        self.retranslateUi(getimage)
        QtCore.QMetaObject.connectSlotsByName(getimage)

    # 元素内文本显示设置
    def retranslateUi(self, getimage):
        _translate = QtCore.QCoreApplication.translate
        getimage.setWindowTitle(_translate("getimage", "label"))
        self.SelectVideo.setText(_translate("getimage", "button"))
        self.SavePicPath.setText(_translate("getimage", "button"))
        self.label.setText(_translate("getimage", "label："))
        self.label_2.setText(_translate("getimage", "label："))
        self.label_3.setText(_translate("getimage", "label："))
        self.Confirm_get.setText(_translate("getimage", "button"))
        self.Quit_get.setText(_translate("getimage", "button"))

"""
————————————————
版权声明：本文为CSDN博主「Anthony」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43159628/article/details/90748671
"""