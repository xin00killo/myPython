#coding=utf-8
# __autor__='wyxces'

# 求列表中第二大的元素

##################通过list排序的方法   自己又想的
def maxN(mlist,n):
    if len(mlist)<2:
        result= -99999999
    l = []
    for x in list:
        l.append(x)
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] <= l[j]:
                l[i] = l[i] + l[j]
                l[j] = l[i] - l[j]
                l[i] = l[i] - l[j]
        # print(l)
        while(i == n-1):
            break
    result = l[n-1]
    return result


##################通过结合 字典的方式    网上找的
def second(ln):
    max = 0
    s = {}
    for i in range(len(ln)):
        flag = 0
        for j in range(len(ln)):
            # 每当当前的i值，比所有的其他值中，大于等于1次，flag就加1，可以得到当前这个数，在整个list中的排序
            if ln[i] >= ln[j] and i != j:
                flag = flag + 1
        s[i] = flag   # 向字典中加数据   i是索引，flag是值（对应 ln[i] 在整个list中第几大）
        # print('flag',flag,' ln[flag]',ln[flag-1],' ',s)
        if flag > max:
            max = flag  #如果 最大的数  比当前的flag值小，则 max = 当前的flag
            # print('max', max, ' ln[max]', ln[max-1], ' ', s)
    # print(s)
    # print('m2', max)
    for i in s:
        # print('i',i,'  s[i]', s[i])
        if s[i] == max - n + 1:  #当 值为倒数第n的时候的坐标
            # print('2222s[i]', s[i])
            break
    print(ln[i])



if __name__ == '__main__':
    list = [1,2,3,4,5,6,2,3]
    # list = [1]
    n = 5
    second(list)
    print('列表{}中倒数第{}大的元素为：{}'.format(list,n,maxN(list,n)))