"""
@author Jet
@desc 用于动态显示讯飞转写的过程
@date 2020/06/28

"""
import sys
import time
from datetime import datetime

from PyQt5 import QtWidgets, QtCore
# from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtCore import *
from PyQt5.uic.properties import QtGui

import JetsXunfeiApi  # 用于调用Jet自己开发的讯飞转写函数
import getaudioinfo  # 特别注意：这是Jet自定义，获取音频文件时长，在audio文件夹下的getaudioinfo.py


# Jet:用于刷新显示当前转写用时的秒数
class TimeThread(QtCore.QThread):
    signal = pyqtSignal(int, str)

    def __init__(self):
        super(TimeThread, self).__init__()
        self.begin_time = datetime.now()

    def emit_msg(self, i, msg):
        self.signal.emit(i, msg)

    def run(self):
        seconds_elapsed = 0
        while True:
            time.sleep(1)
            seconds_elapsed += 1
            # 每隔1秒刷新显示一次（转写用时）
            msg = "已经用时%d秒" % seconds_elapsed
            # print(msg)
            self.emit_msg(seconds_elapsed, msg)


# Jet: 用于调用转写函数，并刷新转写进度提示的UI
class RunThread(QtCore.QThread):
    """
    @author Jet
    @desc 用于调用转写函数，并刷新转写进度提示的UI，包括进度条（百分比），讯飞服务器转写信息提示
    @date 2020/06/24

    """
    #  通过类成员对象定义信号对象
    #  int:数字信息,对应进度条1-100
    #  str: 获取来自讯飞服务器的提示信息，字符串信息，用于显示在文本框中
    signal = pyqtSignal(int, str)  # Jet: 可以传递多个信息参数
    #is_converting_finished = False # Jet: 是否转换成功的标记,没用，不能被调用！

    # 修改构造函数，添加要转写的语音文件，指定要转定到的文本文件名
    def __init__(self, audio_file, raw_txt_file, speaker_num=2):
        super(RunThread, self).__init__()
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file
        self.speaker_num = speaker_num

        # self.begin_time = QDateTime.currentDateTime()  # 设定开始转写的时间
        self.begin_time = datetime.now()  # 获得当前时间，设定开始转写的时间
        # print("in Thread init.")
        # self.signal = pyqtSignal(int, str)  # Jet: 可以传递多个信息参数

    # def __del__(self):
    #   self.wait()

    # Jet adds:
    # i: 对应进度条的1-100
    # msg:要在UI显示的信息（从服务器返回的转写过程中的实时信息）
    # def emit_msg(self, i, msg, **kw):  # **kwargs means keyword arguments. et: 没有用上
    def emit_msg(self, i, msg):

        self.signal.emit(i, msg)  # 注意这里的参数需要与上面pyqtSignal定义的一致
        # print("in emit_msg, msg received: ", msg)

    # Jet adds: 此函数中，写完tt文件之后，需要刷新UI显示， 未完成。还是弃用。统一调用JetsXunfeiApi.py中的函数
    """
    def call_xunfei_converting_api_2speakers(self):
        api = JetsXunfeiApi.XunfeiAudioConvertRequestApi(JetsXunfeiApi.APPID, JetsXunfeiApi.SECRET_KEY,
                                                         self.audio_file, speaker_number=2)
        api.set_convert_thread(self)  # 设置刷新进度显示的线程
        result = api.all_api_request()

        # 指定编码格式为UTF-8格式，中英文都可正常存储
        try:
            fw = open(self.raw_txt_file, 'w', encoding='utf-8')  # w为写文件write
            fw.write(str(result))
            msg = "语音转写内容保存到文件:%s成功！" % self.raw_txt_file
            self.emit_msg(100, msg)
        except:
            msg = "语音转写内容保存到文件:%s失败" % self.raw_txt_file
            self.emit_msg(90, msg)
        finally:
            fw.close()
        # 注意，需要调用的函数是1speaker还是2speakers
    """

    def run(self):
        """
        Jet:在此调用函数，根据进展情况emit(i),刷新进度信息及进度条GUI显示,
        具体的刷新coding放到JetsXunfeiApi.py中

        需要根据音频的大小（长度）来估算转写的时间，确定i值（对应进度条的值1-100)
        调用讯飞转写Api，并同步输出服务器转写过程中返回的实时信息，显示到UI
        """
        msg = "Start：调用讯飞转写语音文件：" + self.audio_file
        self.emit_msg(1, msg)

        # self参数传给JetsXunfeiApi,以便在其中函数中调用本类中定义的print_info函数， 打印信息到UI TextBrowser中
        if self.speaker_num == 1:
            print("call xunfei Api with 1 speaker")

            self.is_converting_finished = JetsXunfeiApi.convert_1speaker_audio_to_text_with_gui(self.audio_file,
                                                                                                self.raw_txt_file, self)
            # self传进去，以便用讯飞服务器返回的信息来刷新UI显示信息
        elif self.speaker_num == 2:
            print("call xunfei Api with 2 speakers")

            # Jet： 把self传递到所调用的函数里，以便在此函数中调用emit_msg更新UI
            self.is_converting_finished = JetsXunfeiApi.convert_2speakers_audio_to_text_with_gui(self.audio_file,
                                                                                                 self.raw_txt_file, self)

            # 改为以下方式能正常调用：
            #self.call_xunfei_converting_api_2speakers()

        # 转写完成，需要把线程thread2 时间stop...


    # Jet adds: 获得启动转写线程的时间
    def get_begin_time(self):
        return self.begin_time


# Jet： 子窗口， 用于实时显示转写状态的UI
#class ConvertingDialog(QtWidgets.QWidget):
class ConvertingDialog(QtWidgets.QDialog):

    # Jet: 修改了默认的 def __init__(self):
    def __init__(self, audio_file, raw_txt_file, speaker_num=2):
        super().__init__()

        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)

        # Jet:初始化音频文件、转写原始文本文件的全路径及文件名
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file
        self.speaker_num = speaker_num
        # 估算转写时间，返回分钟
        self.estimated_converting_time = getaudioinfo.calculate_estimated_converting_time(audio_file)
        # print("estimated converting time: ", self.estimated_converting_time)

        # 提醒用户等待，估算转写时间
        self.label = QtWidgets.QLabel('语音转写提示：', self)
        # self.label.move(50, 15)
        self.label.setGeometry(20, 15, 550, 25)
        self.label.setAlignment(Qt.AlignCenter)

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(20, 40, 550, 300)

        # 进度条设置
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(20, 350, 550, 25)
        self.pbar.setValue(0)

        # 提醒用户，已经转写的时间
        self.label2 = QtWidgets.QLabel('转写用时提示：', self)
        self.label2.setGeometry(20, 390, 250, 25)
        self.label2.setAlignment(Qt.AlignCenter)

        # 按钮初始化
        self.button = QtWidgets.QPushButton('点击开始转写...', self)
        # self.button.setToolTip('这是一个 <b>QPushButton</b> widget')
        self.button.resize(self.button.sizeHint())
        self.button.setGeometry(250, 390, 200, 25)

        self.button.clicked.connect(self.start_converting_thread)  # 绑定多线程触发事件

        # 窗口初始化
        self.setGeometry(300, 300, 600, 420)
        self.setWindowTitle('语音转写——实时进度窗口')

        #self.show() #显示

        self.thread1 = None  # 初始化线程
        self.is_converting_finished = False
        self.is_failed = False

    '''
    # Jet adds: 设置调用转写前需要的参数。不用了，还是放在构造函数里
    def set_parameters(self, audio_file, raw_txt_file, speaker_num=2):
        # Jet:初始化音频文件、转写原始文本文件的全路径及文件名
        self.audio_file = audio_file
        self.raw_txt_file = raw_txt_file
        self.speaker_num = speaker_num
        self.estimated_converting_time = audio.getaudioinfo.calculate_estimated_converting_time(
            audio_file)  # 估算转写时间，返回分钟
        print("estimated converting time: ", self.estimated_converting_time)
    '''
    # Jet：重写关闭窗口的函数
    def closeEvent(self, event):
        print("关闭显示转写进度的子窗口")


    # Jet adds: 创建转写的线程并启动
    def start_converting_thread(self):
        #转写完成，则修改按钮文字，不能再转写，以免讯飞重复收费！
        if self.button.text() == "点击开始转写...":
            # 创建线程，包含音频文件及文本文件名（从构造函数传递来的）
            self.thread1 = RunThread(self.audio_file, self.raw_txt_file, self.speaker_num)

            # print("call func: start thread...")
            # 连接信号
            self.thread1.signal.connect(self.update_ui)  # 进程连接回传到GUI的事件

            # 开始线程
            self.thread1.start()

            self.thread2 = TimeThread()
            self.thread2.signal.connect(self.update_time_elapsed)
            self.thread2.start()
            self.button.setText("正在转写中...")
            self.button.setEnabled(False) #禁止用户再点击
        else:
            self.close()
            #self.closeEvent()

    # Jet adds: 刷新UI显示的函数，包括文本框和进度条的显示
    def update_ui(self, i, msg):
        # print("in call_backlog")
        self.label.setText("转写过程大约需要%d分钟。敬请耐心等待！" % self.estimated_converting_time)
        # print("in call_back 2")

        self.pbar.setValue(i)  # 将线程的参数传入进度条
        # print("processbar %d%%. msg:%s" % (i, msg))

        # Jet:自定义的打印函数，把print的信息打印到textBrowser上
        # 参考：https: // blog.csdn.net / weixin_43097265 / article / details / 92830565
        self.textBrowser.append(msg)  # 在指定的区域显示提示信息
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursor.End)  # 光标移到最后，这样就会自动显示出来

        if i == 100:  # 转写完成,修改按钮文字提示
            self.button.setText("转写完成！点击退出...") #
            self.button.setEnabled(True)  # 用户可以再点击
            self.is_converting_finished = True
            return
        if "失败" in msg or "出错" in msg:
            self.button.setText("转写失败！点击退出...")
            self.is_failed = True
            return


    # Jet adds: 刷新当前用时UI （秒数）
    def update_time_elapsed(self, i, msg):
        '''
        now = QDateTime.currentDateTime()
        seconds = start_time.secsTo(now)
        m_time = QTime()
        m_time.setHMS(0, 0, 0, 0) # 初始化数据，时分秒毫秒
        # 计算时间差(秒)，将时间差加入m_time，格式化输出
        m_time.addSecs(seconds) #这里显示不对！，还是0! 于是不用这种办法，改用下面的办法
        time_elapsed = m_time.elapsed()
        #time_elapsed = m_time.toString("hh:mm:ss")
        '''
        # 判断是否已经完成或中途失败，没完成才继续显示最新时间
        if self.is_converting_finished or self.is_failed:
            #print("stop counting time.")
            #self.thread1.exit()  # 停止线程，会死！
            return
        else:
            now = datetime.now()  # 获得当前时间
            start_time = self.thread2.begin_time
            seconds = (now - start_time).seconds

            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)

            time_elapsed = "转写已经用时： %d:%02d:%02d" % (h, m, s)

            # print(time_elapsed)
            self.label2.setText(time_elapsed)

        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿
        # print("end call_backlog")


# Jet: 自定义main函数
def main():
    # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    app = QtWidgets.QApplication(sys.argv)
    # Jet: 指定转写需要的参数
    # audio_file = r"D:\Jet's Docs\Jet 常用文档-Asus\#2-2020 Ministry\James-雅各书-讲章\6-21 雅1：1-8 主日.mp3"
    # raw_txt_file = r"D:\Jet's Docs\Jet 常用文档-Asus\#2-2020 Ministry\James-雅各书-讲章\6-21 雅1：1-8 主日_raw.txt"

    # audio_file = r"F:\Jet Python Study\PyCharmProjects\icf-audio2text\src\audio\2020-0622-Tanche-活出真我的动力-教练环节.mp3"
    # audio_file = r"G:\Jet Python Study\PyCharmProjects\icf-audio2text\src\audio\2020-0622-Tanche-活出真我的动力-教练环节.mp3"

    audio_file = r"F:\Jet Python Study\PyCharmProjects\icf-audio2text\src\audio\06-教练秀-婚恋的困惑.mp3"
    # audio_file = r"F:\Jet Python Study\PyCharmProjects\icf-audio2text\src\audio\06-教练秀-婚恋的困惑_片断.mp3"
    raw_txt_file = audio_file + "_raw.txt"
    speaker_num = 2
    my_converting_gui = ConvertingDialog(audio_file, raw_txt_file, speaker_num)

    # my_converting_gui = ConvertingDialog()
    # my_converting_gui.set_parameters(audio_file, raw_txt_file, speaker_num)

    my_converting_gui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
