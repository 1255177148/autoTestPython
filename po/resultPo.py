from selenium.webdriver.common.by import By

elements = [
    {'name': 'result_list', 'desc': '搜索结果', 'by': (By.CLASS_NAME, 'gl-item'), 'ec': 'presence_of_element_located', 'action': None, 'needWait': 0, 'waitTime': '', 'js': None},
    {'name': 'price_list', 'desc': '价格列表', 'by': (By.XPATH, '//div[@class="p-price"]/strong/i'), 'ec': 'presence_of_element_located', 'action': None, 'needWait': 0, 'waitTime': '', 'js': None}
]