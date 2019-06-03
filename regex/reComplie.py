#coding:UTF-8
#__autor__='wyxces'

import re
# complie函数
# 用于变异正则表达式，生成一个正则表达式（Pattern）对象，供match和search函数使用

# 用于匹配至少一个数字
regex = r'\d+'
pattern = re.compile(regex)
print('regex:', regex, type(regex), '\npattern:', pattern, type(pattern))
str = 'one12twothree34four'
print('str:', str)
print('pattern.match(str):', pattern.match(str)) # 查找头部，没有匹配
print('pattern.match(str,2,10):', pattern.match(str,2,10)) # 从'e'的位置开始匹配，没有匹配
print('pattern.match(str,3,10):', pattern.match(str,3,10)) # 从'1'的位置开始匹配，正好匹配 返回一个 Match 对象

