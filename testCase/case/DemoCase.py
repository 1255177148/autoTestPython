from unittest import TestCase
import unittest
import os
from BeautifulReport import BeautifulReport


class TestDemo(TestCase):
    def test_demo1(self):
        """测试用例demo,函数名必须以test_开头
        """
        raise ValueError("不合法的邮件标题")
        # print("通过用例")
    
    def test_demo2(self):
        print("通过用例2")

        

if __name__ == '__main__':
    # suite = unittest.TestSuite() # 用来组装,打包,管理多个TestCase（测试用例）文件的
    # suite.addTest(unittest.makeSuite(TestDemo))# 套件对象.addTest(unittest.makeSuite(测试类名))
    
    '''
    相对路径写法，
    ../  表示当前文件所在目录的上一级目录
    ./   表示当前文件所在的目录
    /    表示磁盘目录,比如在linux里就表示根目录
    '''
    suite = unittest.defaultTestLoader.discover("./", '*Case.py') # 获取套件对象，并加载指定目录下，指定的以Case结尾的py文件内的test开头的函数
    
    # 实例化运行对象
    runner = unittest.TextTestRunner()
    # 执行测试套件
    runner.run(suite)
    