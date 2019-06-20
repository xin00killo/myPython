#coding:UTF-8
#__autor__='wyxces'
'''
6、python实现列表去重的方法
'''

mylist = [1,3,5,6,'ee','6',6,'ee','y','1',90,'a','y']

print('原list: \n\t', mylist)

# 通过set 集合不包含重复元素的特性，转换，去重
mylist = list(set(mylist))
print('去重后的list: \n\t', mylist)