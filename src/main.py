from multiprocessing import Pool
from src.channel_extact  import channel_list
from src.pages_parsing   import get_links_from,get_item_info
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

def get_rest_of_url():
    db_urls = [item['url'] for item in url_list.find()]  # 用列表解析式装入所有要爬取的链接
    index_urls = [item['url'] for item in item_info.find()]  # 所引出详情信息数据库中所有的现存的 url 字段
    x = set(db_urls)  # 转换成集合的数据结构
    y = set(index_urls)
    rest_of_urls = x - y
    return rest_of_urls

if __name__ == '__main__':
    pool = Pool()

    # 爬取每个详情页的链接。done!
    # pool.map(get_links_from,channel_list.split())

    # 从数据库中取出url放进spider2里
    # urls=[]
    # for item in url_list.find():
    #     urls.append(item['url'])
    # pool.map(get_item_info,urls)

    # 中断后重新运行
    # pool.map(get_item_info,get_rest_of_url())