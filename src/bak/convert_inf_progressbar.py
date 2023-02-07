from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time


# Jet： 测试用线程刷新GUI的显示，成功

# 继承QThread
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    # Jet: int:数字信息
    # str: 字符串信息
    _signal = pyqtSignal(int, str)#可以传递多个信息参数

    def __init__(self, audio_file, raw_txt_file):
        super(Runthread, self).__init__()
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file

    # def __del__(self):
    #     self.wait()

    # i: 对应进度条的1-100
    # msg:要在UI显示的信息（从服务器返回的转写过程中的实时信息）
    def emit_msg(self, i, msg):
        self._signal.emit(i, msg)  # 注意这里的参数需要与pyqtSignal定义的一致

    # 调用讯飞转写，并同步输出服务器转写过程中返回的实时信息，显示到UI
    def xunfei_converting(self):
        msg = "Start：调用讯飞转写语音文件：" + self.audio_file
        self.emit_msg(1, msg)
        time.sleep(2)
        self.emit_msg(50, msg)
        time.sleep(2)
        # self参数传给JetsXunfeiApi,以便在其中函数中调用本类中定义的print_info函数， 打印信息到UI TextBrowser中
        # JetsXunfeiApi.convert_1speaker_audio_to_text_with_gui(audio_file, raw_txt_file, self)  # self传进去，以便用讯飞服务器返回的信息来刷新UI显示信息
        #注意，需要调用的函数是1speaker还是2speakers

        msg = "Finish: 原始语音转写到文件%s完成。 Thread ends." % self.raw_txt_file
        self.emit_msg(100, msg)

    def run(self):
        #Jet:在此调用函数，根据进展情况emit(i),刷新进度信息及进度条GUI显示
        #需要根据音频的大小（长度）来估算转写的时间，确定i值（对应进度条的值1-100)
        self.xunfei_converting()

        '''
        for i in range(100):
            time.sleep(0.2)
            self._signal.emit(i, "info" + str(i))  # 注意这里的参数需要与pyqtSignal定义的一致
        '''

    @property #访问私有变量（不能被子类继承）
    def signal(self):
        return self._signal


class Converting_Dialog(QtWidgets.QWidget):

    def __init__(self, audio_file, raw_txt_file):
        super().__init__()
        #Jet:初始化音频文件、转写原始文本文件的全路径及文件名
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file

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

        self.thread = None  # 初始化线程

    def start_login(self):
        # 创建线程，包含音频文件及文本文件名（从构造函数传递来的）
        self.thread = Runthread(self.audio_file, self.raw_txt_file)
        # 连接信号
        self.thread.signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

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
    audio_file =r"D:\Jet's Docs\Jet 常用文档-Asus\#2-2020 Ministry\James-雅各书-讲章\6-21 雅1：1-8 主日.mp3"
    raw_txt_file =r"D:\Jet's Docs\Jet 常用文档-Asus\#2-2020 Ministry\James-雅各书-讲章\6-21 雅1：1-8 主日_raw.txt"
    myshow = Converting_Dialog(audio_file, raw_txt_file)
    myshow.show()
    sys.exit(app.exec_())