from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net')
#根据id属性来定位元素
#driver.find_element_by_css_selector('#kw').send_keys('selenium')
#根据class属性来定位元素
#driver.find_element_by_css_selector('.s_ipt').send_keys('selenium')
#根据属性来定位元素
#driver.find_element_by_css_selector('[autocomplete="off"]').send_keys('selenium')
#根据元素层级来定位
driver.find_element_by_css_selector('form#loginForm>ul>input[type="password"]').send_keys('selenium')
sleep(3)
driver.quit()
