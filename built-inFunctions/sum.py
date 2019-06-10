#coding:UTF-8
#__autor__='wyxces'

'''
sum(iterable[, start])
iterable  -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。
'''

list = range(1, 11)
print(sum(list))

print(sum(list,999))  # 列表计算总和后再加 999

# print(sum(1,2))  # TypeError: 'int' object is not iterable