#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

author: Jan Bodnar
website: py40.com
last edited: January 2015

Jet: 可以用此来控制教练录音播放的时间，配合相应的文字显示
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Dontla 20200419 创建一个用于显示数字或符号的容器
        lcd = QLCDNumber(self)
        # Dontla 20200420 创建一个滑块
        sld = QSlider(Qt.Horizontal, self)

        # Dontla 20200420 创建一个垂直布局管理器
        vbox = QVBoxLayout()

        # Dontla 20200420 将小部件加入到垂直布局管理器中
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        # Dontla 20200420 将垂直布局管理器中的小部件重新进行父级化，以将窗口小部件作为父级？
        self.setLayout(vbox)

        # Dontla 20200420 将滑块数值改变的信号链接到显示数字或符号的容器的显示插槽
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
'''
————————————————
版权声明：本文为CSDN博主「Dontla」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Dontla/article/details/105621895
'''