json_obj = {"name":"홍길동",
            "age":"32",
            "where":"역삼동",
            "phone_number":"010-3588-0000",
            "friends":[
                        {"name":"강감찬","age":"20"},
                        {"name":"이순신","age":"24"}
                        ]
            }
print(json_obj)
print(json_obj['name'])
print(json_obj['phone_number'])
print(json_obj['friends'])
friends = json_obj['friends']

for friend in friends:
    print(friend['name'])