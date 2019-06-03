#coding:UTF-8
#__autor__='wyxces'

import re

'''
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	这个选项忽略规则表达式中的空白和注释，并允许使用 ’#’ 来引导一个注释。这样可以让你把规则写得更美观些。。
re.DOTALL  感觉和S一样呀？
'''

# re.I	使匹配对大小写不敏感    不区分(ignore)大小写；
print('-----re.I	使匹配对大小写不敏感    不区分(ignore)大小写；------------')
pattern = 'a'
str = 'ABCDefgabcdEFG'
print(re.findall(pattern, str))
print(re.findall(pattern, str, re.I))
'''
['a']
['A', 'a']
'''


# re.M	多行匹配，影响 ^ 和 $    多(more)行匹配
# 单行匹配时，只匹配整个str串儿的结尾， 多行匹配是匹配每行str串儿的结尾
print('-----re.M	多行匹配，影响 ^ 和 $    多(more)行匹配------------')
pattern = 'b$'
str = 'abcdabcb\nabcdabcb'
print(re.findall(pattern, str))
print(re.findall(pattern, str, flags=re.M))
'''
['b']
['b', 'b']
'''



# re.DOTALL	使得换行符 参与匹配
print('-----re.DOTALL	使得换行符 参与匹配------------')
pattern = '.'
str = 'abcd\nabcd'
print(re.findall(pattern, str))
print(re.findall(pattern, str, flags=re.DOTALL))
'''
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', '\n', 'a', 'b', 'c', 'd']
'''

# re.X	这个选项忽略规则表达式中的空白和注释，
# 并允许使用 ’#’ 来引导一个注释。这样可以让你把规则写得更美观些。。
print('-----re.X	这个选项忽略规则表达式中的空白和注释,允许使用 ’#’ 来引导一个注释------------')
pattern = '''
#需要匹配a
a 
#匹配 a 或 b
|bc
'''
str = 'abcd\nabcd'
print(re.findall(pattern, str))
print(re.findall(pattern, str, re.X))
'''
[]
['a', 'bc', 'a', 'bc']
'''



# re.S	使 . 匹配包括换行在内的所有字符
print('-----re.S	使 . 匹配包括换行在内的所有字符------------')
pattern =r'.'
str = 'abcd\nabcd'
print(re.findall(pattern, str))
print(re.findall(pattern, str, re.S))
'''
[]
['a', 'bc', 'a', 'bc']
'''