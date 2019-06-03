#coding:UTF-8
#__autor__='wyxces'

import re

# 1、从起始位置匹配，如果不是起始位置匹配成功的话，返回none
# 2、匹配成功，re.match方法返回一个匹配的对象，否则返回None

print('----re.match.span--------------------------------------------')
regex1 = 'www'
regex2 = 'com'
str = 'www.wyxces.com'
result1_1 = re.match(regex1, str)
result1_2 = re.match(regex1, str).span()
result2 = re.match(regex2, str)
print('regex1:', regex1, '\nregex2:',regex2, '\nstr:',str)
print('re.match(regex1, str):', result1_1)
print('re.match(regex1, str).span():', result1_2)
print('re.match(regex2, str):', result2)

print('----re.match.group/grpups--------------------------------------------')
str = 'Cats are smarter than dogs'
# .* 表示任意匹配除换行符（\n \r）之外的任何单个或多个字符
regex = '(.*) are (.*?) (.*)'
print('regex:', regex, '\nstr:',str)
matchObj = re.match(regex, str, re.M|re.I)
print('matchObj:', matchObj)
if matchObj:
    print('matchObj.group():', matchObj.group())
    print('matchObj.group(0):', matchObj.group(0))
    print('matchObj.group(1):', matchObj.group(1))
    print('matchObj.group(2):', matchObj.group(2))
    print('matchObj.group(3):', matchObj.group(3))
    print('matchObj.groups():', matchObj.groups())
    print('matchObj.groups(0):', matchObj.groups(0))
    print('matchObj.groups(1):', matchObj.groups(1))
    print('matchObj.groups(2):', matchObj.groups(2))
    print('matchObj.groups(3):', matchObj.groups(3))












