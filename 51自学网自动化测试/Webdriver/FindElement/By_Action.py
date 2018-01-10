#引入ActionChains类
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#加载浏览器驱动
from time import sleep
driver=webdriver.Firefox()
#打开网页
driver.get('https://www.baidu.com/')
#c窗口最大化
driver.maximize_window()
driver.find_element_by_css_selector('#kw').send_keys('python')
#获取搜索框元素对象
element=driver.find_element_by_css_selector('#kw')
#双击操作
ActionChains(driver).double_click(element).perform() #perform()就是执行
sleep(3)
#右击操作
ActionChains(driver).context_click(element).perform()
sleep(3)
#获取元素对象
above=driver.find_element_by_css_selector('.pf')
#悬停操作
ActionChains(driver).move_to_element(above).perform()
sleep(3)
driver.quit()

