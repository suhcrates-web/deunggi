from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import re

url = 'http://www.iros.go.kr/PMainJ.jsp'
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome('./chromedriver', options=options)
driver = webdriver.Chrome('C:/stamp/chromedriver', options=options)
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

driver.get(url)

parent = driver.current_window_handle

uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)
time.sleep(2)
id = driver.find_element(By.XPATH, '//*[@id="id_user_id"]')
id.send_keys('value','suhcrate')
# id.send_keys("suhcrate")
time.sleep(3)
id = driver.find_element(By.ID, 'password')
# id.click()
id.send_keys("12345")
time.sleep(3)
id = driver.find_element(By.XPATH, '//*[@id="leftS"]/div[2]/form/div[1]/ul/li[4]/a')
id.click()
ans = input(":::")
html0 = driver.page_source
html0 = BeautifulSoup(html0, 'html.parser')