####### iros 본진 #######

from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.get(url)
parent = driver.current_window_handle

uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)
time.sleep(2)
id = driver.find_element(By.ID, 'id_user_id')
time.sleep(2)
id.send_keys('')
time.sleep(2)
for i in 'suhcrate':
    id.send_keys(i)

#suhcrate
#yonhap123!
pwd = driver.find_element(By.ID, 'password')
pwd.send_keys('')
time.sleep(2)
for i in 'yonhap123!':
    pwd.send_keys(i)

time.sleep(1)
pwd.send_keys('\n')
time.sleep(2)

parent = driver.current_window_handle
uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)
time.sleep(2)
## 열람하기 들어가기
driver.find_element(By.XPATH, '//a[@href="/iris/index.jsp?isu_view=view"]').click()

time.sleep(2)

parent = driver.current_window_handle
uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)
time.sleep(2)

driver.switch_to.frame('inputFrame') ## html 안에 여러가지 프레임이 있어.여기선 iframe.  프레임 설정을 해줘야됨.
addr = driver.find_element(By.XPATH, '//input[@id="txt_simple_address"]')
addr.send_keys('')
time.sleep(2)
for i in '경상남도 진주시 충무공동 234 혁신도시엘에이치아파트5단지 제501동 제8층 제802호':
    addr.send_keys(i)
addr.send_keys('\n')

time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('resultFrame')
driver.switch_to.frame('frmOuterModal')
driver.find_element(By.XPATH, '//button[@tabindex="2"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[@tabindex="2"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[contains(text(), "다음")]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//button[contains(text(), "다음")]').click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('resultFrame')
driver.find_element(By.XPATH, '//button[contains(text(), "결제")]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="inpMtdCls3"]').click()

time.sleep(3)
inp0 = driver.find_element(By.XPATH, '//input[@id="inpEMoneyNo1"]')
inp0.send_keys('')
time.sleep(2)
for i in 'C6643987':
    inp0.send_keys(i)

inp0 = driver.find_element(By.XPATH, '//input[@id="inpEMoneyNo2"]')
inp0.send_keys('')
time.sleep(2)
for i in '5475':
    inp0.send_keys(i)

inp0 = driver.find_element(By.XPATH, '//input[@id="inpEMoneyPswd"]')
inp0.send_keys('')
time.sleep(2)
for i in 'yon12':
    inp0.send_keys(i)

driver.find_element(By.XPATH, '//input[@id="chk_term_agree_all_emoney"]').click()

driver.find_element(By.XPATH, '//button[@name="inpComplete"]').click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

time.sleep(5)

parent = driver.current_window_handle
uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.find_element(By.XPATH, '//button[contains(text(), "확인")]').click()
driver.switch_to.window(parent)


