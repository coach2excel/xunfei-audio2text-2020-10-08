from PyQt5.QtWidgets import *
import sys

#子窗口为模式窗口
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        button = QPushButton("弹出子窗", self)
        button.clicked.connect(self.show_child)

    def show_child(self):
        child_window = Child()
        child_window.exec() #子窗口为模式窗口


class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("我是子窗口啊")


# 运行主窗口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec_())