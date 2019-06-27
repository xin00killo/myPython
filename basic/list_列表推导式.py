#coding:UTF-8
#__autor__='wyxces'

'''
python中列表推导式用于使用其他列表创建一个新列表。
其基本形式为： [表达式 for 变量 in 列表]
'''


# 得到1-10的平方组成的list
list01 = [x*x for x in range(1,11)]
print(list01)


# 对原列表进行变换和筛选。
#筛选出1-10中偶数的平方
list02 = [x*x for x in range(1,11) if x%2 == 0]
print(list02)


# 对多重嵌套的list进行变换筛选
list03 = [[1,2,3],[4,5,6],[7,8,9],[10]]
list0301 = [i for i in list03 ]
print(list0301)
list0302 = [j for i in list03 for j in i]
print(list0302)
list0303 = [j for i in list03 for j in i if j%2 == 0]
print(list0303)



#想得到多重嵌套的list中一重嵌套中list长度大于1
# 的list中的数为偶数list
list04 = [j for i in list03 if len(i)>1 for j in i if j%2 == 0]
print(list04)


