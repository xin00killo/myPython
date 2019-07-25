#coding:UTF-8
#__autor__='wyxces'

'''
lower()	将字符串转换为小写字符串
upper()	将字符串转换为大写字符串
capitalize()	将字符串首字母变为大写
title()	每个单词的首字母大写
swapcase()	大小写互换
'''

s ="waetuohn;lLL90hgnsa;lier0DCCWybga;ldkeQ3odir"
print('原字符串:\n\t',s)
s_upper = s.upper()
print("转化为大写后为：\n\t", s_upper)
s_lower = s.lower()
print("转化为大写后为：\n\t", s_lower)
s_swap = s.swapcase()
print("大小写互换后为：\n\t", s_swap)
s_capitalize = s.capitalize()
print("首字母大写为：\n\t", s_capitalize)
s_title = s.title()
print("每个单词首字母大写为：\n\t", s_title)