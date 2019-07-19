#coding:UTF-8
#__autor__='wyxces'
from functools import wraps

def singleton(cls):  # 创建外层函数，可以传入类
    _instance = {}  # 创建一个instances字典用来保存单例
    @wraps(cls)
    def getSingleton(*args, **kargs): # 创建一个内层函数来获得单例
        # 判断instances字典中是否含有单例，如果没有就创建单例并保存到instances字典中，然后返回该单例
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return getSingleton # 返回内层函数get_instance



@singleton
class C:
    def __init__(self,x):
        self.x = x


# 应用 single_decorator
c1 = C(1)
c2 = C(2)
print('c1:', c1.x,c1)
print('c2:', c2.x,c2)
'''
输出结果
c1: 1 <single_decorator.C object at 0x000000000214DC18>
c2: 1 <single_decorator.C object at 0x000000000214DC18>
'''