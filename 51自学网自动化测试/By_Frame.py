from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
#设置网页文件路径，r代表转义
file_path=r'E:\python练习\Frame.html'
#转义路径另一种写法
#file_path='E:\\python练习\\Frame.html'
#打开网页
driver.get(file_path)
#切换到frame页面
driver.switch_to.frame("search")
#定位到页面元素
driver.find_element_by_css_selector('#kw').send_keys("selenium")
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()