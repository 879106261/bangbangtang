#引入Keys类
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
driver.find_element_by_css_selector('#kw').send_keys('python')
#ctrl+a 全选
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'a')
sleep(2)
#ctrl+c  ctrl+x
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'c')
sleep(2)
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL,'x')
sleep(2)
#打开新界面
driver.get('https://www.sogou.com/')
#ctrl+v
driver.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL,'v')
sleep(3)
driver.quit()


