#coding:UTF-8
#__autor__='wyxces'

'''
82、s="info:xiaoZhang 33 shandong",
用正则切分字符串输出
['info', 'xiaoZhang', '33', 'shandong']
'''

import re
s="info:xiaoZhang 33 shandong"
pattern = r'\w+'
s_list = re.findall(pattern,s)
print(s_list)

'''
运行结果：['info', 'xiaoZhang', '33', 'shandong']
'''