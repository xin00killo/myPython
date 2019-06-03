#coding:UTF-8
#__autor__='wyxces'

import re

# 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

pattern = r'\d+'
str = 'runoob 123 google 456'
finditer = re.finditer(pattern, str)
print('re.finditer(pattern, str):%s\n\ttype:%s'%(finditer, type(finditer)))

# 遍历返回的结果
print('遍历返回的结果:')
for find in finditer:
    print(find)