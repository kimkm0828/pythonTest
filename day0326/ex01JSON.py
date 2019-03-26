import json

str = '[{"name":"홍길","age":"32"}]'
print(str)
print(type(str))

r = json.loads(str)
print(r)
print(type(r))

str2 = {"name":"홍길","age":"32"}
print(str2)
print(type(str2))