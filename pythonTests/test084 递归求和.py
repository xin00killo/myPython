#coding:UTF-8
#__autor__='wyxces'

'''
84、递归求和
'''

def mySum(l,result=0):
    result = result + l[0]
    while(len(l) - 1 != 0 ):
        return mySum(l[1:],result)
    return result

sum = mySum([1,2,3,4,5,6])
print(sum)