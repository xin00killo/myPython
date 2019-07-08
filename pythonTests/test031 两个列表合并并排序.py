#coding=utf-8
# __autor__='wyxces'


'''
31 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
'''


list1 = [1,5,7,9]
list2 = [2,2,6,8,13]

list3 = sorted(list1+list2)
print(list3)

print('--------------------------------------------------')

list1 = [1,5,7,9]
list2 = [2,2,6,8,13]
list1.extend(list2)
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print(list1)

print('--------------------------------------------------')

list1 = [1,5,7,9]
list2 = [2,2,6,8,13]

for l2 in list2:
    for l1 in list1:
        if l2 <= l1:
            list1.insert(list1.index(l1),l2)
            break
        elif list1.index(l1) ==len(list1)-1:
            list1.append(l2)
            break
print(list1)


