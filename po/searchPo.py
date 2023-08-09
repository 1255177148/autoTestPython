from selenium.webdriver.common.by import By

pageUrl = 'https://www.jd.com/'

elements = [
    #  #J_searchbg+input 是css标签选择器，指id为J_searchbg后的第一个input兄弟节点
    {'name': 'search_input', 'desc': '搜索框点击', 'by': (By.CSS_SELECTOR, '#J_searchbg+input'), 'ec': 'presence_of_element_located', 'action': 'send_keys()', 'needWait': 2, 'waitTime': '2', 'js': ''},
    {'name': 'search_button', 'desc': '搜索按钮点击', 'by': (By.XPATH, '//div[@id="J_searchbg"]/following-sibling::button[1]'), 'ec': 'presence_of_element_located', 'action': 'click()', 'needWait': 0, 'js': 'document.getElementById("J_searchbg").parentNode.children[4].click()'}
]