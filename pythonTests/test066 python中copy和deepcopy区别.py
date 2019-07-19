#coding:UTF-8
#__autor__='wyxces'


'''
66、python中copy和deepcopy区别
'''

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



