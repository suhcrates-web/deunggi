import requests
import json

url = 'http://finpl.kr/issnma/applyISSNMA2000'
header = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6', 'Connection': 'keep-alive', 'Content-Length': '736', 'Content-Type': 'application/json;charset=UTF-8', 'Cookie': '_ga=GA1.1.1780065231.1661821972; ch-veil-id=e2f4ebb7-1093-4fb1-9827-e3494d34f08c; connect.sid=s%3A-8mvQ5Hy6W6Qv4_3uxYiIXsqOzKSx7dq.c8S44rMUHhYlciocAjpCXZ4FmC2j2NAigrkbQoAw7aw; ch-session-84688=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI4NDY4OC02MzBkNjQxNDJhMGVlZTgwYzQyNCIsImlhdCI6MTY2MTgzMjYyNSwiZXhwIjoxNjY0NDI0NjI1fQ.BKCj_0N_wkTzsa2Ss9naFWqr1aTY6KN_6AA9WkvnBfY; _ga_H9S4PCB1NJ=GS1.1.1661832253.3.1.1661832652.0.0.0', 'Host': 'finpl.kr', 'Origin': 'http://finpl.kr', 'Referer': 'http://finpl.kr/issnma/selectISSNMA1000View', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}
header={'Host': 'finpl.kr', 'Connection': 'keep-alive', 'Content-Length': '736', 'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://finpl.kr', 'Referer': 'http://finpl.kr/issnma/selectISSNMA1000View', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7,ru;q=0.6', 'Cookie': '_ga=GA1.1.1780065231.1661821972; ch-veil-id=e2f4ebb7-1093-4fb1-9827-e3494d34f08c; connect.sid=s%3A-8mvQ5Hy6W6Qv4_3uxYiIXsqOzKSx7dq.c8S44rMUHhYlciocAjpCXZ4FmC2j2NAigrkbQoAw7aw; ch-session-84688=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI4NDY4OC02MzBkNjQxNDJhMGVlZTgwYzQyNCIsImlhdCI6MTY2MTgzNTAzNiwiZXhwIjoxNjY0NDI3MDM2fQ.fhv7If6hSv3cYIgGjwji_vBlyxuCKZ5zjEZO5B5Q_js; _ga_H9S4PCB1NJ=GS1.1.1661832253.3.1.1661835112.0.0.0'}

# data = [
#     {
#         "sStatus": "A",
#         "unqNo": "1911-2013-004976",
#         "esttCls": "집합건물",
#         "esttAddr": "경상남도 진주시 사들로 157 진주혁신도시 센텀리버파크 제107동 제18층 제1804호 [충무공동 191]",
#         "owner": "최**외 1명",
#         "upr": 770,
#         "rgstnRecSts": "현행",
#         "flag1": 1,
#         "flag2": 0,
#         "flag3": None,
#         "flag4": None,
#         "flag5": None,
#         "flag6": None,
#         "flag7": None,
#         "no": 41202,
#         "map": "경상남도 진주시 사들로 157",
#         "dungbonCls": "12",
#         "y202tradeSeqFlag": "Y",
#         "y202cmortFlag": "Y",
#         "sinchung": "Y",
#         "summary": "Y",
#         "rowKey": 0,
#         "sortKey": 0,
#         "uniqueKey": "@dataKey1661832626034-0",
#         "_attributes": {
#             "rowNum": 1,
#             "checked": True,
#             "disabled": False,
#             "checkDisabled": False,
#             "className": {
#                 "row": [],
#                 "column": {}
#             }
#         },
#         "_disabledPriority": {},
#         "rowSpanMap": {},
#         "_relationListItemMap": {}
#     }]

data ="""
[{"sStatus":"A","unqNo":"1911-2013-005019","esttCls":"집합건물","esttAddr":"경상남도 진주시 사들로 157 진주혁신도시 센텀리버파크 제108동 제9층 제902호 [충무공동 191]","owner":"조**","upr":770,"rgstnRecSts":"현행","flag1":1,"flag2":0,"flag3":null,"flag4":null,"flag5":null,"flag6":null,"flag7":null,"no":41249,"map":"경상남도 진주시 사들로 157","dungbonCls":"12","y202tradeSeqFlag":"Y","y202cmortFlag":"Y","sinchung":"Y","summary":"Y","rowKey":1,"sortKey":1,"uniqueKey":"@dataKey1661834271691-1","_attributes":{"rowNum":2,"checked":true,"disabled":false,"checkDisabled":false,"className":{"row":[],"column":{}}},"_disabledPriority":{},"rowSpanMap":{},"_relationListItemMap":{}}]
"""

data="""
[
    {
        "sStatus": "A",
        "unqNo": "1911-2014-002443",
        "esttCls": "집합건물",
        "esttAddr": "경상남도 진주시 사들로 126 진주혁신코오롱하늘채 제411동 제18층 제1803호 [충무공동 230]",
        "owner": "최**",
        "upr": 0,
        "rgstnRecSts": "현행",
        "flag1": 1,
        "flag2": 0,
        "flag3": null,
        "flag4": null,
        "flag5": null,
        "flag6": null,
        "flag7": null,
        "no": 41386,
        "map": "경상남도 진주시 사들로 126",
        "dungbonCls": "12",
        "y202tradeSeqFlag": "Y",
        "y202cmortFlag": "Y",
        "sinchung": "Y",
        "summary": "Y",
        "rowKey": 2,
        "sortKey": 2,
        "uniqueKey": "@dataKey1661837390750-2",
        "_attributes": {
            "rowNum": 3,
            "checked": true,
            "disabled": false,
            "checkDisabled": false,
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
"""
# print(json.loads(data))
temp = requests.post(url, headers=header, json=json.loads(data))
print(temp.json())