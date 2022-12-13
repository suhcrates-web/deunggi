
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

## 열람하기 들어가기
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/iris/index.jsp?isu_view=view"]')))
driver.find_element(By.XPATH, '//a[@href="/iris/index.jsp?isu_view=view"]').click()

parent = driver.current_window_handle
uselessWindows = driver.window_handles
for winId in uselessWindows:
    if winId != parent:
        driver.switch_to.window(winId)
        driver.close()
driver.switch_to.window(parent)

wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[@id="inputFrame"]')))

driver.switch_to.frame('inputFrame') ## html 안에 여러가지 프레임이 있어.여기선 iframe.  프레임 설정을 해줘야됨.


### 주소 넣기

send_key_really(driver, 'txt_simple_address', '경상남도 진주시 충무공동 234 혁신도시엘에이치아파트5단지 제501동 제12층 제1201호', 'go')

driver.switch_to.default_content()
driver.switch_to.frame('resultFrame')
driver.switch_to.frame('frmOuterModal')
driver.find_element(By.XPATH, '//button[@tabindex="2"]').click()
driver.find_element(By.XPATH, '//button[@tabindex="2"]').click()
driver.find_element(By.XPATH, '//button[contains(text(), "다음")]').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "다음")]')))
# element = driver.find_element(By.XPATH, '//button[contains(text(), "다음")]').click()
element = driver.find_element(By.XPATH, '//button[contains(text(), "다음")]')
driver.execute_script("arguments[0].click();", element)

driver.switch_to.default_content()
driver.switch_to.frame('resultFrame')

time.sleep(2)
current_url = driver.current_url

driver.find_element(By.XPATH, '//button[contains(text(), "결제")]').click()

wait.until(EC.url_changes(current_url))

wait.until(EC.visibility_of_element_located((By.ID, 'inpMtdCls3')))
element = driver.find_element(By.ID, 'inpMtdCls3')
driver.execute_script("arguments[0].click();",
 element)  # not clickable at point  의 대처법


wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="inpEMoneyNo1"]')))

send_key_really(driver, 'inpEMoneyNo1', 'C6643987')
send_key_really(driver, 'inpEMoneyNo2', '5475')
send_key_really(driver, 'inpEMoneyPswd', 'yon12')
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
