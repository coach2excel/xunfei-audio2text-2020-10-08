from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QGridLayout
import sys

#调用vlc播放
import vlc  #需要事先安装VLC,注意版本
'''
安装并下载
pip3 install python-vlc

安装完成之后在你python的site-packages目录之下找到vlc.py这个VLC脚本
PS：如果你电脑上安装了VLC的话通过这个脚本可以直接调用VLC进行播放。
因为我们的程序不可能要求用户在自己电脑上先安装上VLC那样的话，如果你写的一个播放器软件，却要求用户先安装VLC那不是在开国际玩笑吗？
可以直接调用你项目目录之下的libvlc.dll进行播放不需要单独安装VLC
因此我们需要下载VLC绿色版本解压出我们需要的DLL文件下载地址如下：
http://download.videolan.org/pub/videolan/vlc/

下载时“一定”要下载对应的版本，看清楚自己的系统是多少位的，到时候如果打包的话，也要放入相应版本的DLL文件，最好pip list看一下，python-vlc的版本。下载7z绿色版本之后，解压出来的文件有很多，我们只需要三个文件分别是
libvlc.dll
libvlccore.dll
plugins（这是一个目录）

好了！！！至此，所有需要的文件就都下载完成，一共四个分别是
vlc.py
libvlc.dll
libvlccore.dll
plugins（这是一个目录）
把这四个文件或目录，放在你的项目根目录当中

作者：leixiaozeng
链接：https://www.jianshu.com/p/5bf7f10c1a32
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

import platform

#播放mp3, wav成功

#audio_file =r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.mp3"
audio_file =r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.wav"


class MainUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

        self.init_ui()
    # test mp3
    '''
    def init_ui(self):
        button1 = QtWidgets.QPushButton("button1",self)
        button1.clicked.connect(self.playmusic)
        url = QUrl.fromLocalFile(mp3_file)
        content = QtMultimedia.QMediaContent(url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        button1.clicked.connect(self.playmusic)
    '''
    def init_ui(self):
        button1 = QtWidgets.QPushButton("button1",self)
        button1.clicked.connect(self.playmusic)
        button1.clicked.connect(self.playmusic)

    def playmusic(self):
        #self.player.play()  #mp3
        url = audio_file
        self.mediaplayer.set_mrl(url)
        self.mediaplayer.play()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
