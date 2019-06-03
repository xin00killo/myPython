#coding:UTF-8
#__autor__='wyxces'

import re

# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表


pattern1 = r'\d+'
str = 'runoob 123 google 456* wyxces'

print('pattern1:%s\nstr:%s'%(pattern1,str))
tesultList1 = re.split(pattern1, str)
print('re.split(pattern1, str):', tesultList1)

#对于一个找不到匹配的字符串而言，split 不会对其作出分割
print('-----------------------')
pattern2 = 'xxxxxx'
print('pattern2:%s\nstr:%s'%(pattern2,str))
tesultList2 = re.split(pattern2, str)
print('re.split(pattern2, str):', tesultList2)
