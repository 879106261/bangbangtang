'''from selenium import webdriver
from time import sleep
#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net')
#根据元素层级来定位
driver.find_elements_by_tag_name('option')[1].click()
sleep(3)
driver.find_element_by_css_selector('[value="3"]').click()
sleep(3)
driver.quit()
'''

#引入Select类
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
#加载浏览器驱动
driver=webdriver.Firefox()
#打开网页
driver.get('http://www.51zxw.net')
#定义一个变量保存Select
select=Select(driver.find_element_by_css_selector('[name="CookieDate"]'))
#通过索引定位
select.select_by_index(1)
#通过文字定位
select.select_by_visible_text('留一年')
#通过value值
select.select_by_value("2")  #注意deselect_by_value意思是不选择
sleep(3)
driver.quit()

