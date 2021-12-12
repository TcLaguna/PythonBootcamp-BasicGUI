# readcsv.py
# writecsv.py

import csv
from tkinter.constants import N
# data = ['Time', 10, 500]          # บรรทัดนี้กำหนดค่า data หลอกโปรแกรม

def writecsv(data):                 # กำหนดฟังก์ชั่น csv พิมพ์ข้อความลงในไฟล์ data.csv
    with open('data.csv','a',newline='',encoding='utf-8') as file:   # 'a' = พิมพ์ต่อจากของเดิม / encoding='utf-8' เพื่อให้แสดงผลภาษาไทยได้ตอน Run
        fw = csv.writer(file)       # fw = file writer
        fw.writerow(data)           # ให้ file writer เขียนข้อมูลของ data ลงไปในไฟล์
    print('ถูกขายแล้ว')				  # แสดงข้อความเฉยๆ


def readcsv():                      # กำหนดฟังก์ชั่น readcsv สำหรับอ่านข้อมูล
    with open('data.csv',newline='',encoding='utf-8') as file:    # สั่งเปิดไฟล์ data.csv / encoding='utf-8' เพื่อให้แสดงผลภาษาไทยได้ตอน Run
        fr = csv.reader(file)       # fw = file reader
        #print(list(fr))            # ให้ file reader แสดงข้อมูลทั้งหมดออกมา เป็น string
        data = list(fr)             # ให้ data เก็บค่าที่อ่านได้ทั้งหมดในไฟล์
    return data                     # ส่งข้อมูลของ data ออกจาก readcsv  ต้องใส่ทุกครั้ง ไม่งั้นข้อมูลออกไปไม่ได้

result = readcsv()                  # กำหนดให้ result ใช้งานฟังก์ชั่น readcsv
print(result)                       # แสดงข้อมูลของ data ทั้งหมดออกมา
print(result[6][1])                 # แสดงข้อมูลของ data แถวที่7 คอลัมม์ที่2
print(float(result[6][1])*100)      # แสดงข้อมูลของ data แถวที่7 คอลัมม์ที่2 เป็นตัวเลข และนำไปคูณด้วย 100


#############################################################################
sumlist_quan = []                                   # กำหนดให้ sumlist_quan เป็นกล่องเก็บข้อมูล
for d in result:                                    # กำหนด d วนลูป ฟังก์ชั่น readcsv ตรวจดูข้อมูลทั้งหมดในไฟล์
    sumlist_quan.append(float(d[1]))                # สั่งให้ sumlist_quan เก็บข้อมูลเป็น float ของ คอลัมม์ที่2 ของทุกแถว
print (sumlist_quan, sum(sumlist_quan))             # แสดงค่าของ sumlist_quan และ ผลรวมทั้งหมดใน sumlist_quan
#############################################################################
sumlist_quan2 = [float(d[1]) for d in result]       # วิธีเขียนอีกแบบ ***   กำหนดให้ sumlist_quan เป็นกล่องเก็บข้อมูล float ของ คอลัมม์ที่2 ของทุกแถว โดยใช้ฟังก์ชั่น readcsv
print (sumlist_quan2, sum(sumlist_quan2))           # แสดงค่าของ sumlist_quan และ ผลรวมทั้งหมดใน sumlist_quan
#############################################################################
sumquan = sum([float(d[1]) for d in result])        # กำหนดให้ sumquan เป็นกล่องเก็บข้อมูล ผลรวม ของ float ของ คอลัมม์ที่2 ของทุกแถว โดยใช้ฟังก์ชั่น readcsv
print (sumquan)                                     # แสดงค่าของ sumquan
#############################################################################

def sumdata():                                      # กำหนดฟังก์ชั่น sumdata สำหรับรวมค่าข้อมูล
    result = readcsv()                              # กำหนดให้ result ใช้งานฟังก์ชั่น readcsv
    sumlist_quan = []                               # กำหนดให้ sumlist_quan เป็นกล่องเก็บข้อมูล
    sumlist_total = []                              # กำหนดให้ sumlist_total เป็นกล่องเก็บข้อมูล
    for d in result:                                # กำหนด d วนลูป ฟังก์ชั่น readcsv ตรวจดูข้อมูลทั้งหมดในไฟล์
        sumlist_quan.append(float(d[1]))            # สั่งให้ sumlist_quan เก็บข้อมูลเป็น float ของ คอลัมม์ที่2 ของทุกแถว
        sumlist_total.append(float(d[2]))           # สั่งให้ sumlist_total เก็บข้อมูลเป็น float ของ คอลัมม์ที่3 ของทุกแถว
    sumquan = sum(sumlist_quan)                     # กำหนดให้ sumquan เป็นผลรวมทั้งหมดใน sumlist_quan
    sumtotal = sum(sumlist_total)                   # กำหนดให้ sumquan เป็นผลรวมทั้งหมดใน sumlist_quan
    return (sumquan,sumtotal)                       # ส่งข้อมูลของ sumquan และ sumtotal ออกจาก sumdata


