
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from ToolBox_selenium import send_key_really
import time
import re
from bs4 import BeautifulSoup

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

### ID 입력
send_key_really(driver, 'id_user_id','suhcrate')

### 비번 입력
send_key_really(driver, 'password', 'yonhap123!','go')

suc0 = False
while suc0 == False:
    try:
        driver.find_element(By.ID, 'leftS').find_element(By.XPATH, '//img[@alt="로그아웃"]')
        suc0 = True
    except:
        print('로그인안됨')
        pass
##########

parent = driver.current_window_handle
uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)


##

driver.get('http://www.iros.go.kr/frontservlet?cmd=RISURetrieveUnissuedListC')

wait.until(EC.element_to_be_clickable((By.ID, 'selectBox')))
element = driver.find_element(By.ID, 'selectBox')
driver.execute_script("arguments[0].click();", element)
element =  driver.find_element(By.ID, 'print_bottom')
driver.execute_script("arguments[0].click();", element)
time.sleep(3)
# Alert(driver).accept()
# print(Alert(driver).text)
driver.switch_to.alert
print(driver.page_source)


# uselessWindows = driver.window_handles
# print(uselessWindows)