#coding=utf-8
# __autor__='wyxces'


'''
给定两个整数 A 和 B，返回任意字符串 S，要求满足:
S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 没有出现在 S 中；
子串 'bbb' 没有出现在 S 中。
'''

#   输入不含3a3b的函数文件  本文件的文件名为:strWithout3a3b
# 1 判断AB的输入需要满足 0-100的整数
# 2 确保AB输入后可以生成S
# 3 生成包含A个a，B个b的列表，合并AB，最后用aab  或则abb 替换 abs(A-B-2/A-B)次的 ab
import random, re

def strWithout3a3b(A, B):
    flag = False
    S = "error"
    if 0<= A <=100 and 0<= B <=100:  # 判断A,B 的输入是否满足条件
        # 确保AB输入后可以生成S
        if (A >= B and A <= (B * 2 + 2)) or (A < B and (A * 2 + 2) >= B):
           flag = True
    if flag:
        # 生成含有A个a 和 B个b 的列表  
        A_list = [random.choice("a") for _ in range(A)]
        print('A_list',A_list)
        B_list = [random.choice("b") for _ in range(B)]
        print('B_list',B_list)
        # 组合AB 获取到全部是 [(a,b),(a,b)] 的列表
        AB_list = zip(A_list, B_list)
        print('AB_list',AB_list)
        S_list = [l for ll in AB_list for l in list(ll)]
        print('S_list',S_list)
        S = "".join(S_list)
        print('S',S)
        # 由于zip后只ab个数按最小的来，所以 要把少掉利用 替换 替换回来
        if A > B:
            if A - B > 2:
                S = re.sub("ab", "aab", S, A - B - 2)
                S = S+"aa"
            else:
                S = re.sub("ab", "aab", S, A - B)
        elif A < B:
            if B - A > 2:
                S = re.sub("ab", "abb", S, B - A - 2)
                S = "bb"+S
            else:
                S = re.sub("ab", "abb", S, B - A)
    return S


#        网上查到的
def strWithout3a3b2(A, B):
    flag = False
    S = ""
    c = 0
    if not 0<= A <=100 and 0<= B <=100:
        S = "error"
    while(True):
        c +=1
        count = 0
        if A>B and not flag:
            while A>0 and count<2:
                S+="a"
                A-=1
                count+=1
                print("S-{},A-{},count-{}".format(S,A,count))
            if A > B :
                flag = True
            else:
                flag = False
            print("S-{},A-{},count-{},flag-{}".format(S, A, count,flag))
        elif A > B and  flag and B>0:
            S+="b"
            B-=1
            flag = False
            print("S+=b",S)
        elif A<=B and not flag:
            while B>0 and count<2:
                S+="b"
                B-=1
                count+=1
            if A <=B :
                flag = True
            else:
                flag = False
            print("S-{},B-{},count-{},flag-{}".format(S, B, count,flag))
        elif A <= B and  flag and A>0:
            S+="a"
            A-= 1
            flag = False
        print("本次循环后的S-{},A-{},B-{},count-{},flag-{}".format(S,A,B,count,flag))
        if (not A and  not B):
            return S

# 本文件的文件名为 test_strWithout3a3b

import unittest
class teststrWithout3a3b(unittest.TestCase):
    def test_01(self):
        result = strWithout3a3b(0, 0)
        # 开始进行断言
        try:
            print("strWithout3a3b(0, 0)")
            self.assertEqual(result, "")
        except AssertionError as msg:
            print("AssertionError",msg)
        else:
            print("断言成功")


    def test_02(self):
        result = strWithout3a3b(100, 0)
    # 开始进行断言
        try:
            print("strWithout3a3b(100, 0)")
            self.assertEqual(result, "error")
        except AssertionError as msg:
            print(msg)
        else:
            print("断言成功")
    def test_03(self):
        result = strWithout3a3b(5, 5)
    # 开始进行断言
        try:
            print("strWithout3a3b(5,5)")
            self.assertEqual(result, "ababababab")
        except AssertionError as msg:
            print(msg)
        else:
            print("断言成功")

#  还有   A=3,B=1  --> abaa   A=5，B=5 --> ababababab 等其它组合

#
# # 本文件的文件名为 runtest
# import unittest
#
#
# def runtest():
#     suite = unittest.defaultTestLoader.discover(
#         start_dir="pythonTests",
#         pattern="test_*",
#         top_level_dir=None
#     )
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#

if __name__ == "__main__":
    # unittest.main()
    print(strWithout3a3b(12, 6))
    print(strWithout3a3b2(12, 6))