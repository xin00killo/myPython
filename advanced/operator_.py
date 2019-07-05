#coding=utf-8
# __autor__='wyxces'


'''
如果你需要实现比较功能，需要引入 operator 模块，适合任何对象，包含的方法有：
lt(a,b) 相当于 a<b     从第一个数字或字母（ASCII）比大小
le(a,b)相当于a<=b
eq(a,b)相当于a==b     字母完全一样，返回True,
ne(a,b)相当于a!=b
gt(a,b)相当于a>b
ge(a,b)相当于 a>=b

函数的返回值是布尔哦 例如：
'''
from operator import  *


#
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'a':1, 'b':2, 'c':3}
dict3 = {'a':1, 'b':2}
print(eq(dict1, dict2))
print(eq(dict1, dict3))


a = 'a'
b = 'b'
print(eq(a,b))