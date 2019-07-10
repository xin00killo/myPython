#coding:UTF-8
#__autor__='wyxces'

'''
37 正则表达式匹配中，（.*）和（.*?）匹配区别？
'''


'''
(.*) 贪婪模式，全部匹配,输出匹配到的位置开始及以后的所有
（.*？）非贪婪模式，匹配到一个就不再匹配啦，只输出匹配到的那个
'''

import re

str = 'aslkfjoiwasnvlkjaoijf'
print('.*',re.findall(r'j.*',str))
print('.*?',re.findall(r'j.*?',str))