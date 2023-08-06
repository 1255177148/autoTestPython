import unittest
import os
import logging
import time
from common.emailUtil import Email
from common.log import log_init
from BeautifulReport import BeautifulReport

projectHome = os.path.dirname(os.path.abspath(__file__)) #项目根路径
testCasePath = os.path.join(projectHome, 'testCase')
reportPath = os.path.join(projectHome, 'report')

log_init()#初始化日志
logger = logging.getLogger('main')

def summary_format(result):
    """对测试结果关键信息进行汇总，做为邮件正文

    Args:
        result (_dict_): _测试结果字典数据_

    Returns:
        _str_: _测试结果关键信息_
    """
    summary = "\n" + u"<p>          测试结果汇总信息                </p>" + "\n" + \
                 u"<p> 开始时间: " + result['beginTime'] + u" </p>" + "\n" + \
                 u"<p> 运行时间: " + result['totalTime'] + u" </p>" + "\n" + \
                 u"<p> 执行用例数: " + str(result['testAll']) + u" </p>" + "\n" + \
                 u"<p> 通过用例数: " + str(result['testPass']) + u" </p>" + "\n" + \
                 u"<p> 失败用例数: " + str(result['testFail']) + u" </p>" + "\n" + \
                 u"<p> 忽略用例数: " + str(result['testSkip']) + u" </p>" + "\n"
    return summary

def send_email(context, file):
    """发送测试结果邮件

    Args:
        context (_str_): _邮件正文_
        file (_type_): _附件_
    """
    title = time.strftime('%Y-%m-%d', time.localtime()) + "自动化测试结果"
    email = Email(title, context, file)
    sendResult = email.sendEmail()
    if sendResult:
        logger.info("测试报告邮件发送成功")
    else:
        logger.error("测试报告邮件发送失败")


def load_suite(casePath=testCasePath, rule = '*Case.py'):
    """加载测试用例

    Args:
        casePath (_str_, optional): _测试用例地址_. Defaults to testCasePath.
        rule (str, optional): _测试用例文件加载规则_. Defaults to '*Case.py'.
    """
    suite = unittest.defaultTestLoader.discover(testCasePath, rule) # 获取测试用例的套件对象
    return suite


def run_suite(suite):
    """执行所有加载的测试用例,并返回结果

    Args:
        suite (_type_): _测试用例套件对象_

    Returns:
        _type_: _返回测试报告文件路径和结果摘要,分别作为邮件的附件和正文_
    """
    now = time.strftime('%Y-%m-%d', time.localtime())
    fileName = now + '_report.html'
    run_result = BeautifulReport(suite)
    run_result.report(description='测试报告描述',filename=fileName,report_dir=reportPath)
    report_summary = summary_format(run_result.fields)
    return os.path.join(reportPath, fileName), report_summary


if __name__ == '__main__':
    suite = load_suite()
    report_file, report_summary = run_suite(suite)
    logger.info("测试用例摘要------>" + report_summary)
    send_email(report_summary, report_file)