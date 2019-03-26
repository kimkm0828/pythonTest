from urllib.parse import quote
import requests
import bs4

endpoint = 'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
serviceKey = 'B78CbLfOD6924JbTWwuUqjtPrOE%2F8gN00tgnG17lUMgvQUx%2BqqdulYUiCVflKIexihA7Q22UlwVwHmPLVAGt5g%3D%3D'

# 일요일에 문여는 약국의 이름과 주소

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
listN = []
listA = []
for item in items:
    tagged_item = item.find("dutytime6s")
    tagged_item2 = item.find("dutytime7s")
    tagged_item3 = item.find("dutytime8s")
    if (tagged_item != None and tagged_item2 != None and tagged_item3 != None):
        # listN = {'name': n, 'addr': addr}
        n = item.find("dutyname").text
        addr = item.find("dutyaddr").text
        listN.append({'name': n, 'addr': addr})
        listA.append(addr)
        # print("약국의 이름 : ",n,"//주소 : ",addr)
        count += 1
print("약국이름 : ",listN)
# print("약국주소 : ",listA)
# print('쉬는날에 문여는 약국수 : ',count)

# count = 0
# for item in items:
#     tagged_item = item.find("dutytime6s")
#     tagged_item2 = item.find("dutytime7s")
#     tagged_item3 = item.find("dutytime8s")
#     if (tagged_item == None):
#         n = item.find("dutyname").text
#         addr = item.find("dutyaddr").text
#
#         print("약국의 이름 : ",n,"//주소 : ",addr)
#         count += 1
#
# print('쉬는날에 문여는 약국수 : ',count)