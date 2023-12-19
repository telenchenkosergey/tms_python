# Прочитать сохранённый json файл и записать данные на диск в csv-файл, первой
# строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”

import json, csv

headers = ['id', 'name', 'age', 'phone_number']

with open('info.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)

with open('info.json') as json_file:
    data = json.load(json_file)

lst = []

for k, v in data.items():
    item = []
    item.append(k)
    item.append(v[0])
    item.append(v[1])
    lst.append(item)

with open('info.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for item in lst:
        writer.writerow(item)
