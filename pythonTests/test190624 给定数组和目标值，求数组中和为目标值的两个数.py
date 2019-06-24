#coding:UTF-8
#__autor__='wyxces'


'''
给定一个整数数组nums 和 一个目标值target ，
请你再该数组中找出和为目标值的 那两个整数，并返回他们的数组下标

你可以假设每种输入只会对应一个答案。 但是，你不能重复利用这个数组中同样的元素
'''

#假设每种输入只会对应一个答案
def fun1(nums,target):
    for i in range(0,len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return -99, -99

print('假设每种输入只会对应一个答案'.center(50,'-'))
nums = [2,3,5,7,11,15]
target = 9
x,y = fun1(nums,target)
print('坐标nums(%d,%d)：%d + %d = %d' % (x, y, nums[x], nums[y], target))


#假设每种输入会对应多个答案 , 不能重复利用数组中同样的元素
def fun1(nums,target):
    result = []
    for i in range(0,len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                result.append((i,j))
    return result

print('假设每种输入会对应多个答案'.center(50,'-'))
nums = [2,3,5,7,6,15]
target = 9
result = fun1(nums,target)
for i in result:
    print('坐标nums(%d,%d)：%d + %d = %d'%(i[0],i[1],nums[i[0]],nums[i[1]],target))


'''运行结果：
------------------假设每种输入只会对应一个答案------------------
坐标nums(0,3)：2 + 7 = 9
------------------假设每种输入会对应多个答案-------------------
坐标nums(0,3)：2 + 7 = 9
坐标nums(1,4)：3 + 6 = 9
'''