#coding:UTF-8
#__autor__='wyxces'

'''
70、a = "  heh heh  ",去除收尾空格
'''
import re
a = "  heh   heh  "

#正则1
new_a = ''.join(re.findall(r'\s+(\w.*\w)\s+',a))
print(new_a)

#正则2
new_a3 = re.sub(r'^(\s+)|(\s+)$','',a)
print(new_a3)

#方法3  strip
new_a2 = a.strip()
print(new_a2)


#递归调用
def trim(a):
    if re.match(r'\s',a[0]):
        return trim(a[1:])
    elif re.match(r'\s',a[-1]):
        return trim(a[:-1])
    else:
        return a

print(trim(a))



'''
运行结果
heh   heh
heh   heh
heh   heh
heh   heh
'''