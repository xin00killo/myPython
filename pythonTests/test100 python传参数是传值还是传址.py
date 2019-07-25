#coding:UTF-8
#__autor__='wyxces'


'''
100、python传参数是传值还是传址？
'''

'''
python中函数参数是引用传递（不是值传递），
对于不可变类型（数值、字符串、元组），因变量不能修改,所以运算不会影响到值本身；
而对于可变类型（列表、字典）来说，函数体运算，可能会更改传入的参数变量
'''

def fun(l):
    l += l
    print("fun:",l)

pInt = 5
print("原值：", pInt)
fun(pInt)
print("调用后的原值：",pInt)

pList = [5,6]
print("原值：", pList)
fun(pList)
print("调用后的原值：", pList)