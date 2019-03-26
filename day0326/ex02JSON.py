import json

str = '[{"name":"홍길","age":"32"},{"name":"강감","age":"40"}]'

list = json.loads(str)
print(list)
print(type(list))