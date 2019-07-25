#coding:UTF-8
#__autor__='wyxces'

'''
89、用两种方法去空格
'''

import re

s = "asd adkfjia df aj  adlkfj  adkji  adkjf jl     adf     "

#########方法一  正则表达式  sub函数
s_new1 = re.sub(r"\s+",'',s)
print(s_new1)

#########方法二   正则提取
s_new2 = ''.join(re.findall(r'\S+',s))
print(s_new2)

########方法三 利用split 函数
s_new3 = ''.join(s.split())
print(s_new3)


########方法四 利用replace 函数
s_new4 = s.replace(r'\s+','')
print(s_new3)