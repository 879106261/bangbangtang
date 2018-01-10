from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('https://www.baidu.com/')
#通过id，定位到搜索框，传入搜索值
#driver.find_element_by_id('kw').send_keys('季羡林')
#通过那么
driver.find_element_by_name('wd').send_keys('朱自清')
sleep(3)
#定位搜索按钮,并点击
driver.find_element_by_id('su').click()
sleep(3)

driver.quit()

