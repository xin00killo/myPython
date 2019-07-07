#coding=utf-8
# __autor__='wyxces'
from collections import Counter




# 创建
'''
c=Counter()#创建一个空的Counter类
c=Counter('gallahad')#从一个可iterable对象（list、tuple、dict、字符串等）创建
c=Counter({'a':4,'b':2})#从一个字典对象创建
c=Counter(a=4,b=2)#从一组键值对创建
'''
str = "asasfssffaaaa"
c = Counter(str)
print('c = Counter(str)--c:', c)
#访问
print('c = Counter(str)--c["s"]:', c["s"])
print('访问不存在的qww -- c["qww"]:', c["qww"])

str2 = '1212121333aaaass'
#增加
c.update(str2)
print('c.update(str2)--c:', c)
print('c.update(str2)--c["s"]:', c["s"])
#减少
c.subtract(str)
print('c.subtract(str)--c:', c)
print('c.subtract(str)--c["s"]:', c["s"])
c.subtract(str)
print('再次c.subtract(str)--c:', c)
print('再次c.subtract(str)--c["s"]:', c["s"])

#删除
del c["s"]
print('del c["s"]-c:', c)
print('del c["s"]--c["s"]:', c["s"])


#elements  返回把一个迭代，不包含小于1的元素
print('list(c.elements()):', list(c.elements()))
# for e in c.elements():
#     print(e)

#返回前n多的元素，当多个元素计数值相同时，排列是无确定顺序的。
print('c.most_common():', c.most_common())
print('c.most_common(1):', c.most_common(1))
print('c.most_common(2):', c.most_common(2))
print('c.most_common(3):', c.most_common(3))

#取出计数最少的n-1个元素
print('c.most_common()[:-2:-1]:', c.most_common()[:-2:-1])
print('c.most_common()[-2]:', c.most_common()[-2])

#类方法
'''
+、    # c[x] + d[x]
-、      subtract（只保留正数计数的元素）
&、    交集并返回各元素最小值:  min(c[x], d[x]) 
|      并集并返回各元素最大值:  max(c[x], d[x])
'''
m = Counter(a=3, b=1)
n = Counter(a=1, b=2)
print('m:{}\nn:{}'.format(m,n))
print('m+n', m+n)
print('m-n', m-n)
print('m&n', m&n)
print('m|n', m|n)


#所有计数的总数
print('c:', c)
print('所有技术的总数sum', sum(c.values()))

# list(c)  将c中的键转为列表
print('list(c):',list(c))
# set(c)  将c中的键转为set
print('set(c):',set(c))
# dict(c)  将c中的键值对转为字典
print('dict(c):',dict(c))
#转为(elem, cnt)格式的列表
print('c.items():', c.items())

# 移除0和负值
c = c+Counter()   # 或者写成 c+= Counter
print('c:', c)

#  重置Counter对象，注意不是删除
c.clear()
print('c:', c)

