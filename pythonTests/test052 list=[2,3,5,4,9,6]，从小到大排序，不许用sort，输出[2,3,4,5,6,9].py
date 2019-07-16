#coding:UTF-8
#__autor__='wyxces'


'''
52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
'''

def mySort(list):
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

mylist=[2,3,5,4,9,6]
print(mylist)
mylist = mySort(mylist)
print(mylist)