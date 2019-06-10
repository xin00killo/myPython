#coding:UTF-8
#__autor__='wyxces'

from functools import reduce

'''
reduce(function,list)
function需要两个参数，将list的值，先传前两个-得出结果，再传结果和第3个


'''


list = [2,3,5,6,356,59,5]
result = reduce(max, list)
print(result)



list = [i for i in range(1,10)]
result = reduce(max, list)
print(result)

