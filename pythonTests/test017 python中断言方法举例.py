#coding=utf-8
# __autor__='wyxces'

'''
17、python中断言方法举例
'''

def myAssert(m,n):
    try:
        assert (m == n) #这里需要判断条件
        print('m,n{},断言成功'.format(m,n))
    except Exception as msg:
        print('m,n{},断言失败'.format(m,n))

myAssert(12,"s")
