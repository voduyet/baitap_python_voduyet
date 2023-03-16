import mysql.connector, openpyxl

myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "python")
cur = myconn.cursor()
sql = ("insert into students( masv, ho, ten, ngaysinh, toan, ly, hoa) "
+ "values (%s, %s, %s, %s, %s, %s, %s)")
# val = ("sv01", "phuong","26-03-2002", 7.1, 5.5,6.3)

wb = openpyxl.load_workbook("input.xlsx")
# print(wb.sheetnames)
ws = wb[wb.sheetnames[0]]
for i in range(12, 63):
    # print(ws.cell(row=i, column=2).value)
    val = (ws.cell(row=i, column=2).value, ws.cell(row=i, column=3).value, ws.cell(row=i, column=4).value, ws.cell(row=i, column=5).value, ws.cell(row=i, column=6).value, ws.cell(row=i, column=7).value, ws.cell(row=i, column=8).value)
    try:
        cur.execute(sql,val)
        myconn.commit()
    except:
        myconn.rollback()
# print(cur.rowcount,"record inserted!")
myconn.close()


myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "python")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
# select dữ liệu từ database
    cur.execute("SELECT * FROM sv")
# tìm nạp các hàng từ đối tượng con trỏ 
    result = cur.fetchall()
    for x in result:
        print(x); 
except:
    myconn.rollback()
    myconn.close()


import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "python")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
# cập nhật name cho bảng Employee
    # cur.execute("update students set name = 'Bảoo' where id = 10001")
    cur.execute("UPDATE students SET ho='Phan Viết',ten='Báoooo' WHERE masv='C200009'")
    myconn.commit()
except:
    myconn.rollback()
    myconn.close()

import mysql.connector
#tạo đối tượng connection
myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "", database = "python")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
# cập nhật name cho bảng Employee
    cur.execute("DELETE FROM students WHERE masv = 'C200009'")
    myconn.commit()
except:
    myconn.rollback()
    myconn.close()