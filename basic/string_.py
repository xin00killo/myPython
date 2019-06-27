#coding:UTF-8
#__autor__='wyxces'


# a-zA-Z
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.whitespace)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)

# -*- coding: utf-8  -*-
# -*- Author: WangHW -*-
import string

values = {'var':3.3333333}
#1
t1 = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")
print('TEMPLATE:',t1.substitute(values))
print('############################')
#2
s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""
print('INTERPOLATION:',s % values)
print('############################')

#3
s1 = """
Variable         {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print('FORMAT:',s1.format(**values))




import datetime
# 设计字符串模板
template = ('\nDate: "{}", Temperature: {:.1f}, Condition: "{}"')
# 根据字符串模板生成字符串
log = template.format(datetime.datetime.now(), 23.17, 'good')
# 打印格式化后的字符串
print(log)
