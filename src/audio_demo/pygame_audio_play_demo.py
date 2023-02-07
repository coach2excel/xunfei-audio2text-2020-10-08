import time
import pygame
#Jet: 没有成功！

#audio_file =r"D:\Jet's Docs\Jet 常用文档-Asus\#2-教练\AI-Coaching\AI语音转写-AI Coaching\AI-Coaching-PyCharmProject\audio\2020-0605-教练梦瑶-画大饼的思维.mp3" #Jet: 不支持mp3格式！
#audio_file = r"/audio/2020-0605-教练梦瑶-画大饼的思维.wav"  #Jet: 不支持mp3格式！
audio_file =r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.mp3"
#audio_file =r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.wav"

#Jet： 能播放，但是声音严重扭曲了，吓人！！！

pygame.init()
pygame.mixer.init()
pygame.display.set_mode([0,0]) #不能播放声音， 加上这句就好了，这是加载界面的意思。

print("播放音乐1")
track = pygame.mixer.music.load(audio_file)
start_time = 64450/1000 #13760
pygame.mixer.music.play()
#pygame.mixer.music.play(loops=0, start=start_time)
time.sleep(10)
pygame.mixer.music.stop()



'''
pygame.init() 进行全部模块的初始化，
pygame.mixer.init() 或者只初始化音频部分
pygame.mixer.music.load('xx.mp3') 使用文件名作为参数载入音乐 ,音乐可以是ogg、mp3等格式。载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取。
pygame.mixer.music.play()播放载入的音乐。该函数立即返回，音乐播放在后台进行。
play方法还可以使用两个参数
pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
pygame.mixer.music.stop() 停止播放，
pygame.mixer.music.pause() 暂停播放。
pygame.mixer.music.unpause() 取消暂停。
pygame.mixer.music.fadeout(time) 用来进行淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。
pygame.mixer.music.set_volume(value) 来设置播放的音量，音量value的范围为0.0到1.0。
pygame.mixer.music.get_busy() 判断是否在播放音乐,返回1为正在播放。
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1) 在音乐播放完成时，用事件的方式通知用户程序，设置当音乐播放完成时发送pygame.USEREVENT+1事件给用户程序。 pygame.mixer.music.queue(filename) 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。一次只能指定一个等待播放的音乐文件。
————————————————
版权声明：本文为CSDN博主「huazwz」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/huazwz/article/details/80505091
'''
