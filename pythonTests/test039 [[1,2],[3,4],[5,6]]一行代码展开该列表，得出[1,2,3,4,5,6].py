#coding:UTF-8
#__autor__='wyxces'

'''
39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
'''

list1 = [[1,2],[3,4],[5,6]]


print('--------------------------------------')
list2 = []
for l in list1:
    list2 = list2 + l
print(list2)


print('--------------------------------------')
list2 = [l for l1 in list1 for l in l1]
print(list2)