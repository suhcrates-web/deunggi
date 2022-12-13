import csv
from finpl_into_bag import finpl_into_bag
from finpl_balgup import finpl_balgup


### 핀플 다운로더
#주택목록을 가져와서 핀플에서 검색, 장바구니에 담아 결제

temp = open('data/LH주택목록.csv')
temp = csv.reader(temp)
# print(temp)
n =0

### 장바구니 담기
a = 199
for line in temp:
    if n >a and n <=a+11:
        addr = line[0] +" " +line[1]
        print(addr)
        finpl_into_bag(addr)
    n+=1


### 결제하기
num0 =41430 - 179 + a
for pl0 in range(50):
    finpl_balgup(num0 + pl0)
    print(num0+pl0)