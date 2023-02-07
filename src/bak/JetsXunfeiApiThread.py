# -*- coding: utf-8 -*-
#  Jet: 没有改写完成，暂时不用！因为把线程放进去代码比较复杂了，不如分开到不同的文件里。
#
# 语音转文字
# 非实时转写调用demo

import base64
import hashlib
import hmac
import json
import os
import time
import requests
import getaudioinfo  # 特别注意：这是Jet自定义，获取音频文件时长，在audio文件夹下的getaudioinfo.py
from PyQt5 import QtCore
from PyQt5.QtCore import *


#audio_file = r"C:\Jet's Docs\Jet 常用文档-Asus\#1-STEAM编程教育\#1-大陆JH学校编程培训项目\#1-编程培训项目文档\2020-Moodle在线课程录制\Introduction\0" \
#             r".0-课程介绍v.1.mp3 "

class SliceIdGenerator:
    """slice id生成器"""

    def __init__(self):
        self.__ch = 'aaaaaaaaa`'

    def getNextSliceId(self):
        ch = self.__ch
        j = len(ch) - 1
        while j >= 0:
            cj = ch[j]
            if cj != 'z':
                ch = ch[:j] + chr(ord(cj) + 1) + ch[j + 1:]
                break
            else:
                ch = ch[:j] + 'a' + ch[j + 1:]
                j = j - 1
        self.__ch = ch
        return self.__ch

# Jet:设置讯飞相关的全局变量
# 讯飞服务器网址
lfasr_host = 'http://raasr.xfyun.cn/api'

# Jet从讯飞申请到的：(会根据转换的小时数收费的，有5小时的免费试用
APPID = "5ae46872"
SECRET_KEY = "29333cff087134935d8c43b7443fac38"

# 请求的接口名
api_prepare = '/prepare'
api_upload = '/upload'
api_merge = '/merge'
api_get_progress = '/getProgress'
api_get_result = '/getResult'
# 文件分片大小10M
file_piece_sice = 10485760

# ——————————————————转写可配置参数————————————————
# 参数可在官网界面（https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html）查看，根据需求可自行在gene_params方法里添加修改
# 转写类型
lfasr_type = 0
# 是否开启分词
has_participle = 'false'
has_seperate = 'true'
# 多候选词个数
max_alternatives = 0
# 子用户标识
suid = ''

# 原名RequestApi
#class XunfeiAudioConvertRequestApiThread(object):
class XunfeiAudioConvertRequestApiThread(QtCore.QThread):

    #  通过类成员对象定义信号对象
    # Jet 自定义:
    # int:数字信息,对应进度条1-100
    # str: 获取来自讯飞服务器的提示信息，字符串信息，用于显示在文本框中
    # _signal = pyqtSignal(int, str)  # Jet: 可以传递多个信息参数
    signal = pyqtSignal(int, str) # Jet: 可以传递多个信息参数

    '''
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
    '''
    audio_file_time_length: int

    # Jet：修改
    def __init__(self, audio_file, raw_txt_file, speaker_number=1, has_gui=False):

        print("0: in XunfeiAudioConvertRequestApi __init__")

        super(XunfeiAudioConvertRequestApiThread, self).__init__() # Jet: 父线程
        print("1: in XunfeiAudioConvertRequestApi __init__")

        self.appid = APPID
        self.secret_key = SECRET_KEY

        self.audio_file = audio_file
        # Jet adds:
        self.raw_txt_file = raw_txt_file
        self.speaker_number = speaker_number  # 转写语音中讲话人的个数，默认是1个
        self.estimated_converting_time = getaudioinfo.calculate_estimated_converting_time(audio_file) #估算转写时间，返回分钟


        # self.print_dialog = print_dialog #用于显示信息到UI, XunfeiConvertingDialog的对象

        self.cur_process = 0  # Jet adds: 0-100，对应UI进度条
        self.slice = 1  # Jet adds: 默认上传分割数量为1，即<10M的文件
        # self.audio_file_time_length = get_audio_time_length(audio_file)  # Jet: 音频时间长度（分钟数）

        self.has_gui = has_gui  # Jet: 默认不用GUI显示
        self.converting_thread = None

        print("2: in XunfeiAudioConvertRequestApi __init__")

    # 有GUI显示转写进度，设置对应对话框调用的Thread线程 in convert_audio_progress_gui.py
    '''
    def set_convert_thread(self, converting_thread):
        if converting_thread is not None:
            self.converting_thread = converting_thread  # Jet adds: 用于显示信息到UI, convert_info_progressbar.py中 Runthread的对象
            self.has_GUI = True
            print("in set_convert_thread")
    '''
    # 根据不同的apiname生成不同的参数,本示例中未使用全部参数您可在官网(https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html)查看后选择适合业务场景的进行更换
    # speaker_number默认值为0，则表示盲分（不区分发音人），2代表两人
    # def gene_params(self, apiname, speaker_number=0, taskid=None, slice_id=None):
    # 如果转写一个讲话者的录音， 需设定： speaker_number =1
    def gene_params(self, apiname, speaker_number=1, taskid=None, slice_id=None):
        appid = self.appid
        secret_key = self.secret_key
        upload_file_path = self.audio_file

        ts = str(int(time.time()))
        m2 = hashlib.md5()
        m2.update((appid + ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')

        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        param_dict = {}

        if apiname == api_prepare:
            # slice_num是指分片数量，如果您使用的音频都是较短音频也可以不分片，直接将slice_num指定为1即可
            slice_num = int(file_len / file_piece_sice) + (0 if (file_len % file_piece_sice == 0) else 1)
            self.slice = slice_num  # Jet adds to estimate processing time

            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['file_len'] = str(file_len)
            param_dict['file_name'] = file_name
            param_dict['slice_num'] = str(slice_num)

            # Jet adds： 指定发音人的个数：e.g coach and client
            param_dict['speaker_number'] = speaker_number
            param_dict['has_seperate'] = 'true'

        elif apiname == api_upload:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid
            param_dict['slice_id'] = slice_id
        elif apiname == api_merge:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid
            param_dict['file_name'] = file_name
        elif apiname == api_get_progress or apiname == api_get_result:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid

        # print('param_dict:', param_dict)
        return param_dict

    # 请求和结果解析，结果中各个字段的含义可参考：https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html
    def gene_request(self, apiname, data, files=None, headers=None):
        response = requests.post(lfasr_host + apiname, data=data, files=files, headers=headers)
        result = json.loads(response.text)
        if result["ok"] == 0:
            msg = "{} 成功:".format(apiname) + str(result)
            self.cur_process = 2  # ？
            self.converting_thread.emit_msg(self.cur_process, msg)

            print(msg)

            return result
        else:
            print("{} 出错:".format(apiname) + str(result))

            msg = "{} 出错:".format(apiname) + str(result)
            self.cur_process = 2  # Jet: 随便设一个非百分百
            self.converting_thread.emit_msg(self.cur_process, msg)
            exit(0)
            return result

    # 预处理
    def prepare_request(self):
        return self.gene_request(apiname=api_prepare,
                                 data=self.gene_params(api_prepare,
                                                       speaker_number=self.speaker_number))  # Jet: 从生成对象的构造函数获得讲话人数量1 or 2

    # 上传
    def upload_request(self, taskid, upload_file_path):
        file_object = open(upload_file_path, 'rb')
        try:
            index = 1
            sig = SliceIdGenerator()
            while True:
                content = file_object.read(file_piece_sice)
                if not content or len(content) == 0:
                    break
                files = {
                    "filename": self.gene_params(api_upload).get("slice_id"),
                    "content": content
                }
                response = self.gene_request(api_upload,
                                             data=self.gene_params(api_upload, taskid=taskid,
                                                                   slice_id=sig.getNextSliceId()),
                                             files=files)
                if response.get('ok') != 0:
                    # 上传分片失败
                    print('upload slice fail, response: ' + str(response))
                    msg = '上传语音文件片断失败, 服务器回复: ' + str(response)
                    # self.print_dialog.print_info(msg)
                    self.cur_process = 3  # ?
                    if self.has_gui:
                        self.converting_thread.emit_msg(self.cur_process, msg)

                    return False
                # print('upload slice ' + str(index) + ' success')
                msg = '上传语音文件片断 ' + str(index) + ' 成功。'
                self.cur_process += 1  # Jet：假定1个片断只占1%的时间
                if self.has_gui:
                    self.converting_thread.emit_msg(self.cur_process, msg)

                index += 1
        finally:
            'file index:' + str(file_object.tell())
            file_object.close()
        return True

    # 合并
    def merge_request(self, taskid):
        return self.gene_request(api_merge, data=self.gene_params(api_merge, taskid=taskid))

    # 获取进度
    def get_progress_request(self, taskid):
        return self.gene_request(api_get_progress, data=self.gene_params(api_get_progress, taskid=taskid))

    # 获取结果
    def get_result_request(self, taskid):
        return self.gene_request(api_get_result, data=self.gene_params(api_get_result, taskid=taskid))


    # Jet adds:
    # i: 对应进度条的1-100
    # msg:要在UI显示的信息（从服务器返回的转写过程中的实时信息）
    def emit_msg(self, i, msg):
        self.signal.emit(i, msg)  # 注意这里的参数需要与上面pyqtSignal定义的一致
        print("in emit_msg, msg received: ", msg)



    #线程的主程序：
    def run(self):
        msg = "Start：调用讯飞转写语音文件：" + self.audio_file
        self.emit_msg(1, msg)

        # Jet: 调试阶段，先注释掉下一句。 调用转写函数
        # self.all_api_request()

        msg = "Finish: 原始语音转写到文件%s完成。 Thread ends." % self.raw_txt_file
        self.emit_msg(100, msg)

    '''
        任务状态码
        状态ID	状态描述
        0	任务创建成功
        1	音频上传完成
        2	音频合并完成
        3	音频转写中
        4	转写结果处理中
        5	转写完成
        9	转写结果上传完成
        '''
    # Jet: 集中调用讯飞api的函数
    def all_api_request(self):
        # 1. 预处理
        pre_result = self.prepare_request()
        taskid = pre_result["data"]
        # 2 . 分片上传
        self.upload_request(taskid=taskid, upload_file_path=self.audio_file)
        # 3 . 文件合并
        self.merge_request(taskid=taskid)
        # 4 . 获取任务进度

        interval = 10  # Jet:指定询问服务器转写状态的间隔秒数
        time_elapsed = 0 # Jet: 已经花费的时间，之前的上传不算，这里只计算转写过程的时间

        while True:
            # 每隔间隔秒获取一次任务进度
            progress = self.get_progress_request(taskid)
            progress_dic = progress
            if progress_dic['err_no'] != 0 and progress_dic['err_no'] != 26605:
                print('task error: ' + progress_dic['failed'])

                msg = '转写任务出错：' + progress_dic['failed']
                if self.has_gui:
                    #self.converting_thread.emit_msg(self.cur_process, msg)
                    self.emit_msg(self.cur_process, msg)

                return
            else:
                data = progress_dic['data']
                task_status = json.loads(data)
                if task_status['status'] == 9:
                    print('task ' + taskid + ' finished')

                    msg = '转写任务编号 ' + taskid + '完成!'
                    self.cur_process = 100  # Jet：假定上传语音完成只占5%的时间
                    if self.has_gui:
                        #self.converting_thread.emit_msg(self.cur_process, msg)
                        self.emit_msg(self.cur_process, msg)

                    break
                # 每隔30秒刷新一次gui提示
                if self.has_gui and time_elapsed % 30 == 0:
                    print('The task ' + taskid + ' is in processing, task status: ' + str(data))
                    msg = '转写任务编号 ' + taskid + ' 正在进行中...任务状态： ' + str(data)
                    #self.converting_thread.emit_msg(self.cur_process, msg)
                    self.emit_msg(self.cur_process, msg)
            # 每次获取进度间隔10S
            time.sleep(interval)
            time_elapsed += interval

        # 5 . 获取结果
        # self.get_result_request(taskid=taskid)
        # Jet改写：
        result = self.get_result_request(taskid=taskid)
        return result

# 无需进度条，命令行调用，
# 1个讲话者
def convert_1speaker_audio_to_text(audio_file, output_raw_file):
    api = XunfeiAudioConvertRequestApiThread(audio_file, output_raw_file, speaker_number=1)
    result = api.all_api_request()

    # 指定编码格式为UTF-8格式，中英文都可正常存储
    try:
        fw = open(output_raw_file, 'w', encoding='utf-8')  # w为写文件write
        fw.write(str(result))
        msg = "语音转写内容保存到文件:%s成功！" % output_raw_file
        print(msg)

    except:
        msg = "语音转写内容保存到文件:%s失败" % output_raw_file
        print(msg)

    finally:
        fw.close()

# 1个讲话者 GUI显示进度
def convert_1speaker_audio_to_text_with_gui(audio_file, output_raw_file):
    thread = XunfeiAudioConvertRequestApiThread(audio_file, output_raw_file, speaker_number=1, has_gui=True)
    #thread.set_convert_thread(converting_thread) #设置刷新进度显示的线程

    result = thread.all_api_request()

    # 指定编码格式为UTF-8格式，中英文都可正常存储
    try:
        fw = open(output_raw_file, 'w', encoding='utf-8')  # w为写文件write
        fw.write(str(result))
        msg = "语音转写内容保存到文件:%s成功！" % output_raw_file
        print(msg)

    except:
        msg = "语音转写内容保存到文件:%s失败" % output_raw_file
        print(msg)

    finally:
        fw.close()

# 2个讲话者 GUI显示进度
def convert_2speakers_audio_to_text_with_gui(audio_file, output_raw_file, converting_thread):
    print('in xunfei Api, convert 2speakers.')
    api = XunfeiAudioConvertRequestApiThread(audio_file, output_raw_file, speaker_number=2, has_gui=True)

    #api.set_convert_thread(converting_thread) #设置刷新进度显示的线程

    result = api.all_api_request()

    # 指定编码格式为UTF-8格式，中英文都可正常存储
    try:
        fw = open(output_raw_file, 'w', encoding='utf-8')  # w为写文件write
        fw.write(str(result))
        msg = "语音转写内容保存到文件:%s成功！" % output_raw_file

    except:
        msg = "语音转写内容保存到文件:%s失败" % output_raw_file

    finally:
        fw.close()


# 2个讲话者
def convert_2speakers_audio_to_text(audio_file, output_raw_file):
    api = XunfeiAudioConvertRequestApiThread(audio_file, output_raw_file, speaker_number=2)
    result = api.all_api_request()

    # 指定编码格式为UTF-8格式，中英文都可正常存储
    try:
        fw = open(output_raw_file, 'w', encoding='utf-8')  # w为写文件write
        fw.write(str(result))
        msg = "语音转写内容保存到文件:%s成功！" % output_raw_file

    except:
        msg = "语音转写内容保存到文件:%s失败" % output_raw_file

    finally:
        fw.close()


# 注意：如果出现requests模块报错："NoneType" object has no attribute 'read', 请尝试将requests模块更新到2.20.0或以上版本(本demo测试版本为2.20.0)
# 输入讯飞开放平台的appid，secret_key和待转写的文件路径

if __name__ == '__main__':
    # Jet根据注册获取的信息
    # api = RequestApi(appid="5ae46872", secret_key="29333cff087134935d8c43b7443fac38", upload_file_path=r"C:\Users\ASUS-PC\Documents\6.4.2-test-语音转写.wav")
    # 测试31M，6分钟的教练、客户对话。用时：？，出结果

    # output_file = '../output/' + audio_file + "-讯飞转写原始结果.txt"  # r"D:\audiotest\1.3编程猫源码编辑器的下载和安装.txt"

    # convert_to_file("../audio/"+audio_file, output_file)

    output_file = audio_file + "-讯飞转写原始结果.txt"
    # convert_1speaker_audio_to_text(audio_file, output_file)
    # convert_2speaker_audio_to_text(audio_file, output_file)

'''
2020-0619
转写过程中的信息，可以据此在UI中给出更易读的提示信息，
问题：调用讯飞时，UI不显示，需要用多线程来解决
'''
'''
测试转写内容如下：
/getResult success:
{'data': '[{"bg":"100","ed":"1220","onebest":"那你们怎么样？","speaker":"1"},
{"bg":"1220","ed":"3180","onebest":"呢最近我们都挺好的，","speaker":"1"},
{"bg":"3300","ed":"4180","onebest":"嗯","speaker":"1"},{"bg":"4180","ed":"5500","onebest":"感谢主。嗯","speaker":"2"},{"bg":"5540","ed":"7840","onebest":"你跟生那个","speaker":"2"},{"bg":"7840","ed":"9850","onebest":"水痘的那个情况怎么样？","speaker":"2"},{"bg":"9850","ed":"9980","onebest":"啊","speaker":"2"},{"bg":"10780","ed":"13620","onebest":"噢那个昨天那个","speaker":"1"},{"bg":"13650","ed":"16130","onebest":"就是今天是第20天，嘛","speaker":"1"},{"bg":"16280","ed":"22020","onebest":"然后嗯昨天是洗澡了，然后今天早上就今天就出门了，早上","speaker":"1"},{"bg":"22200","ed":"23130","onebest":"然后","speaker":"1"},{"bg":"23130","ed":"26010","onebest":"那个早上去去市里面","speaker":"1"},{"bg":"26010","ed":"30530","onebest":"找了一个那个医院，然后中医院我妈找了一个院长，然后给我开了 点药，","speaker":"1"},{"bg":"30870","ed":"35810","onebest":"就说那个我妈说得让我再吃吃几副中药。","speaker":"1"}]', 'err_no': 0, 'failed': None, 'ok': 0}


Jet: 后期需要做的事情：
done. 1、从结果字符串获取data之后信息，生成字典，
done. 2、新建文件，存储结果到文件中
done. 3、根据时间的起始和终止，改写为字典：
bg  句子相对于本音频的起始时间，单位为ms
ed  句子相对于本音频的终止时间，单位为ms

done. 4、用GUI操作，让用户选择声音文件，可以适当编辑，选择导出的文本格式，导出文件
done. 5、按ICF标准格式生成word文档


'''
