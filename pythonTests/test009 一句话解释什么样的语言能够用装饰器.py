#coding=utf-8
# __autor__='wyxces'

'''
9、一句话解释什么样的语言能够用装饰器?

函数可以作为参数传递的语言,可以使用装饰器
'''


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
