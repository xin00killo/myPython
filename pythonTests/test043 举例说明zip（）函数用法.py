#coding:UTF-8
#__autor__='wyxces'

'''
43 举例说明zip（）函数用法
'''

'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
'''

list1 = [1,2]
list2 = [3,4]
tuple1 = (5,6)
zip1 = zip(list1,list2,tuple1)
new_list1 = list(zip1)
print(zip1,new_list1) #<zip object at 0x00000000005E6A08> [(1, 3, 5), (2, 4, 6)]

print('----------------------------------------------')
list3 = ['a','b','c','d']
zip3 = zip(list1,list3)
new_list3 = list(zip3)
print(zip3,new_list3)   # 元素个数与最短的列表一致   <zip object at 0x00000000005E6A88> [(1, 'a'), (2, 'b')]

