#coding:UTF-8
#__autor__='wyxces'


# 生成1个list?
list1 = range(1,11)
print('list1', type(list1),list1)   # <class 'range'>

# 生成1个list    这个方法叫做函数推导式
list2 = [i for i in range(1,101)]
print('list2', type(list2),list2)    # <class 'list'>

# 生成1给list
list0 = list(range(1,11))
print('list0', type(list0),list0)    # <class 'list'>

# 列表切片
list3 = list2[2:51:3]
print('list3 , 取2-51，步长3：', list3)

# 倒数第n个元素
print('倒数第10个元素：', list2[-10])

# 向列表追加数据n，无返回
list3.append(11)
print('追加11后的列表list3', list3)

# 求列表中的最大值，返回值
maxList3 = max(list3)
print('list3中的最大值为：', maxList3)

# 求列表中的最小值，返回值
minList3 = min(list3)
print('list3中的最小值为：', minList3)

# 求列表的长度，返回值
lenList3 = len(list3)
print('list3列表的长度为：', lenList3)

# 移除列表中指定的元素n，并返回移除元素的值
pop1 = list3.pop(1)
print('list3移除列表中下标为1的元素%d，移除后列表为：%s'%(pop1, list3))

# 移除列表中指定的元素51，无返回
list3.remove(51)
print('list3移除列表中指定的元素51, 移除后列表为：%s'%(list3))

# 删除列表中下标为n的元素
del list3[0]
print('list3删除列表中下标为0的元素：', list3)

# 反转,无返回
list3.reverse()
print('.reverse()反转后的数据为：', list3)

# 反转,有返回，返回一个生成器
print('reversed反转后的数据为：' )
for x in reversed(list3):
    print(x)


# 返回排序结果，不改变原列表
print('排序：', sorted(list3), '列表：', list3)

# 排序，无返回
list3.sort()
print('排序后的数据为：', list3)

# 返回元素n的下标值
index18 = list3.index(18)
print('元素 18 的下标值：', index18)


# 在m位置的前面插入数据n
list3.insert(4,66)
print('在坐标4的数据前，插入数据66：', list3)

# 将列表list2连接到list1
list4 = list2[10:15:1]
print('将列表 list4：%s,连接到列表list3：%s'% (list4,list3))
list3.extend(list4)
print('\t结果为：%s'% list3)

# 返回数据n在列表中出现的次数
count12 = list3.count(12)
print('数据12在列表中出现的次数:', count12)

# 检查元素是否出现在列表中
print('元素18在列表中：', 18 in list3)
print('元素18不在列表中：', 18 not in list3)

# 清空列表
list3.clear()
print('列表清空后为：', list3)

'''
list1 <class 'type'> range(1, 11)
list2 <class 'type'> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
list3 , 取2-51，步长3： [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
倒数第10个元素： 91
追加11后的列表list3 [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 11]
list3中的最大值为： 51
list3中的最小值为： 3
list3列表的长度为： 18
list3移除列表中下标为1的元素6，移除后列表为：[3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 11]
list3移除列表中指定的元素51, 移除后列表为：[3, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 11]
list3删除列表中下标为0的元素： [9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 11]
反转后的数据为： [11, 48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9]
排序： [9, 11, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48] 列表： [11, 48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9]
排序后的数据为： [9, 11, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
元素 18 的下标值： 4
在坐标4的数据前，插入数据66： [9, 11, 12, 15, 66, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
将列表 list4：[11, 12, 13, 14, 15],连接到列表list3：[9, 11, 12, 15, 66, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
	结果为：[9, 11, 12, 15, 66, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 11, 12, 13, 14, 15]
数据12在列表中出现的次数: 2
元素18在列表中： True
元素18不在列表中： False
列表清空后为： []
'''