from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
import PyQt5
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl

import time

#Jet: 播放mp3,wav OK

mp3_file =r"D:\Jet's Docs\Jet 常用文档-Asus\#2-教练\AI-Coaching\AI语音转写-AI Coaching\AI-Coaching-PyCharmProject\audio\唯恒-张瑾-MCC-对话1.mp3"
wav_file =r"D:\Jet's Docs\Jet 常用文档-Asus\#2-教练\AI-Coaching\AI语音转写-AI Coaching\AI-Coaching-PyCharmProject\audio\2020-0605-教练梦瑶-画大饼的思维.wav"
Sound_level =100#太小声可能听不见！

app = PyQt5.QtWidgets.QApplication(sys.argv)
url = PyQt5.QtCore.QUrl.fromLocalFile(mp3_file)
content = PyQt5.QtMultimedia.QMediaContent(url)
player = PyQt5.QtMultimedia.QMediaPlayer()
player.setMedia(content)
player.setVolume(Sound_level)
print("play mp3")
player.play()

time.sleep(10)
print("play wav")
sound = PyQt5.QtMultimedia.QSound(wav_file)
sound.play()

sys.exit(app.exec())

