#coding:UTF-8
#__autor__='wyxces'

import re


#match	 从开头开始匹配，只匹配一次
print('-------match--------------------------------------------')
patternStr = 'a'
str = 'ABCDabcd'
patternObj = re.compile(patternStr)
print('re.match(patternStr, str, re.I):',re.match(patternStr, str, re.I))
print('patternObj.match(str, 4):',patternObj.match(str, 4))

#search	 整个串儿中匹配，只匹配一次
print('-------search--------------------------------------------')
patternStr = 'b'
str = 'ABCDabcd'
patternObj = re.compile(patternStr)
print('re.search(patternStr, str, re.I):',re.search(patternStr, str, re.I))
print('patternObj.search(str, 4):',patternObj.search(str, 4))
print('patternObj.search(str, 6):',patternObj.search(str, 6))

#findall	 整个串儿中匹配，匹配所有
print('-------findall--------------------------------------------')
patternStr = 'b'
str = 'ABCDabcd'
patternObj = re.compile(patternStr)
print('re.findall(patternStr, str, re.I):',re.findall(patternStr, str, re.I))
print('patternObj.findall(str, 4):',patternObj.findall(str, 4))
print('patternObj.findall(str, 6):',patternObj.findall(str, 6))

#split	 整个串儿中匹配，匹配所有
print('-------split--------------------------------------------')
patternStr = 'b'
str = 'ABCDabcdABCDabcd'
patternObj = re.compile(patternStr)
print('re.split(patternStr, str, re.I):',re.split(patternStr, str, maxsplit=0, flags=re.I))
print('re.split(patternStr, str, re.I):',re.split(patternStr, str, maxsplit=1, flags=re.I))
print('patternObj.split(str, maxsplit=0):',patternObj.split(str, maxsplit=0))
print('patternObj.split(str, maxsplit=1):',patternObj.split(str, maxsplit=1))


#finditer	 整个串儿中匹配，匹配所有,返回迭代器
print('-------finditer--------------------------------------------')
patternStr = 'b'
str = 'ABCDabcdABCDabcd'
patternObj = re.compile(patternStr)
print('re.finditer(patternStr, str, re.I):')
for i in re.finditer(patternStr, str, flags=re.I):
    print('\t', i)
print('patternObj.finditer(str, pos=0):')
for i in patternObj.finditer(str, pos=0):
    print('\t', i)
print('patternObj.finditer(str, pos=6):')
for i in patternObj.finditer(str, pos=6):
    print('\t', i)

#sub	 整个串儿中匹配，匹配所有
print('-------sub--------------------------------------------')
patternStr = 'b'
str = 'ABCDabcdABCDabcd'
patternObj = re.compile(patternStr)
replaceStr = ' 999 '
print('re.sub(patternStr, replaceStr, str, count=0):',re.sub(patternStr, replaceStr, str, count=0))
print('re.sub(patternStr, replaceStr, str, count=0, flags=re.I):',re.sub(patternStr, replaceStr, str, count=0, flags=re.I))
print('re.sub(patternStr, replaceStr, str, count=1, flags=re.I):',re.sub(patternStr, replaceStr, str, count=1))
print('patternObj.sub(replaceStr, str, count=0):',patternObj.sub(replaceStr, str, count=0))
print('patternObj.sub(replaceStr, str, count=1):',patternObj.sub(replaceStr, str, count=1))

