from bs4 import BeautifulSoup
import requests,pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

# spider—1
def get_links_from(channel):
    full_urls=[channel+'o{}'.format(str(i)) for i in range(1,20)]
    url_set=set()
    for full_url in full_urls:
        wb_data=requests.get(full_url)
        soup=BeautifulSoup(wb_data.text,'lxml')
        links=soup.select('#infolist > div.infocon > table > tbody > tr > td.t > a')
        for link in links:
            href=link.get('href')
            if len(href)<=100:
                url_set.add(href)
            else:
                pass
    for item in url_set:
        url_list.insert_one({'url': item})
    print('done!')

# spider—2
def get_item_info(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if soup.select('p.error-tips1'):
        data = {
            'title': None,
            'date': None,
            'price': None,
            'areas': None,
            'phone': None,
            'url': url
        }
    else:
        title=soup.select('h1.title-name')
        date=soup.select('i.pr-5')
        price=soup.select('i.f22.fc-orange.f-type')
        area=soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(2)')
        phone=soup.select('span.phoneNum-style')
        data={
            'title':title[0].text,
            'date':list(date[0].stripped_strings),
            'price':price[0].text if soup.find_all('i.f22.fc-orange.f-type') else None,
            'areas':list(area[0].stripped_strings),
            'phone':list(phone[0].stripped_strings),
            'url':url
        }
    item_info.insert_one(data)
    print('done!')