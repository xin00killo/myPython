#coding:UTF-8
#__autor__='wyxces'

from functools import reduce


mylist = [1,2,3,4,5]
#  map(fun,list)将l列表的值，依次传入f函数中运算
def fun01(x):
    return x+1
print(list(map(fun01, mylist)))
print(list(map(str, mylist)))



#  reduce(fun,list)  f需要两个参数，将l的值，先传前两个-得出结果，再传结果和第3个
def fun02(x,y):
    return x*y
print(reduce(fun02, mylist))



# filter(fun,list) 过滤函数，函数f返回的true/false 确定l的每个值是否保留
def fun03(x):
    return x*3>10
print(list(filter(fun03, mylist)))

#sorted 排序
list04 = [1,2,6,-9,3,-1,-5,5]
print(sorted(list04))
print(sorted(list04, key=abs))


# lambda x,y : x+y  冒号前是参数，冒号后是表达式/函数  返回表达式的值
myLambad = lambda x,y:x+y
print(myLambad(11,16))


# filter函数。此时lambda函数用于指定过滤列表元素的条件
print(list(filter(lambda x:x*x>10,mylist)))

# sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则
print(sorted(list04, key=lambda x:abs(x+3)))

#map函数。此时lambda函数用于指定对列表中每一个元素的共同操作
print(list(map(lambda x:x+5,mylist)))

# reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件
print(reduce(lambda x,y:max(x,y), mylist))

