from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net/')
#层级组合定位
#driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys('selenium')
#driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys('selenium')
#逻辑运算组合定位
driver.find_element_by_xpath('//input[@class="loinp" and @name="username"]').send_keys('selenium')
sleep(3)
driver.quit()


