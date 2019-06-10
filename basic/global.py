#coding:UTF-8
#__autor__='wyxces'

'''
首先是pythond的一个奇异现象，在模块层面定义的变量（无需global修饰），
 如果在函数中没有再定义同名变量，可以在函数中当做全局变量使用：
'''
hehe=6
def f():
    print(hehe)
f()
print(hehe)


'''但如果在函数中有再赋值/定义（因为python是弱类型语言，
 赋值语句和其定义变量的语句一样），则会产生引用了未定义变量的错误：
 UnboundLocalError: local variable 'hehe' referenced before assignment
'''
# hehe=6
# def f():
#     print(hehe)
#     hehe=2
# f()
# print(hehe)

'''而如果在函数中的定义在引用前使用，
那么会正常运行但函数中的变量和模块中定义的全局变量不为同一个
'''
hehe=6
def f():
    hehe=2
    print(hehe)
f()
print(hehe)


'''
那么我们会有疑问，如果我可能在函数使用某一变量后又对其进行修改（也即再赋值），
怎么让函数里面使用的变量是模块层定义的那个全局变量而不是函数内部的局部变量呢？
这时候global修饰符就派上用场了。
'''
hehe=6
def f():
    global hehe
    print(hehe)
    hehe=3
f()
print(hehe)

'''
在用global修饰符声明hehe是全局变量的hehe后
（注意，global语句不允许同时进行赋值如global hehe=3是不允许的），
上述输出是6和3，得到了我们想要的效果。
'''