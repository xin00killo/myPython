#coding:UTF-8
#__autor__='wyxces'

import re

#findAll
#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没匹配到-返回空列表

pattern = re.compile(r'\d+')
str = 'runoob 123 google 456'

result1 = pattern.findall(str)
result2 = pattern.findall(str, 0, 10)

print('pattern:%s\nstr:%s'%(pattern, str))
print('pattern.findall(str):',result1 )
print('pattern.findall(str, 0, 10):',result2 )

result3 = re.findall(pattern,str)
print('re.findall(pattern,str):',result3)