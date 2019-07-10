#coding:UTF-8
#__autor__='wyxces'

'''
36、写一段自定义异常代码
'''
import random
str = 'qwr'
try:
    myInt = int(str)
    print('str:{}-int:{},转换成功！'.format(str,myInt))
except Exception as msg:
    print('str:{}-int:,转换失败！----{}'.format(str,msg))

print('---------------------------------------------------------------')

def fun():
    try:
        i = random.randint(1,100)
        if i % 2 == 1:
            raise Exception(' 不是偶数')
        else:
            print('i={},是偶数'.format(i))
    except Exception as e:
        print(i,e)

fun()