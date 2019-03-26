import os
import sys
import urllib.request
import requests
import json
from urllib.parse import urlparse

def get_api_result(searchStr,display,start):


    url = "https://openapi.naver.com/v1/search/blog?query=" + searchStr + "&display=" + str(display) + "&start="+str(start)
    headers = {"X-Naver-Client-Id": "W59eZXdCzfT02QoECC8H", "X-Naver-Client-Secret": "yPdYKhPYXD"}
    request = urllib.request.Request(url)

    result = requests.get(urlparse(url).geturl(), headers=headers)
    json_obj = result.json()
    return json_obj

def call_and_print(searchStr,page):
    display =100
    json_obj = get_api_result(searchStr,display,page)
    for item in json_obj['items']:
        print(item)

searchStr = '고양이'
for i in range(1,1000,100):
    call_and_print(searchStr,i)
# call_and_print(searchStr,101)





