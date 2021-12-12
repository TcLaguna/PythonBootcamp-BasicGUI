# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv

#######################################################################################################

def timestamp(thai=True):     # กำหนดฟังก์ชั่น พิมพ์วันเวลา โดยถ้าเงื่อนไขเป็นจริงให้ใช้ พ.ศ.
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543)      # แปลง ค.ศ. เป็น พ.ศ.
		stamp = stamp.strftime('%d/%m/%Y (%H:%M)')      # Thai Date
	else:
		stamp = datetime.now().strftime('%d/%m/%Y (%H:%M)')      # Engish Date
	return stamp 

def writetext(quantity,total):       # กำหนดฟังก์ชั่น พิมพ์ข้อความลงในไฟล์ data.txt
	stamp = timestamp()
	filename = 'data.txt'
	sm = sumdata()
	with open (filename, 'a',encoding='utf-8') as file:               # 'a' = พิมพ์ต่อจากของเดิม / encoding='utf-8' เพื่อให้แสดงผลภาษาไทยได้ตอน Run
		file.write('\n'+'{}   ขายทุเรียน: {} กก.   เป็นเงิน: {:,.2f} บาท   รวมขายทุเรียนได้ {} กก. เป็นเงิน {} บาท'.format(stamp,quantity,total,sm[0],sm[1]))

def writecsv(data):                  # กำหนดฟังก์ชั่น csv พิมพ์ข้อความลงในไฟล์ data.csv
    with open('data.csv','a',newline='',encoding='utf-8') as file:    # 'a' = พิมพ์ต่อจากของเดิม / encoding='utf-8' เพื่อให้แสดงผลภาษาไทยได้ตอน Run
        fw = csv.writer(file)        # fw = file writer
        fw.writerow(data)            # ให้ file writer เขียนข้อมูลของ data ลงไปในไฟล์
    print('Success!')				   # แสดงข้อความเฉยๆ

def readcsv():                      # กำหนดฟังก์ชั่น readcsv สำหรับอ่านข้อมูล
    with open('data.csv',newline='',encoding='utf-8') as file:    # สั่งเปิดไฟล์ data.csv / encoding='utf-8' เพื่อให้แสดงผลภาษาไทยได้ตอน Run
        fr = csv.reader(file)       # fw = file reader
        #print(list(fr))            # ให้ file reader แสดงข้อมูลทั้งหมดออกมา เป็น string
        data = list(fr)             # ให้ data เก็บค่าที่อ่านได้ทั้งหมดในไฟล์
    return data                     # ส่งข้อมูลของ data ออกจาก readcsv  ต้องใส่ทุกครั้ง ไม่งั้นข้อมูลออกไปไม่ได้

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

def SummaryData(event):
	# โชว์ Pop Up แจ้งเตือนขึ้นมา
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = 'จำนวนที่ขายได้ : {} กก.\nยอดขาย : {} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)


#######################################################################################################
GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของโบ๊ท')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'),fg='green')
L1.pack()    # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('Angsana New',20))
L2.pack()

v_quantity = StringVar()   # ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate(event=None):								# event=None ทำให้เรียกใช้งานฟังก์ชั่นได้ทั้ง แบบกดปุ่มบนแป้นพิมพ์ และ คลิกปุ่ม 
	quantity = v_quantity.get()
	price = 100
	print('จำนวน', float(quantity) * price)
	cal = float(quantity) * price

	data = [timestamp(thai=True), quantity, cal]          # กำหนดให้ data เป็นข้อมูล วันเวลา, นน.ทุเรียน, ราคาขาย ข้อมูลที่เขียนลงไปใน csv
	writecsv(data)										  # เขียนข้อมูล data ที่เก็บไว้ ลงไปใน data.csv  *****
	writetext(quantity,cal)								  # เขียนข้อมูล data ที่เก็บไว้ ลงไปใน data.text  *****
	
	# โชว์ Pop Up แจ้งเตือนขึ้นมา	
	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ขายทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('')       			# เคลียร์ช่องกรอกข้อมูล
	E1.focus()							# ย้าย Cursor ไปตำแหน่งของ E1


GUI.bind('<F1>',SummaryData)			# กำหนดให้เมื่อกดปุ่ม F1 จะใช้งานฟังก์ชั่น SummaryData

B1 = ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Calculate)				# กำหนดให้เมื่อกดปุ่ม Enter จะใช้งานฟังก์ชั่น Calculate
E1.focus()									# ย้าย Cursor ไปตำแหน่งของ E1

GUI.mainloop()