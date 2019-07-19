#coding:UTF-8
#__autor__='wyxces'


'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
我们可以使用 list() 转换来输出列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
    zip 方法在 Python 2 和 Python 3 中的不同：在 Python 2.x zip() 返回的是一个列表。
    如果需要了解 Pyhton2 的应用，可以参考 Python zip()。
'''


print('---将对象中对应的元素打包成一个个元组-------------------------------------------')
list1 = [1,2]
list2 = [3,4]
tuple1 = (5,6)
zip1 = zip(list1,list2,tuple1)
new_list1 = list(zip1)
print(zip1,new_list1)

print('---如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同-------------------------------------------')
list3 = ['a','b','c','d']
zip3 = zip(list1,list3)
new_list3 = list(zip3)
print(zip3,new_list3)   # 元素个数与最短的列表一致   <zip object at 0x00000000005E6A88> [(1, 'a'), (2, 'b')]


print('---zip(l,l[1:])-------------------------------------')
list4 = ['a', 'b', 'c', 'd', 'e','f']
print (list4)
zip4 = zip(list4,list4[1:])
new_list4 = list(zip4)
print(zip4,new_list4)

print('---zip(* )------解压-------------------------------------')
unzip1 = zip(* new_list1)
zlist1 = list(unzip1)
print(unzip1, zlist1)
unzip3 = zip(* new_list3)
zlist3 = list(unzip3)
print(unzip3, zlist3)

print('---zip(* )------二维矩阵变换(矩阵的行列互换)-------------------------------------')
l1=[[1,2,3],[4,5,6],[7,8,9]]
print([[j[i] for j in l1] for i in range(len(l1[0]))])
for i in zip(*l1):
     i = list(i)
     print(i)


