#coding:UTF-8
#__autor__='wyxces'

'''
13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，
并使用列表推导式提取出大于10的数，最终输出[16,25]
'''


def myfun(x):
    result = x*x
    return result

list1 = [1,2,3,4,5]

#请使用map()函数输出[1,4,9,16,25]
list2 = list(map(myfun, list1))
print(list2)

#使用列表推导式提取出大于10的数，最终输出[16,25]
list3 = [i for i in list2 if i>10]
print(list3)


'''
[1, 4, 9, 16, 25]
[16, 25]
'''