from unittest import TestCase
import unittest
from BeautifulReport import BeautifulReport
import os
import time

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 项目根路径

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d', time.localtime())
    report_path = os.path.join(base_path, 'report')
    fileName = now + '_report.html'
    suite = unittest.defaultTestLoader.discover("./", '*Case.py') # 获取套件对象，并加载指定目录下，指定的以Case结尾的py文件内的test开头的函数
    run_result = BeautifulReport(suite)
    run_result.report(description='测试报告描述',filename=fileName,report_dir=report_path)