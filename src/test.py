import pymongo
from bs4 import BeautifulSoup
import requests

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']

# url_list.remove()
# 删除所有

# 更新数据库，补全URL
for item in url_list.find():
    if 'http' in item['url']:
        pass
    else:
        result = url_list.update_one(
            {'_id': item['_id']},
            {
                '$set': {'url': 'http:'+item['url']}
            }
        )
