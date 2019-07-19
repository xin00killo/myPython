#coding:UTF-8
#__autor__='wyxces'
import threading
import time

class Singleton1(object):
    def __init__(self):
        time.sleep(1)
    @classmethod
    def instance(cls,*args, **kargs):
        if not hasattr(cls, "_instance"):
            Singleton1._instance = Singleton1(*args, **kargs)
        return Singleton1._instance


class Singleton2(object):
    #加锁
    _instance_lock = threading.Lock()
    def __init__(self):
        time.sleep(1)
    @classmethod
    def instance(cls,*args, **kargs):
        # 此时已经是单例模式了，则不加锁
        if not hasattr(cls, "_instance"):
            with Singleton2._instance_lock: # 加锁
                if not hasattr(Singleton2, "_instance"):
                    Singleton2._instance = Singleton2(*args, **kargs)
        return Singleton2._instance

def task1(arg):
    obj1 = Singleton1.instance()
    print('obj1:{}'.format(obj1))
def task2(arg):
    obj2 = Singleton2.instance()
    print('obj2:{}'.format(obj2))

for i in range(10):
    t = threading.Thread(target=task1,args=[i,])
    t.start()
for i in range(10):
    t = threading.Thread(target=task2,args=[i,])
    t.start()
time.sleep(5)
obj2 = Singleton2.instance()
print('obj2-2:{}'.format(obj2))


'''
运行结果：
obj1:<__main__.Singleton1 object at 0x000000000287B7F0>
obj1:<__main__.Singleton1 object at 0x00000000021C3320>
obj1:<__main__.Singleton1 object at 0x000000000287B8D0>
obj1:<__main__.Singleton1 object at 0x000000000287BA90>
obj1:<__main__.Singleton1 object at 0x000000000287B9B0>
obj1:<__main__.Singleton1 object at 0x000000000287BB70>
obj1:<__main__.Singleton1 object at 0x000000000287BC50>
obj1:<__main__.Singleton1 object at 0x000000000287BF28>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj1:<__main__.Singleton1 object at 0x000000000287BE10>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj1:<__main__.Singleton1 object at 0x000000000287BD30>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2:<__main__.Singleton2 object at 0x000000000288E080>
obj2-2:<__main__.Singleton2 object at 0x000000000288E080>
'''