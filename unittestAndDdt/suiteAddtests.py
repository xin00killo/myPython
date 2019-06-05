#coding:UTF-8
#__autor__='wyxces'

import unittest

class MyTest1(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')
    def tearDown(self) -> None:
        print('tearDown')
    def test1_1(self):
        print('MyTest1.test1_1')
    def test1_2(self):
        print('MyTest1.test1_2')
    def test1_3(self):
        print('MyTest1.test1_3')

class MyTest2(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')
    def tearDown(self) -> None:
        print('tearDown')
    def test2_1(self):
        print('MyTest2.test2_1')
    def test2_2(self):
        print('MyTest2.test2_2')
    def test2_3(self):
        print('MyTest2.test2_3')

if __name__ == '__main__':
    # 创建第一组测试套件  添加用例的方式 suite.addTest（类名（'方法名'））
    suite1 = unittest.TestSuite()
    suite1.addTest(MyTest1('test1_1'))
    suite1.addTest(MyTest1('test1_2'))
    print('''suite1.addTest(MyTest1('test1_1')),addTest(MyTest1('test1_2'))\n\t''', suite1)
    # print(suite1[1])
    # 创建第二组测试套件  添加用例的方式 suite.addTest（类名（'方法名'））
    suite2 = unittest.TestSuite()
    suite2.addTest(MyTest2('test2_2'))
    suite2.addTest(MyTest2('test2_3'))
    print('''suite2.addTest(MyTest2('test2_2')),addTest(MyTest2('test2_3')))\n\t''', suite2)

    # 创建第三组测试套件  添加用例的方式 suite.addTest（类名（'方法名'））
    suite3 = unittest.TestSuite()
    suite3.addTest(MyTest1('test1_3'))
    suite3.addTest(MyTest2('test2_1'))
    print('''suite3.addTest(MyTest1('test1_3')),addTest(MyTest2('test2_1')))\n\t''', suite3)
    print('suite3.countTestCases()', suite3.countTestCases())

    # 创建一个综合套件，添加用例的方法 suite.addTests(测试套件名)
    suite = unittest.TestSuite()
    suite.addTests(suite1)
    suite.addTests(suite2)
    suite.addTests(suite3)
    print('''suite.addTests(suite1)，suite.addTests(suite2)，suite.addTests(suite3)\n\t''', suite)
    print('suite.countTestCases()', suite.countTestCases())

    runner = unittest.TextTestRunner()
    print('----------runner.run(suite1)-------')
    runner.run(suite1)
    print('----------runner.run(suite)-------')
    runner.run(suite)


