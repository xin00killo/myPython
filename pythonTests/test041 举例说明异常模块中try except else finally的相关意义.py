#coding:UTF-8
#__autor__='wyxces'


'''
41 举例说明异常模块中try except else finally的相关意义
'''

'''
try - 捕获异常
except - 
else - 如果没有异常，则执行
finally -  无论是否有异常都执行
'''

try:
    v = int("sdfj")
    print('这里是try部分，如果没有异常，应该会打印')
except Exception as e:
    print('这里是except部分，抛出异常，打印这里，异常信息：', e)
else:
    print('这里是else部分，嗯，没有异常会打印这里？')
finally:
    print('这里是fainally部分，无论如何都会打印吧?')

print('----------------------------------------------------------------------')
try:
    v = int("3")
    print('这里是try部分，如果没有异常，应该会打印')
except Exception as e:
    print('这里是except部分，抛出异常，打印这里，异常信息：', e)
else:
    print('这里是else部分，嗯，没有异常会打印这里？')
finally:
    print('这里是fainally部分，无论如何都会打印吧?')