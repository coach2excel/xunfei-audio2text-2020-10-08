import os, time
import vlc  # pip install python-vlc
#在Windows系统上，vlc.py是通过查询Windows注册表的方式来搜索路径并加载VLC的dll动态库的。
# 但它其中也提供了一个配置环境变量PYTHON_VLC_MODULE_PATH的加载方式，这样我们就能在尽可能不修改vlc.py源码的前提下完成VLC动态库的集成。
# https://blog.csdn.net/yingshukun/article/details/89527561
# 官方文档： https://www.olivieraubert.net/vlc/python-ctypes/doc/
# VLC参数详解： https://blog.csdn.net/avsuper/article/details/80145439
# 2020/07/02 Jet 测试成功, Remix


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

    # 拖动指定的毫秒值处，即开始播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_time(self, ms):
        self.media.play()  # 必须先播放，
        time.sleep(0.01)  # 稍微停一下
        result = self.media.set_time(ms)  #Jet：自己改的
        #self.media.stop()  #有此句反而不会在指定ms播放

        return result

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

    # 注册监听器，可理解为信号函数
    # https://blog.csdn.net/yingshukun/article/details/89527561
    def add_callback(self, event_type, callback):
        '''
        VLC 监听器
        上面代码中，我们注册了MediaPlayerTimeChanged类型的监听器，表示已播放时间变化时回调，可以看到my_call_back会不断回调，因为每播放一点都会回调。

        除了上述的监听器，VLC的监听器实际上非常多，常见的我们列举如下：

        # ***Jet： 在连接信号和槽函数时判断信号类型

        MediaPlayerNothingSpecial：vlc处于空闲状态，只是等待发出命令
        MediaPlayerOpening：vlc正在打开媒体资源定位器（MRL）
        MediaPlayerBuffering（int cache）：vlc正在缓冲
        MediaPlayerPlaying：vlc正在播放媒体
        MediaPlayerPaused：vlc处于暂停状态
        MediaPlayerStopped：vlc处于停止状态
        MediaPlayerForward：vlc通过媒体快进（这永远不会被调用）
        MediaPlayerBackward：vlc正在快退（这永远不会被调用）
        MediaPlayerEncounteredError：vlc遇到错误，无法继续
        MediaPlayerEndReached：vlc已到达当前播放列表的末尾
        MediaPlayerTimeChanged：时间发生改变
        MediaPlayerPositionChanged：进度发生改变
        MediaPlayerSeekableChanged：流媒体是否可搜索的状态发生改变（true表示可搜索，false表示不可搜索）
        MediaPlayerPausableChanged：媒体是否可暂停状态发生改变（true表示可暂停，false表示不可暂停）
        MediaPlayerMediaChanged : 媒体发生改变
        MediaPlayerTitleChanged: 标题发生改变（DVD/Blu-ray）
        MediaPlayerChapterChanged :章节发生改变（DVD/Blu-ray）
        MediaPlayerLengthChanged :(在vlc版本<2.2.0仅适用于Mozilla）长度已更改
        MediaPlayerVout :视频输出的数量发生改变
        MediaPlayerMuted :静音
        MediaPlayerUnmuted :取消静音
        MediaPlayerAudioVolume :音量发生改变
        ————————————————
        版权声明：本文为CSDN博主「血色v残阳」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
        原文链接：https://blog.csdn.net/yingshukun/article/details/89527561
            '''
        self.media.event_manager().event_attach(event_type, callback)
        #self.media.event_manager().event_attach(vlc.EventType.MediaPlayerTimeChanged, callback)
        #self.media.event_manager().event_attach(vlc.EventType.MediaPlayerPlaying, callback)


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



vlc_player = VlcPlayer()

def call_back_time_changed(event):
   print("call:", vlc_player.get_time())


#从指定位置播放，这种播放误差逐渐拉大，从几秒到1分钟（1小时的录音）
def demo_1(start_time_mm):
    audio_file = r"F:\Jet Python Study\Xunfei语音转写_Jet's Audio & Txt\2010-06-02-coach 谭澈zoom.mp3"

    #vlc_player = VlcPlayer()
    vlc_player.set_uri(audio_file)
    vlc_player.add_callback(vlc.EventType.MediaPlayerTimeChanged, call_back_time_changed)

    #用以下
    #vlc_player.play()#必须先播放，
    #time.sleep(0.01)#稍微停一下
    vlc_player.set_time(start_time_mm) #从指定毫秒处播放
    #vlc_player.stop()
    #vlc_player.play()

    #只播放一会儿就停下
    time.sleep(5)
    vlc_player.stop()

    # 防止当前进程退出
    while True:
        pass

if "__main__" == __name__:
    #demo_2(110960)#实际播放滞后到100500，相差10’
    demo_1(110960)  # 实际播放滞后到100500，相差10’

    #demo_2(2031430)  # 实际播放滞后到1984000 相差47'
    #demo_2(1801080) #沉默一段时间才会有声音
    #demo_1(2508780) # 2479600  相差29’
    #demo_1(3073220)#实际播放滞后到3046000，相差30‘

'''
————————————————
版权声明：本文为CSDN博主「fleaxin」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fleaxin/article/details/101943941
'''