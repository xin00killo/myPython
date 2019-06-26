#coding=utf-8
# __autor__='wyxces'

'''
12、简述with方法打开处理文件帮我我们做了什么？
'''

import os
print(os.getcwd())

# 读文件
try:
    f = open('../basic/file_/myfile.text','r')
    # 如果文件不存在，open()函数就会抛出一个IOError的错误，并：FileNotFoundError
    str = f.read()
    print(str)
except:
    pass
finally:
    f.close()

'''
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with 的作用就是调用close（）方法
'''

with open( '../basic/file_/myfile.text', 'r' ) as f:
    print( f.read() )