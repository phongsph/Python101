from tkinter import *
from tkinter import ttk  #theme of tk
from tkinter import messagebox
import csv
from datetime import datetime
import math


GUI = Tk() #หน้าจอหลัก
GUI.title('PROGRAM CONVERT NUMBER') #ใส่ชื่อโปรแกรม
GUI.geometry('500x400')

L1 = Label(GUI,text = 'Convert Number and Save TO CSV',font=('Angsana New',25),fg='hot pink')
L1.place(x=50,y=20)

##### CSV WRITE 
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #data;ist =['pen','pencil','erasor']


##########SECTION RIGHT##########
LF1 =ttk.LabelFrame(GUI,text='Enter Decemal Number')# ทำเฟรมใส่ค่า1
LF1.place(x=100,y=70) #กำหนดตำแหน่งเฟรม

LF2 =ttk.LabelFrame(GUI,text='Binary Number')# ทำเฟรมแสดงค่า2
LF2.place(x=100,y=200) #กำหนดตำแหน่งเฟรม

LF3 =ttk.LabelFrame(GUI,text='Hex Number')# ทำเฟรมแสดงค่า2
LF3.place(x=100,y=290) #กำหนดตำแหน่งเฟรม


v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui

E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',15),foreground='red')#ทำช่องกรอกข้อมูล
E1.pack(ipadx=20,ipady=10) #กำหนดขนาด entry

E2 = ttk.Entry(LF2,font=('Angsana New',15),foreground='light sky blue')#ทำช่องกรอกข้อมูล
E2.pack(ipadx=20,ipady=10) #กำหนดขนาด entry

E3 = ttk.Entry(LF3,font=('Angsana New',15),foreground='light sky blue')#ทำช่องกรอกข้อมูล
E3.pack(ipadx=20,ipady=10) #กำหนดขนาด entry

###### DEF SAVE DATA #########

def Savedata():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')#ดึงข้อมูล datetime
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v-data 
    intdata = int(data)
    bindata = bin(intdata)
    hexdata = hex(intdata)
    E2.delete(0, '')
    E2.insert(0, bindata)
    E3.delete(0, '')
    E3.insert(0, hexdata)
    text = [t,'DEC=',data,'BIN=',bindata,'HEX=',hexdata]  # t = [datetime,ข้อมูลที่ทำการกรอก]
    writecsv(text) #บัญทึกค่า text
    v_data.set('') # เครียข้อมูลในช่องกรอก

##### สร้างปุ่ม save #######

B4 = ttk.Button(LF1,text='save and convert data',command=Savedata) #ทำปุ่มให้ save data
B4.pack(ipadx=20,ipady=10)#กำหนดขนาดbuttom

#######################


GUI.mainloop()