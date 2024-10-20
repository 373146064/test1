import pymongo

client=pymongo.MongoClient('localhost',27017)
mybase=client["testdb"]
mycol=mybase["sites_2"]


mylist=[{"_id":1,"name":"lihua","age":"100", "address": "Google 搜索"},
        {"_id": 2, "name": "Facebook", "address": "脸书"},
        {"_id": 3, "name": "Taobao", "address": "淘宝"},
        {"_id": 4, "name": "Zhihu", "address": "知乎"}
        ]
x=mycol.insert_many(mylist)
print(x)