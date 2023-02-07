#字典的应用——我的字典--二进制存取
import pickle #序列化（保存）对象到文件
#pickle将Python对象层次结构转换为字节流

dict1 = {
    'immanuel':{'中文':'以马内利','难度':3},
    'salvation':{'中文':'救赎','难度':2},
    'bless':{'中文':'称颂','难度':4},
}

#按key升序排序
def sort_dict(dict1):
    list1=sorted(dict1.items(), key = lambda item:item[0])
    sorted_dict =dict(list1)
    return sorted_dict

#按key降序排序
def reverse_sort_dict(dict1):
    list3=sorted(dict1.items(), key = lambda item:item[0], reverse=True)
    reverse_dict =dict(list3)
    return reverse_dict

#查找单词
def search_vocab(vocab, dict1):
    if vocab in dict1:
        item=dict1[vocab]
        print(vocab,':', item['中文'], ',难度:', item['难度'])
    else:
        print('%s not found.' % vocab)

#保存词典到文件        
def save_sorted_dict(dict1, filename):
    fw=open(filename, 'wb')  #b代表用二进制方式写入文件
    pickle.dump(dict1, fw)
    fw.close()
    
#从词典文件读取数据，生成python字典
def read_sorted_dict(filename):
    global dict3 #声明为全局变量
    fr=open(filename, 'rb')   #b代表用二进制方式读取文件
    dict3=pickle.load(fr)
    print('read dict from file:\n',dict3)
    
#把词典数据写入数据文件
filename='mydict.data'  #跟.py文件在同一文件夹
dict2 = sort_dict(dict1)
save_sorted_dict(dict2, filename)

#从词典数据文件中读取
dict3={}
read_sorted_dict(filename)

dict3['hallelujah']={'中文':'哈利路亚','难度':1}
print('new item added:\n', dict3)
dict3 = sort_dict(dict3)
print('dict3 after sort again:\n', dict3)

dict4 = reverse_sort_dict(dict3)
print('reverse sorted  dict4:\n',dict4)

vocab =input('请输入要查找的单词：')
search_vocab(vocab, dict3)

