from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait # 显式等待用
from selenium.webdriver.support import expected_conditions as EC # 显式等待用
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import importlib
import logging

logger = logging.getLogger('main.page')

class Page:
    def __init__(self, driver, page) -> None:
        self.driver = driver
        self.page = page
        self.by = ()
        self.action = None
        self.needWait = None
        self.ec = None
        self.waitTime = None
        self.js = None
        self.elements = get_page_elements(page)
    
    def get_page_elements(self, element):
        """获取指定元素数据

        Args:
            element (_type_): _指定的元素名称_
        """
        for each in self.elements:
            if each['name'] == element:
                self.by = each['by']
                self.needWait = each['needWait']
                self.ec = each['ec']
                if each['waitTime'] is not None:
                    self.waitTime = each['waitTime']
                if each['action'] is not None:
                    self.action = each['action']
                if each['js'] is not None:
                    self.js = each['jc']
    
    def selenium_cmd(self, find_type='find_element', args=None):
        """拼装selenium命令

        Args:
            find_type (str, optional): _description_. Defaults to 'find_element'.
            args (_type_, optional): _description_. Defaults to None.
        """
        if

def get_page_elements(page):
    """动态加载指定页面文件，获取文件中定义的所有元素

    Args:
        page (_type_): _指定页面_
    """
    elements = None
    if page:
        try:
            module = importlib.import_module(page)
            elements = module.elements
        except Exception as e:
            logger.error('加载页面,获取定义的页面元素报错--->', exc_info=e)
    return elements