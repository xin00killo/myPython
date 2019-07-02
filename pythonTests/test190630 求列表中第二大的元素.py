#coding=utf-8
# __autor__='wyxces'

# 求列表中第二大的元素

def maxN(list, n ):
    if len(list)<2:
        return -99999
    else:
        l = sorted(list)
        max_n = n * (-1)
        return l[max_n]

if __name__ == '__main__':
    list = [1,5,6,9,3,45,6,3,4]
    n = 2
    print('列表{}中倒数第{}大的元素为：{}'.format(list,n,maxN(list,n)))