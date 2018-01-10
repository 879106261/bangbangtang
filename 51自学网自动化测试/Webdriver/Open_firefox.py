from selenium import webdriver
from time import sleep



#加载浏览器驱动
driver=webdriver.Firefox()

#打开网页
driver.get('http://jenkins.deppon.com/view/TPS/')
#窗口最大化
driver.maximize_window()
sleep(3)

driver.get('http://192.168.17.125/crm-web/login/index.action')
#调整窗口大小
driver.set_window_size(400,800)
#刷新页面
driver.refresh()
sleep(3)
#页面回退
driver.back()
sleep(3)
#页面前进
driver.forward()
sleep(3)

#关闭浏览器
driver.quit()