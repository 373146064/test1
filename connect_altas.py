import pymongo

client=pymongo.MongoClient('mongodb://cluster0-shard-00-02.tcnha.mongodb.net:27017/')

mydatadb=client["testdb"]
mycol=mydatadb["sites1"]

list={'name':"Taobao","alexa":"100","url":"https://www.taobao.com"}

x=mycol.insert_one(list)

print(x)

