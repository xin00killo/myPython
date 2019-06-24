#coding:UTF-8
#__autor__='wyxces'
'''
7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
'''

#*args  可变参数  可以接受0~多个值
argsList = [1,2,3,5]
argsList2 = [2,4,6,8]

def fun(a,*args):
    print('a:',a)
    print('*args', *args)
    print('args', args)
    for arg in args:
        print(arg)
print('fun(1)'.center(50,'-'))
fun(1)
print('fun(1, argsList)'.center(50,'-'),argsList)
fun(1, argsList)
print('fun(1, argsList,argsList2)'.center(50,'-'),argsList,argsList2)
fun(1, argsList,argsList2)
print('fun(1, 1,2,3,5)'.center(50,'-'))
fun(1,1,2,3,5)






#**kwargs   关键字参数  传入字典
kwargsDict = {'a':1,'b':2, 'c':3}
def fun(**mydicts):
    # print('**mydict', **mydicts)
    print('mydict', mydicts)
    for key,value in mydicts.items():
        print(key,value)
print('fun(**kwargsDict)'.center(50,'-'),kwargsDict)
fun(**kwargsDict)


