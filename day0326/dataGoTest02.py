from urllib.parse import quote
import requests
import bs4

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'B78CbLfOD6924JbTWwuUqjtPrOE%2F8gN00tgnG17lUMgvQUx%2BqqdulYUiCVflKIexihA7Q22UlwVwHmPLVAGt5g%3D%3D'

Q0 = quote('서울특별시')
Q1 = quote('강남구')
QT = '1'
QN = quote('삼성약국')
QRD = 'NAME'
pageNo = '1'
startPage = '1'
numOfRows = '10'
pageSize = '10'

paramset = "serviceKey="+serviceKey+"&Q0="+Q0+"&Q1="+Q1+"&QT="+QT+"&QN="+QN+"&QRD="+QRD+"&pageNo="+pageNo+"&startPage="+startPage+"&numOfRows="+numOfRows+"&pageSize="+pageSize

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content,'html.parser')
print(bs_obj)
title_list = bs_obj.findAll('dutymapimg')
print(title_list)
# print(bs_obj.findAll('dutyname'))