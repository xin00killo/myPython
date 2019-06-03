#coding:UTF-8
#__autor__='wyxces'

import unittest

class UnittestTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')
    def test_001(self):
        print('1111111111111111111')
    def test_002(self):
        print('2222222222222222222')
    def test_003(self):
        print('3333333333333333333')
    def tearDown(self) -> None:
        print('tearDown')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(UnittestTest())
    runner = unittest.TextTestRunner()
    runner.run(suite)