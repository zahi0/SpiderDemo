from bs4 import BeautifulSoup
import requests,pymongo

# 更新地区

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_info = ganji['item_info']

for item in item_info.find():
    wb_data = requests.get(item['url'])
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    area = soup.select('ul.det-infor > li > a')
    areas=[]
    for i in area:
        areas.append(i.get_text())
    result = item_info.update_one(
        {'_id': item['_id']},
        {
            '$set': {'areas': areas}
        }
    )