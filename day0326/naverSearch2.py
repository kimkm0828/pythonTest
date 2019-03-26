import os
import sys
import urllib.request
import requests
import json
from urllib.parse import urlparse

searchStr = '고양이'

url = "https://openapi.naver.com/v1/search/blog?query=" + searchStr
headers = {"X-Naver-Client-Id":"W59eZXdCzfT02QoECC8H","X-Naver-Client-Secret":"yPdYKhPYXD"}
request = urllib.request.Request(url)

result = requests.get(urlparse(url).geturl(),headers=headers)
json_obj = result.json()
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['items'])



