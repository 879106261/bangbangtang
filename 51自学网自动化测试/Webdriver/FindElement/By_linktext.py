from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net/')
#通过linktext对应超链接文字全名
driver.find_element_by_link_text('程序开发').click()
#通过linktext对应超链接文字部分名
driver.find_element_by_partial_link_text('神秘面纱').click()
sleep(3)
driver.quit()