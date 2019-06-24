#coding=utf-8
# __autor__='wyxces'

'''
thon format 格式化函数
'''


print("{} {}".format("hello", "world") ) # 不设置指定位置，按默认顺序

print("{0} {1}".format("hello", "world") ) # 设置指定位置
print( "{1} {0} {1}".format("hello", "world") ) # 设置指定位置
#设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

#向 str.format() 传入对象：
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

#数字格式化
print("{:.2f}".format(3.1415926))

#大括号
print ("{} 对应的位置是 {{0}}".format("runoob"))

'''
hello world
hello world
world hello world
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
网站名：菜鸟教程, 地址 www.runoob.com
value 为: 6
3.14
runoob 对应的位置是 {0}
'''