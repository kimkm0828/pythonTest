

def getParking():
    import requests
    import json

    url = 'http://openapi.seoul.go.kr:8088/66646952616b696d3333576154424a/json/GetParkInfo/1/900/'

    r = requests.get(url).text
    list = json.loads(r)
    total = int(list['GetParkInfo']['list_total_count'])
    Plist = []
    for start in range(1, total, 1000):
        end = start + 1000 - 1
        if end > total:
            end = total
        subUrl = 'http://openapi.seoul.go.kr:8088/66646952616b696d3333576154424a/json/GetParkInfo/' + str(
            start) + '/' + str(end) + '/'

        data = json.loads(requests.get(subUrl).text)
        row = data['GetParkInfo']['row']

        for item in row:
            if 'PARKING_NAME' in item:
                name = item['PARKING_NAME']
                addr = item['ADDR']
                LAT = item['LAT']
                LNG = item['LNG']
                Plist.append({'name': name, 'addr': addr, 'LAT': LAT, 'LNG': LNG})

    return Plist


def getPharmacy():
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

    paramset = "serviceKey=" + serviceKey + "&Q0=" + Q0 + "&QRD=" + QRD + "&pageNo=" + pageNo + "&startPage=" + startPage + "&numOfRows=" + numOfRows

    url = endpoint + paramset
    print(url)
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')
    items = bs_obj.findAll('item')

    listN = []

    for item in items:
        tagged_item = item.find("dutytime6s")
        tagged_item2 = item.find("dutytime7s")
        tagged_item3 = item.find("dutytime8s")
        if (tagged_item != None and tagged_item2 != None and tagged_item3 != None):
            name = item.find("dutyname").text
            addr = item.find("dutyaddr").text
            lat = item.find('wgs84lat').text
            lon = item.find('wgs84lon').text
            # print(name, lat, lon)
            listN.append({'name': name, 'addr': addr, 'lat': lat, 'lon': lon})
    return listN



def getEos():
    import requests
    from bs4 import BeautifulSoup
    rlist = []
    url = 'https://bp.eosgo.io/'
    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, 'html.parser')
    itemList = bs_obj.findAll('div', {"class": "lf-item"})

    #               해야할일            포문 돌리는건 똑같음
    hrefs = [item.find("a")['href'] for item in itemList]  # 위의 4줄이 1줄로 줄어듬

    for h in hrefs:
        r = requests.get(h)
        obj = BeautifulSoup(r.content, 'html.parser')
        profile_name = obj.find("div", {'class': 'profile-name'})
        title = profile_name.find("h1").text

        cb = obj.find("div", {"class": "cover-buttons"})
        location = cb.find('span', {'class': 'button-label'}).text
        website = cb.find('a')['href']

        rlist.append({"title": title, "location": location, "website": website})
    return rlist


def getNowNews():
    import urllib.request
    import bs4

    rList = []

    url = 'https://news.naver.com/'
    html = urllib.request.urlopen(url)
    obj = bs4.BeautifulSoup(html, "html.parser")
    newsList = obj.findAll("div", {"class": "newsnow_tx_inner"})
    for news in newsList:
        a = news.find("a")
        url = a["href"]
        title = news.find('strong').text
        rList.append({"title":title,"url":url})
    return rList



