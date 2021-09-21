# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:23:30 2021

@author: 米特

註解control1
"""

import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost', 27050)

db = conn['data']   #假定名為test的db已經存在
db_admin = conn['admin']    #command的執行必須通過名為admin的db才能進行
#test(db)下創建data(collections)
col_data = db["test"]

#匯50筆資料進去
#for i in range(1, 50000):
  # col_data.insert_one({'bookId':i, 'value':(i*200)}) #插入測試資料，必須在分片之前保證shard key的存在，本例中為_id

db_admin.command('enablesharding', 'data')        #確認目標db的sharding功能開啟
db_admin.command('shardcollection', 'data.test', key = {'mid':'hashed'},chumk={"numInitialChunks" : 4})    #指定目標collection和對應的shard key


conn.close()