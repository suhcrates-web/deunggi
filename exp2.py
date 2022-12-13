from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
from ToolBox_selenium import send_key_really

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://www.iros.go.kr/PMainJ.jsp'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/stamp/chromedriver', options=options)
#options.add_argument("--disable-notifications")

driver.implicitly_wait(10) ## 10초까지 기다리기

wait = WebDriverWait(driver, 10)

driver.get(url)
parent = driver.current_window_handle

uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)


send_key_really(driver, 'id_user_id', 'suhcrate' )
#
# suc0 = False
# while suc0 == False:
#     try:
#         id = driver.find_element(By.ID, 'id_user_id')
#         id.send_keys('')
#
#         suc0 = True
#     except:
#         pass

#
# suc0 = False
# while suc0 == False:
#     id.send_keys('a')
#     len0 = len(driver.find_element(By.ID, 'id_user_id').get_attribute('value'))
#     if len0 >0 :
#         suc0 = True
#
#     for _ in range(len0):
#         id.send_keys(Keys.BACKSPACE)
#
#
# for i in 'suhcrate':
#     id.send_keys(i)
