import json
from datetime import datetime

file = open(r"C:\Users\Anbar\Desktop\MOCK_DATA.json", "r")
data = json.load(file)
print('ok')
print(type(data))
alternative = []
for item in data:
    item['price'] = float(item['price'][1:])
    #item['last_update'] = datetime.strptime(item['last_update'], '%Y-%m-%d')
    item['collection'] = int(item['collection'])
    item['promotion'] = int(item['promotion'])
    item['promotion'] = tuple(range(item['promotion']))
    dic = {"model":"Store.Product",
           "pk": data.index(item)+1,
           "fields": item}
    alternative.append(dic)

save_path = r"C:\Users\Anbar\Desktop\product_data.json"




## Save result in a new file
with open(save_path, 'w') as outfile:
    json.dump(alternative, outfile)
    
    


