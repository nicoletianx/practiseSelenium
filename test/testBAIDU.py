# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH

#URL = "http://www.baidu.com"
URL = Config().get('URL')
#获取当前路径&返回脚本路径
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
#locator_result = (By.XPATH, '//div[div/h3/a]')

#driver = webdriver.Chrome(executable_path=driver_path)
driver = webdriver.Chrome()
driver.get(URL)
driver.find_element(*locator_kw).send_keys('selenium 灰蓝')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
print (links)
for link in links:
    print(link.text)
driver.quit()
