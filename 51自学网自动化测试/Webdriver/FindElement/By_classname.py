from selenium import webdriver
from time import sleep
#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.baidu.com/')
#通过class定位
driver.find_element_by_class_name('s_ipt').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()


