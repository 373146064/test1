import pymongo

myclient=pymongo.MongoClient("localhost",27017)
mydb=myclient["testdb"]
mycol=mydb['sites']


#delete 删除文档
'''myquery={"name":"Taobao"}
mycol.delete_one(myquery)


for x in mycol.find():
    print(x)'''

#mycol.delete_many({})  {}传入的是一个空的查询对象 删除集合中的所有文档



#drop() 删除集合