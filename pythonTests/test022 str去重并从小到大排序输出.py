#coding=utf-8
# __autor__='wyxces'


'''
22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
'''


s = 'ajldjlajfdljfddd'

def fun1(str):
    l1 = list(set(str))
    l1.sort()
    return l1

def fun2(str):
    l2 = list(str)
    l2 = []
    for x in str:
        if x not in l2:
            l2.append(x)
    # print('l2',l2)
    for i in range(0,len(l2)-1):
        for j in range(i+1,len(l2)):
            if l2[i] > l2[j]:
                t = l2[i]
                l2[i]=l2[j]
                l2[j]=t
    return l2



print('fun1',fun1(s))
print('fun2',fun2(s))

