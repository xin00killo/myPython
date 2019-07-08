#coding=utf-8
# __autor__='wyxces'

'''
26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"

'''

import re

# me
str = "not 404 found 张三 99 深圳"
str = re.sub(r'[a-z0-9]','',str)  #将字母 数字都替换掉，等于删除啦
print(str)
str = re.findall(r'\w.*',str) # 从字符开始匹配到结尾
print(str,type(str))
str = "".join(str) #将列表转换回 字符串
print(str)

print('分割线'.center(50,'-'))
#网上找的方法
str = "not 404 found 张三 99 深圳"
list = str.split(' ')
print(list)
res  = re.findall(r'\d+|[a-z]+', str)
print(res)
for i in res:
    if i in list:
        list.remove(i)
print(list)
new_str = '  '.join(list)
print(new_str)