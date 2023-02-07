2020-0628
文件功能概述及调用关系：

1、主界面：XunfeiConvertingUI.py
class XunFeiConvertingUIMainWindow
功能：用户选择要转写的audiofile,要转写到的原始txt file,开始转写

2、转写进度界面（子界面）：covnerti_audio_progress_gui.py
    调用： JetsXunfeiApi.py  (涉及需付费的数据，后期需要源码加密！）
            调用：audio/getaudiofo.py

3、转换原始转写的txt为其它格式（时间戳格式、1人或2人对话ICF格式):
    （注：可以主界面显示，也可以用Tab或菜单或工具栏选择，用新的对话框显示）
    调用：transform_rawtxt.py

















