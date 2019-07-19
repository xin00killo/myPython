#coding:UTF-8
#__autor__='wyxces'



dic = {'d':'d','a':'a','f':'f'}


'''77、根据键对字典排序（方法一，zip函数）'''
list1 = list(zip(dic.keys(),dic.values()))
new_list1 = sorted(list1,key=lambda x:x[0])
new_dic1 = {i[0]:i[1] for i in new_list1}
print(new_dic1)


'''78、根据键对字典排序（方法二,不用zip)'''
# -------------只取key，排序后重新组装字典-------------
list2 = [i for i in dic.keys()]
list2.sort()
new_dic2={}
for i in list2:
    new_dic2[i]=dic[i]
print(new_dic2)
# -------------用列表推导式转换成元组-------------
list3 = [i for i in dic.items()]
list3.sort(key=lambda x:x[0])
new_dic3 = {i[0]:i[1] for i in list3}
print(new_dic3)
