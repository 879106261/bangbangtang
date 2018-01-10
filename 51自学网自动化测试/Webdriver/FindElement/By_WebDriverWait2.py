from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException
from time import ctime
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
sleep(2)
#隐式等待
driver.implicitly_wait(5)
#检测元素是否存在
try:
    print(ctime())
    driver.find_element_by_css_selector('#kw').send_keys("selenium")
    driver.find_element_by_css_selector('#su1').click()
except NoSuchElementException as msg:
    print(msg)
finally:
    print(ctime())

sleep(3)
driver.quit()
