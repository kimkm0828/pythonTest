import requests
import bs4

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?'
serviceKey = 'B78CbLfOD6924JbTWwuUqjtPrOE%2F8gN00tgnG17lUMgvQUx%2BqqdulYUiCVflKIexihA7Q22UlwVwHmPLVAGt5g%3D%3D'
numOfRows='10'
pageSize='1'
pageNo = '1'
MobileOS='ETC'
MobileApp = 'AppTest'
arrange = 'A'
contentTypeId = '15'
areaCode = '1'
sigunguCode='4'
listYN = 'Y'

paramset = "serviceKey="+serviceKey+"&numOfRows="+numOfRows+"&pageSize="+pageSize+"&pageNo="+pageNo+"&MobileOS="+MobileOS+"&MobileApp="+MobileApp+"&arrange="+arrange+"&contentTypeId="+contentTypeId+"&areaCode="+areaCode+"&sigunguCode="+sigunguCode+"&listYN="+listYN
url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content,'html.parser')
title_list = bs_obj.findAll('title')
print(title_list)
# print(bs_obj)