import pymongo,charts

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_info = ganji['item_info']
area_times=ganji['area_times']
areas=[]

for item in item_info.find():
    areas.extend(item['areas'])

area_index=list(set(areas))
area_index.remove('')
area_index.remove('近期价格走势')
area_index.sort()
post_time=[]
for i in area_index:
    post_time.append(areas.count(i))

for area, times in zip(area_index, post_time):
    data={'name':area,'data':times}
    area_times.insert_one(data)

# def data_gen(types):
#     length=0
#     if length<=len(area_index):
#         for area,times in zip(area_index,post_time):
#             data={
#                 'name':area,
#                 'data':[times],
#                 'type':types
#             }
#             yield data
#             length+=1
#
# series=[]
# for data in data_gen('column'):
#     if data['data'][0]>20:
#         series.append(data)
#
# charts.plot(series,show='inline',options=dict(title=dict(text='赶集网北京地区二手物品发帖量')))