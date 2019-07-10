#coding:UTF-8
#__autor__='wyxces'

'''
44 a="张明 98分"，用re.sub，将98替换为100
'''
import re

str = "张明 98分"
new_str = re.sub(r'98','100',str)
print(new_str)