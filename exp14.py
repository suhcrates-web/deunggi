
######  수집하는 부분 ########

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import binascii, codecs
import mysql.connector
from datetime import date, datetime
from database import cursor, db

xcode ='24'
xcgcd= 'DCM000024214000301'
open0 = False
options = webdriver.ChromeOptions()
# options.binary_location = 'C:/Users/yb/Downloads/GoogleChromePortable64/App/Chrome-bin/chrome.exe'
driver = webdriver.Chrome('C:/stamp/chromedriver', options=options)
url= 'http://testbot.ddns.net:5236/donga/gookhwe/'
driver.get(url)