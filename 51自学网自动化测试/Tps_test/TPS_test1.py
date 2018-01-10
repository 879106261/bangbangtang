#引入webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

#打开浏览器和tps
driver=webdriver.Firefox()
driver.get('http://192.168.68.89:8180/itf/login/index.action')
driver.maximize_window()
sleep(2)
#定位登录页面元素
driver.find_element_by_css_selector('#username').send_keys('085692')
driver.find_element_by_name('password').send_keys('aaaaaa1!')
sleep(2)
#点击登录
driver.find_element_by_css_selector('button[class="login-button btn-primary"]').click()
sleep(8)
#driver.find_element_by_css_selector('button[class="x-btn-center"]').click()
driver.find_element_by_css_selector('img[class="x-tool-close"]').click()
#driver.find_element_by_xpath('//div[contains(text(),"订单管理")]').click()
#js=driver.find_element_by_xpath('//div[contains(.,"订单管理")]').click()
#driver.execute_script(js)
driver.find_element_by_link_text('订单管理').click()

