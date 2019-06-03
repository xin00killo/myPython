#coding:UTF-8
#__autor__='wyxces'

import re

# re.search方法
# 1、扫描整个字符串 并返回第一个成功的匹配


print('-----re.search.span-------------------------------------------')
regex1 = 'www'
regex2 = 'com'
str = 'www.wyxces.com'
result1_1 = re.search(regex1, str)
result1_2 = re.search(regex1, str).span()
result2_1 = re.search(regex2, str)
result2_2 = re.search(regex2, str).span()
print('regex1:', regex1, '\nregex2:',regex2, '\nstr:',str)
print('re.search(regex1, str):', result1_1)
print('re.search(regex1, str).span():', result1_2)
print('re.search(regex2, str):', result2_1)
print('re.search(regex2, str).span():', result2_2)

regex3 = 'xyw'
print('regex3:', regex3, '\nstr:',str)
result3 = re.search(regex3, str)
print('re.search(regex3, str):', result3)


print('-----re.search.group----------网上拷贝的一个---------------------------------')
s = "[this is a book]"
PATTERN = "\[(((\w+)(\s+)?)+)\]"
print('regex:', PATTERN, '\nstr:',s)
m = re.search(PATTERN, s, re.DOTALL)
print(m)
if m:
    for i in range(5):
        print("m.group(%d) => '%s', start = %d, end = %d" % (i, m.group(i), m.start(i), m.end(i)))

    it = re.finditer("(\w+)(\s+)?", m.group(1))
    for search in it:
        print("m.group(1, 2) => '%s','%s'" % search.group(1, 2))