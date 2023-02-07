import os, time
import vlc

# 2020/07/02 测试成功
class VlcPlayer:
    '''
        args:设置 options
    '''
    def __init__(self, *args):
        if args:
            instance = vlc.Instance(*args)
            self.media = instance.media_player_new()
        else:
            self.media = vlc.MediaPlayer()

    # 设置待播放的url地址或本地文件路径，每次调用都会重新加载资源
    def set_uri(self, uri):
        self.media.set_mrl(uri)

    # 播放 成功返回0，失败返回-1
    def play(self, path=None):
        if path:
            self.set_uri(path)
            return self.media.play()
        else:
            return self.media.play()

    # 暂停
    def pause(self):
        self.media.pause()

    # 恢复
    def resume(self):
        self.media.set_pause(0)

    # 停止
    def stop(self):
        self.media.stop()

    # 释放资源
    def release(self):
        return self.media.release()

    # 是否正在播放
    def is_playing(self):
        return self.media.is_playing()

    # 已播放时间，返回毫秒值
    def get_time(self):
        return self.media.get_time()

    # 拖动指定的毫秒值处播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_time(self, ms):
        #return self.media.get_time() # Jet: 这个函数不对！
        return self.media.set_time(ms)  #Jet：自己改的


    # 音视频总长度，返回毫秒值
    def get_length(self):
        return self.media.get_length()

    # 获取当前音量（0~100）
    def get_volume(self):
        return self.media.audio_get_volume()

    # 设置音量（0~100）
    def set_volume(self, volume):
        return self.media.audio_set_volume(volume)

    # 返回当前状态：正在播放；暂停中；其他
    def get_state(self):
        state = self.media.get_state()
        if state == vlc.State.Playing:
            return 1
        elif state == vlc.State.Paused:
            return 0
        else:
            return -1

    # 当前播放进度情况。返回0.0~1.0之间的浮点数
    def get_position(self):
        return self.media.get_position()

    # 拖动当前进度，传入0.0~1.0之间的浮点数(需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_position(self, float_val):
        return self.media.set_position(float_val)

    # 获取当前文件播放速率
    def get_rate(self):
        return self.media.get_rate()

    # 设置播放速率（如：1.2，表示加速1.2倍播放）
    def set_rate(self, rate):
        return self.media.set_rate(rate)

    # 设置宽高比率（如"16:9","4:3"）
    def set_ratio(self, ratio):
        self.media.video_set_scale(0)  # 必须设置为0，否则无法修改屏幕宽高
        self.media.video_set_aspect_ratio(ratio)

    # 注册监听器
    def add_callback(self, event_type, callback):
        self.media.event_manager().event_attach(event_type, callback)

    # 移除监听器
    def remove_callback(self, event_type, callback):
        self.media.event_manager().event_detach(event_type, callback)


#从指定位置播放，这种播放有误差，跟下一个函数差不多
def demo_2(start_time_mm):
    #url = "file:///home/rolf/GWPE.mp4"
    url = r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.mp3"

    playing = set([1, 2, 3, 4])
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(url)
    start_time = 'start-time='+"{:.2f}".format(start_time_mm/1000)
    print(start_time)
    media.add_option(start_time)  # 600 seconds (10 minutes)
    player.set_media(media)
    player.play()
    time.sleep(0.1)  # wait briefly for it to start
    while True:
        state = player.get_state()
        if state not in playing:
            break

#从指定位置播放，这种播放误差逐渐拉大，从几秒到1分钟（1小时的录音）
def demo_1(start_time_mm):
    audio_file = r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.mp3"

    player = VlcPlayer()
    player.set_uri(audio_file)
    #player.add_callback(vlc.EventType.MediaPlayerTimeChanged, my_call_back)

    player.play()#必须先播放，
    time.sleep(0.01)#稍微停一下
    player.set_time(start_time_mm) #从指定毫秒处播放
    player.play()
    time.sleep(29)
    player.stop()


    # 播放本地mp3
    # player.play("D:/abc.mp3")

    # 防止当前进程退出
    while True:
        pass

#def my_call_back(event):
   # print("call:", player.get_time())

if "__main__" == __name__:
    #demo_1(110960)#实际播放滞后到100500，相差10’
    #demo_2(2031430)  # 实际播放滞后到1984000 相差47'
    demo_2(1801080)
    #demo_1(2508780) # 2479600  相差29’
    #demo_1(3073220)#实际播放滞后到3046000，相差30‘

'''
————————————————
版权声明：本文为CSDN博主「fleaxin」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fleaxin/article/details/101943941
'''