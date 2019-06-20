#coding:UTF-8
#__autor__='wyxces'

'''
1、一行代码实现1--100之和,利用sum()函数求和
'''

from functools import reduce

def sum01():# 循环相加
    sumrel = 0;
    for i in range(1,101):
        sumrel = sumrel+i
    print(sumrel)
sum01()

def sum02():# 利用sum 函数
    list = range(1,101)
    print( sum(list))
sum02()


def sum03():# reduce lambda函数
    list = [i for i in range(1, 101)]
    print(reduce(lambda x,y : x+y , list))
sum03()





