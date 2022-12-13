import requests
import json
from bs4 import BeautifulSoup


def finpl_gimme_code(addr):
    url = 'http://finpl.kr/issnma/selectAddress'

    header = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6', 'Connection': 'keep-alive',
              'Content-Length': '97', 'Content-Type': 'application/json;charset=UTF-8',
              'Cookie': '_ga=GA1.1.1780065231.1661821972; ch-veil-id=e2f4ebb7-1093-4fb1-9827-e3494d34f08c; connect.sid=s%3A-8mvQ5Hy6W6Qv4_3uxYiIXsqOzKSx7dq.c8S44rMUHhYlciocAjpCXZ4FmC2j2NAigrkbQoAw7aw; ch-session-84688=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI4NDY4OC02MzBkNjQxNDJhMGVlZTgwYzQyNCIsImlhdCI6MTY2MTgyMzA1NCwiZXhwIjoxNjY0NDE1MDU0fQ.2yFMNf7QjozjuYbVsJkk08T8qazoEGvcWNberGufupw; _ga_H9S4PCB1NJ=GS1.1.1661821972.1.1.1661823096.0.0.0',
              'Host': 'finpl.kr', 'Origin': 'http://finpl.kr', 'Referer': 'http://finpl.kr/issnma/selectISSNMA0000View',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'X-Requested-With': 'XMLHttpRequest'}

    data = {
        # "txtSimpleAddress": "진주혁신 센텀리버파크 101동 403호",
        "txtSimpleAddress": addr,
        "currPage": "1",
        "esttCls": "0"
    }
    temp = requests.post(url, headers=header, json=data)
    temp = temp.json()
    # print(temp)
    num0 = temp['rows']['list'][0]['고유번호']
    address0 = temp['rows']['list'][0]['주소']
    map0 = temp['rows']['list'][0]['map']

    return num0, address0, map0

