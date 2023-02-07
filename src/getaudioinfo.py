# 获取指定音频的信息（特别是时长）

import wave  # pip install wave
import contextlib
from mutagen.mp3 import MP3  # pip install mutagen

# 获取更多wav信息，参见：https://blog.csdn.net/u010070526/article/details/85218613
# 例如：画出波形图

mp3file = r"G:\Jet Python Study\PyCharmProjects\icf-audio2text\audio\2020-0622-Tanche-活出真我的动力-教练环节.mp3"
wavfile = r"G:\Jet Python Study\PyCharmProjects\icf-audio2text\audio\JetCoachDeng-Sample-6m.wav"

# 返回音频时长的秒数
def get_wav_length(filename):
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = int(frames / float(rate))
        print(filename + " duration time: " + str(duration))

    return duration


# 返回音频时长的秒数
def get_mp3_length(filename):
    audio = MP3(filename)
    duration = int(audio.info.length)
    print(filename + " duration time: " + str(duration))
    return audio.info.length


# 获取指定音频mp3/wav的时长，返回秒数
# 用途： 用于后续转写过程时估算所需时间，或用于播放音频指定位置
def get_audio_time_seconds(audio_file):
    duration_time = 0  # Jet： 这里得先定义，否则运行时会出错！因为以下两个if可能存在都不成立的情况！
    if audio_file.endswith("mp3"):
        duration_time = get_mp3_length(audio_file)
    elif audio_file.endswith("wav"):
        duration_time = get_wav_length(audio_file)
    return int(duration_time)


# 获取指定音频mp3/wav的时长，返回分钟数
# 用途： 用于后续转写过程时估算所需时间
def get_audio_time_length(audio_file):
    duration_time = 0  # Jet： 这里得先定义，否则运行时会出错！因为以下两个if可能存在都不成立的情况！
    if audio_file.endswith("mp3"):
        duration_time = int(get_mp3_length(audio_file) / 60)
    elif audio_file.endswith("wav"):
        duration_time = int(get_wav_length(audio_file) / 60)
    return duration_time


# Jet: 估算转写时间，60分钟的音频按20分钟计算,相当于1分钟需要等待20秒，
# 可能估算得太长了，经过实际测试，再改动（跟网络速度有关）
def calculate_estimated_converting_time(audio_file):
    duration_time = get_audio_time_length(audio_file)
    converting_time = int(duration_time / 3)
    return converting_time


def main():
    get_wav_length(wavfile)
    get_mp3_length(mp3file)


if __name__ == "__main__":
    main()
