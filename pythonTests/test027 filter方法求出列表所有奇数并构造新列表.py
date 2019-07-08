#coding=utf-8
# __autor__='wyxces'

'''
27  filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newA = list(filter(lambda x:x%2==1,a))
print(newA)
