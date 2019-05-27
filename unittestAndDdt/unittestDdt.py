#coding:UTF-8
#__autor__='wyxces'

from ddt import ddt, data, unpack, file_data
import unittest

@ddt
class UnittestDdt(unittest.TestCase):
    @data(1)
    def test_normal(self, value):
        print('----test_normal----(value,1) ', (value,1))
        try:
            self.assertEqual(value,1)
            print(value,'= 1')
        except AssertionError as msg:
            print(msg)

    @data(2,3,4)
    def test_normals(self, value):
        print('----test_normals----(value,2)', (value,2))
        try:
            self.assertEqual(value,2)
            print(value, '= 2')
        except AssertionError as msg:
            print(msg)

    @data((1,2),(2,4))
    @unpack
    def test_tuple(self, value1, value2):
        print('----test_tuple----(value1+1, value2)',value1, '+1', value2)
        try:
            self.assertEqual(value1+1, value2)
            print(value1, '+1 = ', value2)
        except AssertionError as msg:
            print(msg)

    @data([1,2,3],[2,3,4])
    @unpack
    def test_list(self,value1, value2, value3):
        print('----test_list----(value1 + value2, value3)', value1, '+', value2, value3)
        try:
            self.assertEqual(value1 + value2, value3)
            print(value1, '+', value2 , ' = ', value3)
        except AssertionError as msg:
            print(msg)

    @data({'key1':1,'key2':2},{'key1':3,'key2':4})
    @unpack
    def test_dict(self, key1, key2):
        print('----test_tuple----(key1 * 2, key2)',key1, '* 2', key2)
        try:
            self.assertEqual(key1 * 2, key2)
            print(key1, '* 2 = ', key2)
        except AssertionError as msg:
            print(msg)

    @file_data(r'E:\learn\pythonCode\wyxces\files\ddtTest.json')
    def test_json(self,json_value):
        print('----test_json----(json_value)', (json_value))
        print(json_value)

if __name__ == '__main__':
    unittest.main()
