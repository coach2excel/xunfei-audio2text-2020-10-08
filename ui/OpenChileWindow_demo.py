
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#成功

'''
模式对话框 与 非模式对话框 （modeless dialog | modal dialog）

模式对话框，就是在弹出窗口的时候，整个程序就被锁定了，处于等待状态，直到对话框被关闭。这时往往是需要对话框的返回值进行下面的操作。如：确认窗口（选择“是”或“否”）。
非模式对话框，在调用弹出窗口之后，调用即刻返回，继续下面的操作。这里只是一个调用指令的发出，不等待也不做任何处理。如：查找框。

show() ------  modeless dialog

exec() ------- modal dialog
————————————————
版权声明：本文为CSDN博主「jianglz-gz」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_40520077/article/details/104040414
'''
class FirstWindow(QWidget):

    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(FirstWindow, self).__init__(parent)
        self.resize(100, 100)
        self.btn = QToolButton(self)
        self.btn.setText("click")

        #Jet: 需要判断是否已经针对当前音频做过原始转换，以避免重复提交，重复被讯飞收费！
        #to Do...


    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()


class SecondWindow(QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(200, 200)
        self.setStyleSheet("background: black")

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    s = SecondWindow()
    ex.btn.clicked.connect(s.handle_click)
    ex.btn.clicked.connect(ex.hide)
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())