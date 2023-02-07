#Jet:这是核心代码，不能运行的。

class Example(QThread):
    signal = pyqtSignal(str)    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # 进行任务操作
        msg ="this is msg in Thread"
        print("emit signal.")
        self.signal.emit(msg)    # 发射信号


# UI类中
def buttonClick(self):
    self.thread = Example()
    self.thread.signal.connect(self.callback)
    print("thread start...")
    self.thread.start()    # 启动线程
    print("after thread start...")

def callback(self, msg):
    print("call back. display msg from Thread:", msg)
    #Jet： to update UI
    #pass

if __name__ == "__main__":
    e = Example()

'''
————————————————
版权声明：本文为CSDN博主「新安浅滩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hu694028833/article/details/80977302
'''