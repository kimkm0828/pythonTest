from urllib.parse import quote
import requests
import bs4

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'B78CbLfOD6924JbTWwuUqjtPrOE%2F8gN00tgnG17lUMgvQUx%2BqqdulYUiCVflKIexihA7Q22UlwVwHmPLVAGt5g%3D%3D'

Q0 = quote('서울특별시')
# Q1 = quote('강남구')
# QT = '1'
# QN = quote('삼성약국')
QRD = 'NAME'
pageNo = '1'
startPage = '1'
numOfRows = '5000'
# pageSize = '10'

paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&QRD="+QRD+"&pageNo="+pageNo+"&startPage="+startPage+"&numOfRows="+numOfRows

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content,'html.parser')
items = bs_obj.findAll('item')

count = 0
for item in items:
    tagged_item = item.find("dutytime1c")
    if (tagged_item != None):
        close_time = int(tagged_item.text)
        if(close_time > 2100):
            count += 1
print("월요일 9시 이후까지 하는 약국의 수 : ",count)