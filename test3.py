import pymongo

client=pymongo.MongoClient("localhost",27017)
mybase=client["testdb"]
mycol=mybase["sites"]


'''x=mycol.find_one()
print(x)

for x in mycol.find():
    print(x)


for x in mycol.find({},{"_id":0,"name":1,"alexa":1}):
    print(x)

for x in mycol.find({},{"name":0}):
    print(x)
#除了 _id，不能在一个对象中同时指定 0 和 1，即要么只能全是0，全是1，指定的参数有0有1就报错


#   根据指定条件查询
myquery={"name":"Google"}
mydoc=mycol.find(myquery)#这里是查找name为Google的文档列表，是列表所以不是单独一个文档，要用find
for x in mydoc:
    print(x)

#  高级查询
myquery2={"name":{"$gt":"H"}}#$gt 大于    $lt 小于
mydoc2=mycol.find(myquery2)
for x in mydoc2:
    print(x)

# 使用正则表达式查询
myquery3={"name":{"$regex":"^z"}}
mydoc3=mycol.find(myquery3)
for x in mydoc3:
    print(x)


myresult=mycol.find().limit(3)
for x in myresult:
    print(x)
'''

mydoc4=mycol.find().sort("alexa",-1)#加-1就是倒序
for x in mydoc4:
    print(x)



