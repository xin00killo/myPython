#coding:UTF-8
#__autor__='wyxces'


# 定义集合   序列是无序的，不能够重复的，所以可以用它的强制类型转换来去重
set1 = {1,5,9,6,4,3,8,12}
print('初始的集合数据为：', set1)

# 将n加到集合中
set1.add(99)
print('将99 加入到集合中后：', set1)

# 将集合中的n移除，如果不存在，则报keyerror错误
try:
    set1.remove(5)
    print('将集合中的5移除', set1)
    set1.remove(15)
    print('将集合中的15移除', set1)
except KeyError as msg:
    print('KeyError:集合中没有',msg)

# 将集合中的n移除，不存在也不报错
num = 15
set1.discard(num)
print('移除%s后的，set：%s'% (num, set1))
num = 9
set1.discard(num)
print('移除%s后的，set：%s'% (num, set1))


# 检查元素是否在集合中
print('99 在集合中:', 99 in set1)
print('99 不在集合中:', 99 not in set1)

# 清空集合
set1.clear()
print('集合清空后为：', set1)

'''
初始的集合数据为： {1, 3, 4, 5, 6, 8, 9, 12}
将99 加入到集合中后： {1, 3, 4, 5, 6, 99, 8, 9, 12}
将集合中的5移除 {1, 3, 4, 6, 99, 8, 9, 12}
KeyError:集合中没有 15
移除15后的，set：{1, 3, 4, 6, 99, 8, 9, 12}
移除9后的，set：{1, 3, 4, 6, 99, 8, 12}
99 在集合中: True
99 不在集合中: False
集合清空后为： set()
'''
