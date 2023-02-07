#https://blog.csdn.net/qq_45414559/article/details/105560090

'''

Jet:无法运行！

快速美化PyQt–QcureUi
QcureUi
快速美化PyQt应用
项目地址(欢迎star):https://github.com/Amiee-well/cureUi
使用方法
pip install QcureUi

调用QcureUi.cure.Windows()

共有五个参数填写：

1.第一个参数为QWidget面板类（必填）

2.第二个参数为托盘名字（必填）

3.第三个参数为选择美化颜色面板（选填，默认为default）

现已有参数为：blue，blueDeep，blueGreen，pink四种

该参数为True时将随机从已有颜色库返回其一

4.第四个参数为窗口名字（选填，默认为QCureWindow）

5.第五个参数为窗口图标（选填，默认为空）

注意事项
注意:托盘图标默认名称为icon.jpg,改变该图标可在运行目录下放置该图片
————————————————
版权声明：本文为CSDN博主「꧁༺北海以北的等待༻꧂」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_45414559/article/details/105560090
'''
from QcureUi import cure
app = QApplication(sys.argv)
win = cure.Windows(Examples(), "tray name", True, "program name", "myicon.ico")
sys.exit(app.exec_())

