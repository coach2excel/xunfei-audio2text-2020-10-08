from PyQt5 import QtCore
from PyQt5.QtWidgets import *
#自定义控件：带搜索功能的输入下拉框
#圆角文本框： line 187 ff.
#https://blog.csdn.net/weixin_44152831/article/details/89487533

#自定义文本输入框
class CustomEdit(QLineEdit):
    """
    带下拉框的文本输入框类（文本下拉输入框），输入文字可以搜索内容
    """
    def __init__(self, parent, size=(50, 50, 100, 20), name='edit',
                 drag=False, text_list=True, search=True, qss_file=''):
        """
        初始化控件
        :param parent: 控件显示的父对象
        :param size: 输入框控件尺寸
        :param name: 输入框控件名称
        :param drag: 拖放标识位
        :param text_list: 是否开启下拉框功能标识位
        """
        super(CustomEdit, self).__init__(None, parent)
        # 输入框的尺寸
        self.w = size[2]
        self.h = size[3]
        self.setGeometry(*size)
        # 输入框名称
        self.setObjectName(name)
        # 输入框是否支持拖放
        self.drag_flag = False
        if drag:
            self.setAcceptDrops(True)
            self.setDragEnabled(True)  # 开启可拖放事件
        else:
            self.setAcceptDrops(False)
            self.setDragEnabled(False)  # 关闭可拖放事件

        self.click_flag = False  # 点击状态，为False时显示下拉框
        self.text_list = None  # 下拉框对象
        self.p_text = ""    # placehold text，输入框背景上的灰色文字
        self.qss_file = qss_file  # 下拉框样式文件
        self.org_data = []  # 用来进行搜索的数据list



        # 如果text_list为True，则初始化下拉框
        if text_list:
            # 下拉列表模型为StringListModel
            self.list_model = QtCore.QStringListModel()
            # 初始化下拉列表对象为QListView类型
            self.text_list = QListView(parent)
            # 下拉列表名称，以list_开头
            self.text_list.setObjectName("list_%s" % name)
            # 设置下拉列表初始化尺寸
            self.text_list.setGeometry(size[0], size[1]+size[3], size[2], size[3])
            # 隐藏下拉列表
            self.text_list.hide()
            # 初始化下拉列表数据
            self.text_list.data = []

        # 点击下拉框列表元素，绑定消息响应函数
        self.func = None
        self.text_list.clicked.connect(lambda: self.on_select_data(self.func))

        if search:
            self.textChanged.connect(self.on_search_data)

    def on_search_data(self):
        """
        文本变化时的消息响应，搜索下拉框列表里的数据
        """
        # 输入框中文本和List选择文本不一样的时候，才显示下拉框
        cur_text = self.text()
        list_text = ''
        idx = self.text_list.currentIndex()
        if self.text_list.data:
            list_text = self.text_list.data[idx.row()]
        if cur_text != list_text:  # and len(cur_text) > 1:
            self.text_list.show()

        # 根据消息响应传入的data来搜索
        self.text_list.data = self.org_data[:]
        for _text in self.org_data:
            if cur_text not in _text:
                self.text_list.data.remove(_text)
        # 刷新下拉框
        self.list_model.setStringList(self.text_list.data)
        self.text_list.setModel(self.list_model)

        if not self.click_flag:
            self.text_list.hide()
            self.click_flag = True
        if self.text_list.data:  # 有数据的时候就调整下拉框大小
            self.text_list.resize(self.w, self.h * 0.6 * len(self.text_list.data))
        else:
            self.text_list.hide()  # 没有数据就隐藏下拉框


    def fill_data(self, text_data_list):
        """
        初始化文本下拉输入框控件数据
        :param text_data_list: 下拉框数据，必须为纯文本list
        """
        # 设置下拉列表数据
        self.list_model.setStringList(text_data_list)
        self.text_list.setModel(self.list_model)
        self.text_list.data = text_data_list
        # 填充list数据
        if text_data_list:
            self.text_list.data = text_data_list
            self.org_data = text_data_list[:]  # 深拷贝一份数据，用来搜索
            self.text_list.resize(self.w, self.h * 0.6 * len(self.text_list.data))
            self.setText(text_data_list[0])
        else:
            self.setText('')
        self.text_list.hide()

    edit_clicked = QtCore.pyqtSignal()  # 定义clicked信号

    def mouseReleaseEvent(self, event):
        """
        鼠标按键松开时的事件处理
        :param event: 鼠标按键松开事件
        """
        # 左键松开
        if event.button() == QtCore.Qt.LeftButton:
            # 下拉列表存在数据，并且未点击过，则显示下拉框
            if self.text_list.data and not self.click_flag:
                self.text_list.show()
            # 下拉列表存在，并且点击过，则隐藏下拉框
            elif self.click_flag:
                self.text_list.hide()
            self.click_flag = not self.click_flag
            self.edit_clicked.emit()  # 发送clicked信号

    def on_select_data(self, func):
        """
        选择下拉框数据时的消息响应函数
        """
        text = ''
        idx = self.text_list.currentIndex()
        if self.text_list.data:
            text = self.text_list.data[idx.row()]
        self.text_list.hide()
        self.setText(text)
        self.setFocus()
        self.setCursorPosition(len(text))
        # 选择数据后就隐藏了下拉框，设置点击标识位为False，下次点击才会显示下拉框
        self.click_flag = False
        if func:
            func()




class MainWindow(QMainWindow):
    """主窗口，继承了QMainWindow类"""
    def __init__(self, name, title):
        """初始化类的成员变量"""
        super(MainWindow, self).__init__()
        self.w = 0
        self.h = 0
        self.init_ui(name, title)  # 初始化UI界面

    def init_ui(self, name, title):
        """初始化UI界面"""
        self.w = 140
        self.h = 100

        self.setObjectName(name)  # 设置主窗口对象的名称
        self.setWindowTitle(title)  # 设置主窗口显示的标题
        self.resize(self.w, self.h)  # 设置主窗口尺寸

        #self.custom_edit = CustomEdit(self, size=(10, 10, 120, 24),
        #        name='custom_edit', search=False)
        self.custom_edit = CustomEdit(self, size=(10, 10, 120, 24),
                                      name='custom_edit', search=True)

        self.custom_edit.setPlaceholderText('我是自定义输入框')



        data_list = [i * ('%s' % i) for i in range(15)]
        self.custom_edit.fill_data(data_list)

        self.setStyleSheet('QMainWindow{background:white}')
        # 设置圆角文本框
        edit_style = '''
                 QLineEdit{
                     border:1px solid gray;
                     width:100px;
                     border-radius:10px;
                     padding:2px 4px;
                     background: pink;
                     color: purple;
                 }
                 '''
        self.custom_edit.setStyleSheet(edit_style)

        pad = 2
        per_h = 16
        max_h = self.h - 40
        list_style = '''
                 QListView{
                     border: 1px solid gray;
                     min-width: 100px;
                     max-width: %spx;
                     max-height: %spx;
                     background-color: yellow;
                     border-radius:10px;
                 }
                 QListView::item{
                     padding-bottom: %spx;
                     min-height: %spx;
                     border-bottom: 1px solid gray;
                 }
                 ''' % (self.w, max_h, pad, per_h)
        self.custom_edit.text_list.setStyleSheet(list_style)
        list_h = (pad + per_h + 2) * len(data_list)
        list_h = min(max_h, list_h)
        self.custom_edit.text_list.setFixedSize(120, list_h)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    n = 'CustomUI'
    t = '自定义控件'
    ex = MainWindow(n, t)
    ex.show()
    sys.exit(app.exec_())
