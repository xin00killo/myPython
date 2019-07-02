#coding=utf-8
# __autor__='wyxces'

'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

def myInsert(myList, num):
    length = len(myList)
    if myList[0] <=myList[length-1]:   #添加判断 数组排序规则判断语句
        for i in range(0,length):
            if num <= myList[i]:
                myList.insert(i,num)
                break
            elif i == length-1:
                myList.append(num)
    else:
        for i in range(0,length):
            if num > myList[i]:
                myList.insert(i,num)
                break
            elif i == length-1:
                myList.append(num)

    return myList

def getNum(num=None):
    num = input('请输入插入数组的数据:')
    if num.isdigit():
        # print('getNum-if', num, type(num))
        return int(num)
    else:
        # print('getNum-else', num)
        print('输入非法，请重新输入'.center(50,'-'))
        return getNum()

if __name__ == '__main__':
    myList = [1,3,5,6,9,11,15,16]
    # num = getNum()
    # print('num', num)
    myList = myInsert(myList, getNum())
    print('插入数据后的结果：\n\t',myList)
