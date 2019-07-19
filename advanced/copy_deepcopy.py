#coding:UTF-8
#__autor__='wyxces'

'''
对于嵌套列表：
deepcopy：独立的新个体单独存在
copy:嵌套列表中的子列表未能独立存在
'''
import copy

origin  = [1,2,[3,4]]
copy1 = copy.copy(origin)
copy2 = copy.deepcopy(origin)
print('origin:{}\ncopy1:{}\ncopy2:{}\ncopy1==copy2:{}\ncopy1 is copy2:{}'.format
      (origin,copy1,copy2,copy1==copy2,copy1 is copy2))
# 修改 origin 的元素
origin[2][0] = "new3"
origin[1] = "new1"
print('修改origin后再次打印：\n\torigin:{}\n\tcopy1:{}\n\tcopy2:{}'.format
      (origin,copy1,copy2))

'''
运行结果“
origin:[1, 2, [3, 4]]
copy1:[1, 2, [3, 4]]
copy2:[1, 2, [3, 4]]
copy1==copy2:True
copy1 is copy2:False
修改origin后再次打印：
	origin:[1, 'new1', ['new3', 4]]
	copy1:[1, 2, ['new3', 4]]
	copy2:[1, 2, [3, 4]]
'''

print("=========python的数据存储方式,解析「假」copy 问题==================================")
a = [1, 2, 3]  # 给 [1, 2, 3]  贴一个标签a
b = a #再贴一个标签
a = [4, 5, 6] # 把 a 标签从 [1 ,2, 3] 上撕下来，贴到了 [4, 5, 6] 上
print('a:',a,'b:',b)  # a 的值改变后，b 并没有随着 a 变

c = [1, 2, 3]  # 给 [1, 2, 3]  贴一个标签c
d = c #再贴一个标签
c[0], c[1], c[2] = 4, 5, 6 #改变原来 list 中的元素  标签还是那个标签
print('c:',c,'d:',d)


'''对于子对象，python会把它当作一个公共镜像存储起来，
所有对他的复制都被当成一个引用，
所以说当其中一个引用将镜像改变了之后另一个引用使用镜像的时候镜像已经被改变了。'''

