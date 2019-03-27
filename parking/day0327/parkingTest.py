# 66646952616b696d3333576154424a

import requests
import json

url = 'http://openapi.seoul.go.kr:8088/66646952616b696d3333576154424a/json/GetParkInfo/1/900/'

r = requests.get(url).text
list = json.loads(r)
total = int(list['GetParkInfo']['list_total_count'])
Plist = []
for start in range(1,total,1000):
    end = start+1000-1
    if end > total:
        end = total
    subUrl = 'http://openapi.seoul.go.kr:8088/66646952616b696d3333576154424a/json/GetParkInfo/'+str(start)+'/'+str(end)+'/'

    data = json.loads( requests.get(subUrl).text )
    row = data['GetParkInfo']['row']

    for item in row:
        if 'PARKING_NAME' in item:
            name = item['PARKING_NAME']
            addr = item['ADDR']
            LAT = item['LAT']
            LNG = item['LNG']
            Plist.append({'name': name, 'addr': addr, 'LAT': LAT, 'LNG': LNG})

print(len(Plist))