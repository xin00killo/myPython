#coding:UTF-8
#__autor__='wyxces'

'''
87、统计字符串中某字符出现次数
'''

import re


str ="waetuohn;laier90hgnsa;lier0phybga;ldkeirha's;lodir"
c = "a"

################  使用正则
count = len(re.findall(c,str))
print("字符{}在str中出现次数为{}次".format(c,count))


##############  使用循环
count2=0
for s in list(str):
    if s == c:
        count2 += 1

print("字符{}在str中出现次数为{}次".format(c,count2))

##############  count函数
count3 = str.count(c)
print("字符{}在str中出现次数为{}次".format(c,count3))


'''
运行结果：
字符a在str中出现次数为5次
字符a在str中出现次数为5次
字符a在str中出现次数为5次
'''