#coding:UTF-8
#__autor__='wyxces'

'''
14、python中生成随机整数、随机小数、0--1之间小数方法
'''

import random

#整数
myInt = random.randint(1,100)


#小数
myFloat = random.uniform(1,10)


#0--1之间小数方法
myFloat2 = random.random()
myFloat3 = random.uniform(0,1)


print('整数:{}\n小数:{}\n0-1的小数1: {} , 2: {}'.format(myInt, myFloat, myFloat2,myFloat3))

