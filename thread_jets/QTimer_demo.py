from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys

class ShowTime(QWidget):
    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout= QGridLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)

        # 窗口初始化
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('当前时间、定时器')
        self.show()


    def showTime(self):
        time = QDateTime.currentDateTime()

        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())
'''
————————————————
版权声明：本文为CSDN博主「润森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44510615/article/details/90339614
'''