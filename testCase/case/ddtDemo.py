import ddt
import unittest
from unittest import TestCase

case_data1 = [
    {'name': '测试1', 'age': 5},
    {'name': '测试2', 'age': 6}
]

case_data2 = [1, 2, 3]

case_data3 = ([1, 2, 3], [4, 5, 6])

@ddt.ddt
class DemoTest(TestCase):
    
    @ddt.data(*case_data1)
    def test_1(self, caseData):
        print(f'test_1--->{caseData}')
    
    @ddt.data(case_data2)
    def test_2(self, caseData):
        print(f'test_2--->{caseData}')
    
    
    @ddt.data(*case_data2)
    def test_3(self, caseData):
        print(f'test_3--->{caseData}')
    
    @ddt.data(case_data3)
    def test_4(self, caseData):
        print(f'test_4--->{caseData}')
    
    @ddt.data(*case_data3)
    def test_5(self, caseData):
        print(f'test_5--->{caseData}')
    
    @ddt.data(*case_data3)
    @ddt.unpack
    def test_6(self, a, b, c):
        print(f'test_6--->{a},{b},{c}')

if __name__ == '__main__':
    unittest.main()