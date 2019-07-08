#coding=utf-8
# __autor__='wyxces'

'''
29、正则re.complie作用
'''

# complie函数
# 用于变异正则表达式，生成一个正则表达式（Pattern）对象

import re

regex = r'\d+'
pattern = re.compile(regex)
str = 'asdf11234jlkjkl1q234jlkjlk235'
dList = pattern.findall(str)
newStr = ''.join(dList)
print(dList,' ',newStr)