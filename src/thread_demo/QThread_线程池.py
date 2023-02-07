# -*- coding: utf-8 -*-
"""
Jet:此例无法运行，可参考框架
代码的核心含义是以一条线程 管理着线程池，线程池再统一管理着其他线程。
@Desc:
https://blog.csdn.net/weixin_38587278/article/details/106430250?utm_medium=distribute.pc_relevant_ask_down.none-task-blog-baidujs-1.nonecase&depth_1-utm_source=distribute.pc_relevant_ask_down.none-task-blog-baidujs-1.nonecase
"""
from PyQt5.QtCore import QThread, QThreadPool, pyqtSignal, QObject, QRunnable


class HnQtPoolThread(QThread):
    '''
    线程池线程，用于管理线程池
    '''

    def __init__(self):
        super().__init__()
        self.threadpool = HnQTThreadPool()

    def run(self):
        '''
        启动线程池
        '''
        self.threadpool.Start()

    def addThread(self, _thread):
        self.threadpool.addThread(_thread)


class HnQTThreadPool():
    '''
        线程池
    '''
    thread_list = []

    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.threadpool.globalInstance()
        # Jet: 以下tool不知在哪里定义的！
        poolnum = tool.loadJsons(tool.setting_address)[0]['pool_num']
        self.threadpool.setMaxThreadCount(int(poolnum))

    def addThread(self, _thread):
        self.thread_list.append(_thread)

    def Start(self):
        for i in self.thread_list:
            self.threadpool.start(i)
        self.threadpool.waitForDone()
        self.thread_list.clear()


class HnSignal(QObject):
    progress_signal = pyqtSignal(int)
    result_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()


class HnThreadForExcel_Argv(QRunnable):
    '''
        为Excel生成提供PYQT线程类
    '''

    def __init__(self, _suplier, dfs, _before_date, _after_date, _Hnsignal=None):
        super().__init__()
        self._suplier = _suplier
        self.fs = dfs
        self._before_date = _before_date
        self._after_date = _after_date
        self.signal = _Hnsignal
        self.setAutoDelete(True)

    def run(self):
        ...
        # 各种方法

    def __del__(self):
        pass


if __name__ == '__main__':
    poolthread = HnQtPoolThread()  # 线程管理线程池
    # Jet: 以下多个变量不知在何处定义的！
    for i in items:  # PyQt的Table类
        if count % 2 == 0:
            threadsignal = HnSignal()  # PyQt5继承QObject
            thfs = fs
            mbedate = before_date
            mafdate = after_date
            ###为线程创建副本
            mythread = HnThreadForExcel_Argv(i.text(), thfs, mbedate, mafdate, threadsignal)
            threadsignal.progress_signal.connect(progress_bar_callback)
            threadsignal.result_signal.connect(message_call_back)
            try:
                pool.poolthread.addThread(mythread)
            except Exception as e:
                print(e.with_traceback())
        count += 1
    poolthread.start()