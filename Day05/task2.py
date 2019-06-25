# -*- coding: utf-8 -*-
from pymongo import MongoClient

# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库
db = conn.mydb

# 获取集合
collection = db.student


# 添加文档
collection.insert_many([{"name": "abc1", "age": 19, "gender": 1, "address": "北京", "isDelete": 0},
                        {"name": "abc2", "age": 19, "gender": 1, "address": "北京", "isDelete": 0}])


res = collection.find()
for row in res:
    print(row)
    print(type(row))

# 断开
conn.close()

"""
运行结果

{'_id': ObjectId('5d119920b99aa467bf03e685'), 'name': 'abc1', 'age': 19, 'gender': 1, 'address': '北京', 'isDelete': 0}
<class 'dict'>
{'_id': ObjectId('5d119920b99aa467bf03e686'), 'name': 'abc2', 'age': 19, 'gender': 1, 'address': '北京', 'isDelete': 0}
<class 'dict'>

Process finished with exit code 0

"""