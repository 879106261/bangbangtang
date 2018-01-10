from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #as就是取个别名，该类是预期判断条件
from selenium.webdriver.common.by import By  #引入By类定位
from time import sleep

driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
sleep(2)
driver.find_element_by_css_selector('#kw').send_keys("selenium")
#每隔0.5s判断元素是否定位到，最长等待5s
#EC.presence_of_all_elements_located 检查一组是否在页面显示  EC.presence_of_element_located检查一个元素
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su12')))
element.click
sleep(3)
driver.quit()
