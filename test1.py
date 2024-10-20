import pymongo

client=pymongo.MongoClient('localhost',27017)
database=client['testdb']    #像database,mycol这些都是代表的对象，像是一个与数据库，集合的连接


mycol=database['sites']#在testdb数据库中建立sites集合
print(mycol)
'''mydict={"name": "zhangsan", "alexa": "10000", "url": "https://www.baidu.com"}
x=mycol.insert_one(mydict)
print(x)
print(x.inserted_id)'''

mylist=[{'name':"Taobao","alexa":"100","url":"https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}]
x=mycol.insert_many(mylist)
print(x)












'''mycol_list=database.list_collection_names()
if "sites" in mycol_list:
    print("集合已存在")'''







'''dblist=client.list_database_names()  #读取MongoDB中的所有数据库
if "testdb" in dblist:
    print("数据库已存在")'''




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
'''db=client.test
print(db)
col=db.table
print(col)
col.insert_one({"name":"John",'age':23})'''