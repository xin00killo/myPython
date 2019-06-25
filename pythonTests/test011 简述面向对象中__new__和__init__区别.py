#coding:UTF-8
#__autor__='wyxces'

'''
11、简述面向对象中__new__和__init__区别
'''
import inspect

'''
__new__:创建对象时调用，会返回当前对象的一个实例
__init__:创建完对象后调用，对当前对象的一些实例初始化，无返回值

在类中，如果__new__和__init__同时存在，会优先调用__new__
__new__方法会返回所构造的对象，__init__则不会。__init__无返回值
如果__new__返回一个对象的实例，会隐式调用__init__
如果__new__不返回一个对象的实例，__init__不会被调用

object.__init__(self[, ...])
# 在对象的实例创建完成后调用。参数被传给类的构造函数。如果基类有__init__方法，子类必须显示调用基类的__init__。
# 没有返回值，否则会再引发TypeError错误。




__new__和__init__参数的不同
__new__所接收的第一个参数是cls，而__init__所接收的第一个参数是self。
这是因为当我们调用__new__的时候，该类的实例还并不存在（也就是self所引用的对象还不存在），
所以需要接收一个类作为参数，从而产生一个实例。
而当我们调用__init__的时候，实例已经存在，
因此__init__接受self作为第一个参数并对该实例进行必要的初始化操作。
这也意味着__init__是在__new__之后被调用的。

__new__作为构造器，起创建一个类实例的作用。而__init__作为初始化器，起初始化一个已被创建的实例的作用。
'''

print('在类中，如果__new__和__init__同时存在，会优先调用__new__'.center(100,'-'))
class Data(object):
    def __new__(self):
        print ("new")
    def __init__(self):
        print ("init")
print ('源码：\n',inspect.getsource(Data))  # failed
print('调用：\nData():')
Data()


print('__new__方法会返回所构造的对象，__init__则不会。__init__无返回值'.center(100,'-'))
# class Data(object):
#     def __init__(cls):
#         cls.x = 2
#         print ("init")
#         return cls
# Data() #TypeError: __init__() should return None, not 'Data'

class Data(object):
    def __new__(cls):
        print ("new")
        cls.x = 1
        return cls
    def __init__(self):
        print('init')


data = Data()
print(data.x)
data.x = 3
print(data.x)





print('如果__new__返回一个对象的实例，会隐式调用__init__'.center(100,'-'))
class A(object):
    def __new__(cls):
        object = super(A,cls).__new__(cls)
        print ('... new')
        return object
    def __init__(self):
        print('... init')
A()

print('如果__new__不返回一个对象的实例，__init__不会被调用'.center(100,'-'))
class A(object):
    def __new__(cls):
        print ('... new')
        return cls
    def __init__(self):
        print('... init')
A()


# 在对象的实例创建完成后调用。参数被传给类的构造函数。如果基类有__init__方法，子类必须显示调用基类的__init__。
# 没有返回值，否则会再引发TypeError错误。