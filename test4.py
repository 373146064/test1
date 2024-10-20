import pymongo

client=pymongo.MongoClient("localhost",27017)
mydb=client["testdb"]
mycol=mydb['sites']

myquery={"name":{"$regex":"^F"}}

newvalues={"$set":{"alexa":"123"}}
mycol.update_one(myquery,newvalues)
print("文档已修改")
for x in mycol.find():
    print(x)

