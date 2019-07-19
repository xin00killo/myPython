#coding:UTF-8
#__autor__='wyxces'

'''
69、请将[i for i in range(3)]改成生成器
'''
list = [i for i in range(3)]
gen = (i for i in range(3))
print(type(gen))

'''
<class 'generator'>
'''

