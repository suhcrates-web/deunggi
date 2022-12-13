import requests
from bs4 import BeautifulSoup
from finpl_gimme_code import finpl_gimme_code


# addr = '진주혁신 센텀리버파크 101동 403호'

#### 장바구니 입력
def finpl_into_bag(addr):
    num0, address0, map0 = finpl_gimme_code(addr)
    print(num0)
    print(address0)
    print(map0)
    print("====================")

    url = 'http://finpl.kr/issnma/insertISSNMA0000'

    header = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '514',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': '_ga=GA1.1.1780065231.1661821972; ch-veil-id=e2f4ebb7-1093-4fb1-9827-e3494d34f08c; connect.sid=s%3A-8mvQ5Hy6W6Qv4_3uxYiIXsqOzKSx7dq.c8S44rMUHhYlciocAjpCXZ4FmC2j2NAigrkbQoAw7aw; ch-session-84688=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI4NDY4OC02MzBkNjQxNDJhMGVlZTgwYzQyNCIsImlhdCI6MTY2MTgyMjY0MywiZXhwIjoxNjY0NDE0NjQzfQ.gkIMQ6OKARTtJ1ufKL-jMaCDbCaSTSz0aqFdjT3Uj9k; _ga_H9S4PCB1NJ=GS1.1.1661821972.1.1.1661822653.0.0.0',
        'Host': 'finpl.kr',
        'Origin': 'http://finpl.kr',
        'Referer': 'http://finpl.kr/issnma/selectISSNMA0000View',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    data = [
        {
            "sStatus": "A",
            "unqNo": num0,
            "esttCls": "집합건물",
            "esttAddr": address0,
            "map": map0,
            "rgstnRecSts": "현행",
            "rowKey": 0,
            "sortKey": 0,
            "uniqueKey": "@dataKey1661822646394-0",
            "_attributes": {
                "rowNum": 1,
                "checked": 'true',
                "disabled": 'false',
                "checkDisabled": 'false',
                "className": {
                    "row": [],
                    "column": {}
                }
            },
            "_disabledPriority": {},
            "rowSpanMap": {},
            "_relationListItemMap": {}
        }
    ]
    print(f"{address0} //장바구니 입력")
    requests.post(url, headers=header, json=data)
