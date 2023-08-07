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