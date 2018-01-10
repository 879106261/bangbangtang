from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net/')
#通过tagname，默认定位第一个
driver.find_element_by_tag_name('input').send_keys('selenium')
#通过tagnames，找出所有的，使用列表下标的方式，定位第一个
driver.find_elements_by_tag_name('input')[0].send_keys('selenium')
sleep(3)
#driver.quit()