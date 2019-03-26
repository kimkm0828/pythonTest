import json
s = '{"name":"홍길","age":"32"}'

obj = json.loads(s)
print(obj)
print(type(obj))

r = json.dumps(obj)
print(r)

# r = str(obj)
# print(r)
# print(type(r))