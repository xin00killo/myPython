#coding:UTF-8
#__autor__='wyxces'

'''
99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
'''
import re

s = '''adsfa<html><h1>www.
99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>sdf
<html><h1>www.
dsfdfwww.itcast.cn</h1>
www.itcasdfst.cn</h1>
'''

pattern = r"<\w+><\w+>.*?</\w+></\w+>"
s_new = "".join(re.findall(pattern, s))
print(s_new)


