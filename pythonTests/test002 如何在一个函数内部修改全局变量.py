#coding:UTF-8
#__autor__='wyxces'

'''
2、如何在一个函数内部修改全局变量
利用global 修改全局变量
'''

from basic import global_

g1 = 'g1.1'
print("g1 = 'g1':",g1)


class Test002_1:
    g2 = 'g2.1'
    print("g2 = 'g2':", g2)
    def modify(self):
        g1 = 'g1.1-m'
        print("modify g1",g1)
        g2 = 'g2.1-m'
        print("modify g2", g2)
    def __str__(self):
        return ('__str__,g1:%s, g2:%s'%(g1,self.g2))



class Test002_2:
    g2 = 'g2.2'
    print("g2 = 'g2':", g2)
    g3 = 'g3.2'
    def modify(self):
        global g1
        global g2
        g1 = 'g1.2-m'
        print("modify g1",g1)
        g2 = 'g2.2-m'
        print("modify g2", g2)
        self.g3 = 'g3.2-m'
        print("modify self g2", self.g3)

    def __str__(self):
        return ('__str__,g1:%s, g2:%s, g3:%s'%(g1,self.g2, self.g3))



if __name__ == '__main__':
    print('----------Test002_1----------------')
    t1 = Test002_1()
    print(t1)
    t1.modify()
    print(t1)


    print('----------Test002_2----------------')
    t2 = Test002_2()
    print(t2)
    t2.modify()
    print(t2)
