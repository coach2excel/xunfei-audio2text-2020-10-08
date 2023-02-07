from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time


# 继承QThread
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    # Jet: int:数字信息
    # str: 字符串信息
    _signal = pyqtSignal(int, str)#可以传递多个信息参数

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def emit_msg(self, i, msg):
        if i%3 == 0:
            self._signal.emit(i, msg)  # 注意这里的参数需要与上面pyqtSignal定义的一致
            print("in emit_msg, msg received: ", msg)


    def run(self):
        #Jet:在此调用函数，根据进展情况emit(i),刷新进度信息及进度条GUI显示

        for i in range(100):
            time.sleep(0.2)
            #self._signal.emit(i, "info"+str(i))  # 注意这里的参数需要与pyqtSignal定义的一致
            self.emit_msg(i, "info"+str(i))

        self._signal.emit(100, "finish thread")

    def xunfei_converting(self, audio_file, raw_txt_file):
        # 此处调用Jet定义的函数
        print("调用child window中的讯飞转写函数成功")
        self.print_info("Start：调用讯飞转写语音。")

        # self参数传给JetsXunfeiApi,以便在其中函数中调用本类中定义的print_info函数， 打印信息到UI TextBrowser中
        #JetsXunfeiApi.convert_to_file(self, audio_file, raw_txt_file)  # 这两个参数由前两个函数调用时设置值
        self.print_info("Finish: 调用讯飞转写函数完成。")


class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # 按钮初始化
        self.button = QtWidgets.QPushButton('开始', self)
        self.button.setToolTip('这是一个 <b>QPushButton</b> widget')
        self.button.resize(self.button.sizeHint())
        self.button.move(120, 150)
        self.button.clicked.connect(self.start_login)  # 绑定多线程触发事件

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(10,5, 210, 100)


        # 进度条设置
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(50, 120, 210, 25)
        self.pbar.setValue(0)

        # 窗口初始化
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('OmegaXYZ.com')
        self.show()

        self.thread1 = None  # 初始化线程

    def start_login(self):
        # 创建线程
        self.thread1 = Runthread()
        # 连接信号
        self.thread1._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread1.start()

    def call_backlog(self, i, msg):
        self.pbar.setValue(i)  # 将线程的参数传入进度条
        print("msg:", msg)

        #Jet:自定义的打印函数，把print的信息打印到textBrowser上
        # 参考：https: // blog.csdn.net / weixin_43097265 / article / details / 92830565
        self.textBrowser.append(msg)# 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Example()
    myshow.show()
    sys.exit(app.exec_())