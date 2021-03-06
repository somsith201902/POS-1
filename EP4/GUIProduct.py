#GUIcalculator.py
from tkinter import *
from tkinter import ttk #theme for lable and entry
from CRUD import *
import csv


from datetime import datetime
font_title = ("arial", 22)
font_result= ("arial", 14)
GUI = Tk()
GUI.title("pricetice4")
GUI.geometry('1050x750+450+25') 

## TAB 
from tkinter.ttk import Notebook

Tab = Notebook(GUI)
F1 = Frame(Tab)
F2 = Frame(Tab)
F4 = Frame(Tab)
F3 = Frame(Tab)

Tab.add(F1, text="Sales")
Tab.add(F2, text="Add Products")
Tab.add(F3, text="All Products")
Tab.add(F4, text="History")
Tab.pack(fill=BOTH, expand=1)









############## Add Product (Tab) ###################

## Row0
L0 = ttk.Label(F2, text='Barcode', font=font_title)
L0.pack(pady=10) # for c cen ter aglin
v_barcode = StringVar() 
B0 = ttk.Entry(F2, textvariable=v_barcode) 
B0.pack()

## Row1
L1 = ttk.Label(F2, text='Product', font=font_title)
L1.pack(pady=10) # for c center aglin
v_product = StringVar() #String var คือกล่อง ใส่ตัวแปรที่เปี่ยนแปลงได้
B1 = ttk.Entry(F2, textvariable=v_product) 
B1.pack()

## Row2
L2 = ttk.Label(F2, text='Price', font=font_title)
L2.pack(pady=10) # for c center aglin
v_price = StringVar() #box2 
B2 = ttk.Entry(F2, textvariable=v_price) 
B2.pack()

## Row3
L3 = ttk.Label(F2, text='Amount', font=font_title)
L3.pack(pady=10) # for c center aglin
v_amount = StringVar() #box3
B3 = ttk.Entry(F2, textvariable=v_amount) 
B3.pack()
#button

def Write(listdata): 
    print("Writing...")
    with open('EP5\data.csv', 'a', newline='', encoding='UTF-8') as file:
	    f = csv.writer(file)
	    f.writerow(listdata)
    print("Finished")

def Calc():
    bc = v_barcode.get()
    pd = v_product.get() # .get() พนักงานเปีดกล่องดุว่ามีอะไรบ้างในนั้น
    pc = v_price.get()
    am = v_amount.get()
    date = datetime.now().strftime("%a %d/%m/%y %I:%H:%M %p ")
    cal = int(pc) * int(am)
    Write([bc,pd,pc,am,cal,date])
    text_result = f'สินค้า : {pd}, ลาคา : {pc}, จำนวน : {am}'
    text_result = text_result + f'\nรวมคา {cal}\n{date} '
    v_result.set(text_result)
    apB1.insert('', 'end', value=[bc,pd,pc,am,cal,date])



But_1 = ttk.Button(F2, text='Add Product',command=Calc)
But_1.pack(ipadx=10, ipady=5, pady = 20)
#result
v_result = StringVar()
v_result.set("---- Status ----")
R1 = ttk.Label(F2, textvariable=v_result,font=font_result) 
R1.pack()



############### All Product (Tab) ###############

#function

apL1 = Label(F3, text="All Products", font=font_title)
apL1.pack()

## Treeview()##

header = ['Barcode','Products','Price','Amount','Total','Last Update']
w = [70,150,70,70,70,160]

apB1 = ttk.Treeview(F3, height=10, column=header, show="headings")
apB1.pack()
for hd in header:
    apB1.heading(hd, text=hd)
for hd,w in zip(header,w):
    apB1.column(hd, width=w)

## insert data ##
alldata = ReadData('EP5/data.csv')
for dt in alldata:
    apB1.insert('', 'end', value=dt)

############## Sales (Tab) ###################

BF1 = Frame(F1)
BF1.place(x=30, y=30)

def Insert_Sales(i):
    dt = current_stock[i] 
    dt[3] = 1 
    dt[4] = dt[3] * int(dt[2])
    current_table.insert('', 'end', value=dt)

current_table={}
current_stock = ReadData('EP5/data.csv')
row_count = 0

#### Button
for i in range(len(current_stock)):
    print(current_stock)
    B1 = ttk.Button(BF1,text=current_stock[i][1],command=lambda x=i : Insert_Sales(x))
    if i % 3 == 0:        
        B1.grid(row=row_count, column=0,ipady=10,padx=20,pady=5)
    elif i % 3 == 1:        
        B1.grid(row=row_count, column=1, ipady=10, padx=5, pady=5)
    elif i % 3 == 2:
        B1.grid(row=row_count, column=2, ipady=10, padx=20, pady=5)   
        row_count += 1 
       
    # B1.place(x=50, y=50 * (i+0.5))
    

## reference
ref = Label(F1, text="Ref :")
ref.place(x=430, y=5)

v_REF = StringVar()
v_REF.set("______ Reference ______")
REF = Label(F1, textvariable=v_REF)
REF.place(x=455, y=5)
## Treeview()##

header = ['Barcode','Products','Price','Amount','Total','Last Update']
w = [70,150,70,70,70,160]

current_table = ttk.Treeview(F1, height=10, column=header, show="headings")
current_table.place(x=430, y=30)

for hd in header:
    current_table.heading(hd, text=hd)
for hd,w in zip(header,w):
    current_table.column(hd, width=w)


GUI.mainloop()