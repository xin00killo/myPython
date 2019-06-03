#coding:UTF-8
#__autor__='wyxces'

import re

# 检索和替换
# re.sub用于替换字符串中的匹配项

print('----real参数为字符串---------------------------')
phone = '130-1111-2222  # 这是一个~电话号码'
print('phone:', phone)
# 删除注释   # 号后面的都被删除了
pattern1 = '#.*$'
print('删除注释\npattern1:',pattern1)
phone01 = re.sub(pattern1, '', phone)
print('re.sub(pattern1, '', phone):', phone01)
# 移除非数字的内容
pattern2 = '\D'
print('移除非数字的内容\npattern2:',pattern2)
phone02 = re.sub(pattern2, '', phone)
print('re.sub(pattern2, '', phone):', phone02)

print('----real参数为函数---------------------------')
def myDouble(matched):
    value = int(matched.group('value'))
    return str(value*2)
s = 'a-4-8-S-9-eaa-889-aegR18HJWS4WG1'
pattern = '(?P<value>\d+)'
ss = re.sub(pattern, myDouble, s)
print('str:', s, '\npattern:', pattern)  # 会将匹配到的结果，作为参数，传给函数
print('re.sub(pattern, myDouble, s):', ss)