import requests
import json

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
r = requests.get(url)
text = bytes(r.text,'iso-8859-1').decode('utf-8')
x = json.loads(text)
for i in range(len(x)):
    print(x[i]['code'])
    print(x[i]['value'])
    print("-"*100)