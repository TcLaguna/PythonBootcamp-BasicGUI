# database.py

import sqlite3

conn = sqlite3.connect('product-database.sqlite3')
c = conn.cursor()

# CREATE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history ( 
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quan REAL,
                total REAL )""")
print('Success')

def insert_transaction(data):
    # data = {'tid':'1212312121','stamp':'2021-12-21 10:20:59'...}
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']

    with conn:
        command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit()            # เซฟข้อมูล
print('inserted!')

def view_transaction():        # เรียกดูข้อมูลจาก database
    with conn:
        c.execute("SELECT * FROM transaction_history")
        data = c.fetchall()
        print(data)         # แสดงข้อมูลจาก database

# เรียกดูข้อมูลจาก database
transaction = {'tid':'0000000001',
                'stamp':'2021-12-21 11:21:59',
                'product':'ทุเรียน',
                'price':100,
                'quan':20,
                'total':2000}
#insert_transaction(transaction)     # ใส่ข้อมูลลง database
view_transaction()                  # แสดงข้อมูลจาก database
