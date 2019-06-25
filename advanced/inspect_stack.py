#coding:UTF-8
#__autor__='wyxces'

import inspect # 自检查模块
'''
stack 	 堆栈
英 [stæk]  美 [stæk]
n. 	(通常指码放整齐的) 一叠，一摞，一堆; 大量; 许多; 一大堆; 
    (尤指工厂的) 大烟囱;
v. 	(使)放成整齐的一叠(或一摞、一堆) ; 
    使成叠(或成摞、成堆)地放在…; 使码放在…; 
    (令飞机) 分层盘旋等待着陆; 
'''
#获取函数的名字
def debug():
    print('inspect.stack()'.center(50,'-'))
    callnamer = inspect.stack()
    print('[debug] enter: {}'.format(callnamer))
    print(callnamer)
    print(callnamer[0])
    print(callnamer[1])
    print(callnamer[0][3])
    print(callnamer[1][4])
    for i in callnamer[0] :
        print('0-',i)
debug()

def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print ("[DEBUG]: enter {}()".format(caller_name))

def say_hello():
    debug()
    print ("hello!")

def say_goodbye():
    debug()
    print ("goodbye!")

if __name__ == '__main__':
    say_hello()
    say_goodbye()