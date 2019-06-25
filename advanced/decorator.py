#coding=utf-8
# __autor__='wyxces'

'''decorator 装饰器
'''
import datetime

print('添加功能的方式，添加一个基础装饰器'.center(50,'-'))
def debug(func):
    def wrapper():
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print ("hello!")
say_hello = debug(say_hello)  # 添加功能并保持原函数名不变
say_hello()



print('@语法糖的方式，添加一个基础装饰器'.center(50,'-'))
@debug
def say_hello2():
    print ("hello2!")
say_hello2()



print('被装饰的函数需要传入参数'.center(50,'-'))
def debug3(func):
    def wrapper(something):  # 指定一毛一样的参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数

@debug3
def say_hello3(something):
    print ("hello3 {}!".format(something))
say_hello3(99)



print('被装饰的函数需要传入参数-参数N多个'.center(50,'-'))
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




#带参数的装饰器
print('带参数的装饰器'.center(50,'-'))
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print ("say {}!".format(something))

@logging(level='DEBUG')
def do(something):
    print('do {} ...'.format(something))
if __name__ == '__main__':
    say('something say')
    do('something do')



print('基于类实现的装饰器'.center(50,'-'))
class logging(object):
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("[Debug]: enter {func}()".format(func=self.func.__name__))
        return self.func(*args, **kwargs)
@logging
def say(something):
    print ("say {}!".format(something))
if __name__ == '__main__':
    say('something')



print('带参数的类装饰器'.center(50,'-'))
class logging(object):
    def __init__(self, level= 'INFO'):
        self.level = level
    def __call__(self,func): # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: enter {func}()".format(
                level=self.level,
                func=func.__name__))
            return func(*args, **kwargs)
        return wrapper
@logging('DEBUG')
def say(something):
    print ("say {}!".format(something))
if __name__ == '__main__':
    say('something')



print('内置装置器@property 属性'.center(50,'-'))
'''
cdef getx(self):
    return self._x
def setx(self, value):
    self._x = value
def delx(self):
    del self._x
# create a property
x = property(getx, setx, delx, "I am doc for x property")
print(x)
'''
@property
def x(self): ...
print(x)



print('装饰器函数调用顺序'.center(50,'-'))
def html_tags(tag_name):
    print ('begin outer function.')
    def wrapper_(func):
        print ("begin of inner wrapper function.")
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            print ("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
        print ('end of inner wrapper function.')
        return wrapper
    print ('end of outer function')
    return wrapper_

@html_tags('b')
def hello(name='Toby'):
    return 'Hello {}!'.format(name)

hello('hello001')
hello('hello002')



print('错误的函数签名和文档'.center(50,'-'))
def logging(func):
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print ("[DEBUG]: enter {}()".format( func.__name__))
        return func(*args, **kwargs)
    return wrapper


@logging
def say(something):
    print ("say {}!".format(something))
say('错误的函数签名和文档')
print (say.__name__ ) # say
print (say.__doc__ )# say something



print('使用标准库里的functools.wraps，可以基本解决这个问题'.center(50,'-'))
from functools import wraps
def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """print log before a function."""
        print ("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper
@logging
def say(something):
    """say something"""
    print ("say {}!".format(something))
say('使用标准库里functools.wraps')
print (say.__name__ ) # say
print (say.__doc__ )# say something

import inspect
# print (inspect.getargspec(say))  # failed
print ('源码：\n',inspect.getsource(say))  # failed



# 怎么感觉 py3  这里不报错了。。。
print('不能装饰@staticmethod 或者 @classmethod'.center(50,'-'))
class Car(object):
    def __init__(self, model):
        self.model = model
    @logging  # 装饰实例方法，OK
    def run(self):
        print ("{} is running!".format(self.model))

    @logging  # 装饰静态方法，Failed
    @staticmethod
    def check_model_for(obj):
        if isinstance(obj, Car):
            print ("The model of your car is {}".format(obj.model))
        else:
            print ("{} is not a car!".format(obj))