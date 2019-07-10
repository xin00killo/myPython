#coding:UTF-8
#__autor__='wyxces'

'''
42 python中交换两个数值
'''



a = 5
b = 6
print('a-{},b-{}'.format(a,b))
temp = a
a = b
b = temp
print('a-{},b-{}'.format(a,b))
print('------------------------------------------------')
c = 9
d = 10
print('c-{},d-{}'.format(c,d))
c = c + d
d = c - d
c = c - d
print('c-{},d-{}'.format(c,d))
