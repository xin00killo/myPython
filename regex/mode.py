#coding:UTF-8
#__autor__='wyxces'

import re

# ^	匹配字符串的开头
print('-----^	匹配字符串的开头------------')
pattern1 = '^b'
pattern2 = 'b'
str1 = 'abcdabcd'
str2 = 'babcdabcd'
print(re.findall(pattern1, str1)) #-->[]  因为开头不匹配，所以结果为空
print(re.findall(pattern2, str1)) #-->['b', 'b']
print(re.findall(pattern1, str2)) #-->['b']
print(re.findall(pattern2, str2)) #-->['b', 'b', 'b']


# $	匹配字符串的末尾
print('-----$	匹配字符串的末尾------------')
pattern1 = 'b$'
pattern2 = 'b'
str1 = 'abcdabcd'
str2 = 'abcdabcdb'
print(re.findall(pattern1, str1)) #-->[]  因为开头不匹配，所以结果为空
print(re.findall(pattern2, str1)) #-->['b', 'b']
print(re.findall(pattern1, str2)) #-->['b']
print(re.findall(pattern2, str2)) #-->['b', 'b', 'b']


# .	匹配任意字符
print('-----.	匹配任意字符------------')
pattern = '.'
str = 'abcd\nabcd'
print(re.findall(pattern, str)) #-->['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
print(re.findall(pattern, str, flags=re.DOTALL)) #-->['a', 'b', 'c', 'd', '\n', 'a', 'b', 'c', 'd']


# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
print('-----[...]	用来表示一组字符 满足其中之一即匹配------------')
pattern1 = '[ac]'
str1 = 'abcdabcd'
print(re.findall(pattern1, str1)) #-->['a', 'c', 'a', 'c']


# [^...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
print('-----[^...]	用来表示一组字符 不匹配其中的字符------------')
pattern1 = '[^ac]'
str1 = 'abcdabcd'
print(re.findall(pattern1, str1)) #-->['b', 'd', 'b', 'd']


# re*	匹配0个或多个的表达式。
print('-----re*	匹配0个或多个的表达式。------------')
pattern1 = 'c*'
str1 = 'abcdccdd'
print(re.findall(pattern1, str1)) #-->['', '', 'c', '', 'cc', '', '', '']


# re+	匹配1个或多个的表达式。
print('-----re+		匹配1个或多个的表达式。------------')
pattern1 = 'c+'
str1 = 'abcdccdd'
print(re.findall(pattern1, str1)) #-->['c', 'cc']

# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
print('-----re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式。------------')
pattern1 = 'c?'
str1 = 'abcdccdd'
print(re.findall(pattern1, str1)) #-->['', '', 'c', '', 'c', 'c', '', '', '']


# re{ n}	匹配n个前面表达式。
print('-----re{ n}	匹配n个前面表达式。------------')
pattern1 = 'c{2}'
str1 = 'abcdccdd'
str2 = 'abcdccddcccddd'
print(re.findall(pattern1, str1)) #-->['cc']
print(re.findall(pattern1, str2)) #-->['cc', 'cc']


# re{ n}	匹配n个前面表达式。
print('-----re{n,}	匹配n个前面表达式。------------')
pattern1 = 'c{2,}'
str1 = 'abcdccdd'
str2 = 'abcdccddcccddd'
print(re.findall(pattern1, str1)) #-->['cc']
print(re.findall(pattern1, str2)) #-->['cc', 'ccc']


# re{ n}	匹配n个前面表达式。
print('-----re{n,}	匹配n个前面表达式。------------')
pattern1 = 'c{2,3}'
str1 = 'abcdccddcccdddccccdddd'
print(re.findall(pattern1, str1)) #-->['cc', 'ccc', 'ccc']


# a| b	匹配a或b
print('-----a| b	匹配a或b------------')
pattern1 = 'a|b'
pattern2 = 'a|b|c'
str1 = 'abcdabcd'
print(re.findall(pattern1, str1)) #-->['a', 'b', 'a', 'b']
print(re.findall(pattern2, str1)) #-->['a', 'b', 'c', 'a', 'b', 'c']


#(re)	匹配括号内的表达式，也表示一个组（分组）
print('-----(re)	匹配括号内的表达式，也表示一个组------------')
pattern1 = '(a)b(c|d)'
str1 = 'abcdabcdacbd'
result = re.match(pattern1, str1)
print(result) #--><re.Match object; span=(0, 3), match='abc'>
print(result.group(1)) #-->a
print(result.group(2)) #-->c


#((?imx: re)	在括号中使用i, m, 或 x 可选标志
print('-----(?imx: re)	在括号中使用i, m, 或 x 可选标志-----------')
pattern1 = '(?i:A)'
pattern2 = '(?x:a  b)'
pattern3 = '(?m:^a)'
pattern4 = '(^a)'
str1 = 'abcd\nabcdAcbd'
print(re.findall(pattern1, str1)) #--> ['a', 'a', 'A']
print(re.findall(pattern2, str1)) #--> ['ab', 'ab']
print(re.findall(pattern3, str1)) #--> ['a', 'a']
print(re.findall(pattern4, str1)) #--> ['a']


# \w	匹配数字字母下划线
print('-----\w	匹配数字字母下划线------------')
pattern1 = r'\w'
str1 = '这里是：wyx正则_-1'
print(re.findall(pattern1, str1)) #-->['这', '里', '是', 'w', 'y', 'x', '正', '则', '_', '1']


# \W	匹配非数字字母下划线
print('-----\W	匹配非数字字母下划线------------')
pattern1 = r'\W'
str1 = '这里是：wyx正则_-1'
print(re.findall(pattern1, str1)) #-->['：', '-']


# \s	匹配任意空白字符，等价于 [\t\n\r\f]。
print('-----\s	匹配任意空白字符，等价于 [\\t\\n\\r\\f]。------------')
pattern1 = r'\s'
str1 = '这 里\t是'
print(re.findall(pattern1, str1)) #-->[' ', '\t']

# \S	匹配任意非空字符
print('-----\S	匹配任意非空字符------------')
pattern1 = r'\S'
str1 = '这 里\t是'
print(re.findall(pattern1, str1)) #-->['这', '里', '是']


# \d	匹配任意数字，等价于 [0-9]。
print('-----\d	匹配任意数字，等价于 [0-9]。------------')
pattern1 = r'\d'
str1 = '这 11里\t是wyx18'
print(re.findall(pattern1, str1)) #-->['1', '1', '1', '8']

#\D	匹配任意非数字
print('-----\D	匹配任意非数字------------')
pattern1 = r'\D'
str1 = '这 11里\t是wyx18'
print(re.findall(pattern1, str1)) #-->['这', ' ', '里', '\t', '是', 'w', 'y', 'x']

#\A	匹配字符串开始
print('-----\A	匹配字符串开始------------')
pattern1 = r'里'
pattern2 = r'\A里'
pattern3 = r'\A这'
str1 = '这 11里\t是wyx18'
print(re.findall(pattern1, str1)) #-->['里']
print(re.findall(pattern2, str1)) #-->[]
print(re.findall(pattern3, str1)) #-->['这']


#\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
print('-----\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。------------')
pattern1 = r'\d'
pattern2 = r'\d\Z'
str1 = '这 11里\t是wyx18\n这 11'
print(re.findall(pattern1, str1)) #-->['1', '1', '1', '8', '1', '1']
print(re.findall(pattern2, str1)) #-->['1']

# #\z	匹配字符串结束
# print('-----\z	匹配字符串结束------------')
# pattern1 = r'\d'
# pattern2 = '\d\z'
# str1 = '这 11里是wyx18这 11'
# print(re.findall(pattern1, str1)) #-->['1', '1', '1', '8', '1', '1']
# print(re.findall(pattern2, str1)) #-->['1']

#\\G	匹配最后匹配完成的位置
# print('-----\G	匹配最后匹配完成的位置。------------')
# pattern1 = r'\d'
# pattern2 = r'\G(\d)'
# str1 = '这 11里\t是wyx18\n这 11'
# print(re.findall(pattern1, str1)) #-->['1', '1', '1', '8', '1', '1']
# print(re.findall(pattern2, str1)) #-->['1']


#\b	匹配一个单词边界，也就是指单词和空格间的位置。
# 例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
print('-----\\b	匹配一个单词边界，也就是指单词和空格间的位置。------------')
pattern2 = r'里\b'
str1 = '这 11里\t是wyx18\n里这 11里'
print(re.findall(pattern2, str1)) #-->['里', '里']  匹配到的是 里\t  和 最后的里


#\B	匹配非单词边界
# 'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
print('-----\\B	匹配非单词边界。------------')
pattern2 = r'里\B'
str1 = '这 11里\t是wyx18\n里这 11里'
print(re.findall(pattern2, str1)) #-->['里']匹配到的是 \n里这 的里


#\1...\9	匹配第n个分组的内容。
print('-----\1...\9	匹配第n个分组的内容。-----------')
pattern1 = r'(a)b(c|d)'
str1 = 'abcdabcdacbd'
result = re.match(pattern1, str1)
print(result) #--><re.Match object; span=(0, 3), match='abc'>