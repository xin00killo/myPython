#coding:UTF-8
#__autor__='wyxces'

import threading
import time

class Singleton(type):
    _instance_lock = threading.Lock()
    def __init__(self, *args, **kwargs):
        time.sleep(1)

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass= Singleton):
    print('foo')



def task(arg):
    f = Foo()
    print(f)
for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

