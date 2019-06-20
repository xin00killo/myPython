#coding:UTF-8
#__autor__='wyxces'

'''
3、列出5个python标准库
os：提供了不少与操作系统相关联的函数
sys:   通常用于命令行参数
re:   正则匹配
math: 数学运算
datetime:处理日期时间


文件通配符 glob
访问 互联网 urllib   其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
数据压缩  以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
性能度量 timeit
测试模块 doctest
'''

import glob
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
print(glob.glob('*.py'))
