#coding=utf-8
# __autor__='wyxces'

'''decorator 装饰器
'''
def debug(func):
    def wrapper():
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print ("hello!")
say_hello = debug(say_hello)  # 添加功能并保持原函数名不变
say_hello()

@debug
def say_hello2():
    print ("hello2!")
say_hello2()

def debug3(func):
    def wrapper(something):  # 指定一毛一样的参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数

@debug3
def say_hello3(something):
    print ("hello3 {}!".format(something))
say_hello3(99)


def debug4(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print ('Prepare and say...',)
        return func(*args, **kwargs)
    return wrapper  # 返回


kwargsDict = {'a':1,'b':2, 'c':3}
@debug4
def say_hello4(*args, **kwargs):
    print ("hello {}{}!".format(args, kwargs))
say_hello4(1,2,3, **kwargsDict)