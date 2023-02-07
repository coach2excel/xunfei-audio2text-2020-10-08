# Baidu AI翻译UI
# 从源语言翻译到目标语言

import tkinter as tk
from tkinter.scrolledtext import ScrolledText  # 带滚动条的多行文本框
from tkinter import ttk  # Tk主题样式设置
import tkinter.filedialog
import os
#import baidutranslationapi  # 需要对应的.py文件，放在同一文件夹内

#设定speaker1是教练或客户
def combo_speaker1_selected(event):
    print("src: %s" % combo_speaker1.get())  # #获取选中的值_方法1
    # print("src: %s"  % src_lang.get())      # #获取选中的值_方法2

# 保存到选定的文件
def save_icf_to_word():
    pass

def save_icf_to_txt():
'''
    if not len(str_translation) == 0:
        default_dir = os.getcwd()  # 获取当作工作目录
        # 打开另存为对话框
        file_path = tk.filedialog.asksaveasfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        print('save translation to file path: %s' % file_path)

        try:
            fp = open(file_path, "w", encoding='utf-8')
            # 把已经翻译好的文本字符串保存到指定文件
            fp.write(str_translation)  # 需要先翻译好才行
        except IOError:
            print("Fail to open file.")
        finally:
            fp.close()
    else:
        tk.messagebox.showinfo('保存错误提示', '请先翻译好再保存哦')
'''

# 选择指定的音频文件
def select_audio_file():
    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    # 打开文件选择对话框
    file_path = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(current_path)))
    print('read file from path: %s' % file_path)

    return file_path

def set_output_dir():
    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    # 打开文件选择对话框
    file_path = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(current_path)))
    print('read file from path: %s' % file_path)

    #set default output path

    return file_path

def convert_audio2raw_script(filename):
    # 调用讯飞语音，转写成原始文稿
    #convert_audio.

    # 显示在左边文本框中

    #先按默认文件名保存在默认路径下（以防意外）
    

    pass
# ====================================
root_frame = tk.Tk()  # 生成主窗口
root_frame.title("教练语音转写助手")  # 窗口标题
root_frame.geometry("1760x1280+200+20")  # 窗口大小，宽x高(注意：是用字母x表示乘号，后面+号是相对于屏幕的x,y坐标


# 创建tk变量
var_src_lang = tk.StringVar()  # #创建变量，便于取值
var_dst_lang = tk.StringVar()  # #创建变量，便于取值

# 文本框，不需要绑定变量， 可用insert/get函数来设置/获取文本
text_raw = ScrolledText(root_frame, width=40, height=20, font=("隶书", 18))  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
text_src.place(x=30, y=80)  # 滚动文本框在页面的位置

text_icf = ScrolledText(root_frame, width=40, height=20, font=("隶书", 18))  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
text_dst.place(x=600, y=80)  # 滚动文本框在页面的位置

# 语言：标签及下拉选项
label_src = tk.Label(root_frame, text="源语言：")
label_src.place(x=30, y=20)
combo_speaker1 = ttk.Combobox(root_frame, textvariable=var_src_lang)  # #创建下拉菜单

combo_speaker1.place(x=100, y=20)  # #将语言下拉选项绑定到窗体
combo_speaker1["value"] = ("教练", "客户")  # #给下拉菜单设定值
combo_speaker1["state"] = "readonly"  # 不让用户修改
combo_src.current(0)  # #设定下拉菜单的默认值为第1个

label_dst = tk.Label(root_frame, text="目标语言：")
label_dst.place(x=550, y=20)

combo_dst.place(x=650, y=20)  # #将语言下拉选项绑定到窗体
combo_dst["value"] = ("中文", "英语", "俄语", "日语")  # #给下拉菜单设定值
combo_dst["state"] = "readonly"  # 不让用户修改
combo_dst.current(0)  # #设定下拉菜单的默认值为第1个

combo_speaker1.bind("<<ComboboxSelected>>", combo_speaker1_selected)  # #给下拉菜单绑定事件

btn_batch_translate = tk.Button(root_frame, text=' 全完翻译完再显示  ', command=batch_translate)
btn_batch_translate.place(x=850, y=20)
# btn_translate = Button(root_frame, text='  翻译  ')
# btn_translate.bind('<ButtonRelease-1>', buttonListener_translate)

btn_translate_by_row = tk.Button(root_frame, text=' 逐行翻译并显示  ', command=translate_by_row)
btn_translate_by_row.place(x=1000, y=20)

# to 添加btn_paste:
btn_paste = tk.Button(root_frame, text='粘贴文本', command=paste_text)
btn_paste.place(x=300, y=580)

btn_read_src = tk.Button(root_frame, text='从文件中读取...', command=read_from_file)
btn_read_src.place(x=400, y=580)

btn_save_dst = tk.Button(root_frame, text='保存翻译文本...', command=save_to_file)
btn_save_dst.place(x=950, y=580)

root_frame.mainloop()  # #窗口持久化
