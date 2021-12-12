# readjson.py

import json
def readjson():
    with open('data.json',encoding='utf-8') as file:      # เปิดไฟล์ data.json
        data = json.load(file)                          # อ่านข้อมูลในไฟล์ data.json
        print(type(data))
        print(data[0])
    return data

def writejson(data):
    jsonobject = json.dumps(data,ensure_ascii=False)        # เขียนข้อมูลลงในไฟล์ data.json
    with open('data.json','w',encoding='utf-8')as file:         # โหลด 'w' คือเขียนข้อมูลทับ
        file.write(jsonobject)


data = {'1234567':['Banana',20,50],
        '1231249':['Durian',200,4],
        '1254234':['Mango',15,40],
        '1234321':['แอปเปิ้ล',30,10]}
writejson(data)

