from PyQt5.QtWidgets import *
import sys


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        button = QPushButton("弹出子窗", self)
        button.clicked.connect(self.show_child)
        self.windowlist = []

    def show_child(self):
        child_window = Child()
        self.windowlist.append(child_window)  # Jet:加上这条就不会闪了
        #child_window.showNormal()  #Jet: 一闪而过！
        #child_window.show() #Jet: 一闪而过！
        child_window.exec_()
        #child_window.exec()   # Jet：运行时错误：AttributeError: 'Child' object has no attribute 'exec'


#class Child(QWidget):
class Child(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是子窗口啊")


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()
    #window.show_child()

    sys.exit(app.exec_())

"""
————————————————
版权声明：本文为CSDN博主「jianglz - gz」的原创文章，遵循CC
4.0
BY - SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https: // blog.csdn.net / weixin_40520077 / article / details / 104040414
"""