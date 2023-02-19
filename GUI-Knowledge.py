from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ใส่ชื่อโปรแกรม
GUI.geometry('400x300')

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')#สร้างปุ่ม
#B1.pack(ipadx=20,ipady=20) #packกำหนดปุ่มดา้่นบนสุด
#ipadx y กำหนดขนาดปุ่ม

L1 = Label(GUI,text = 'โปรแกรมบันทึกความรู้',font=('Angsana New',20),fg='green')
L1.place(x=20,y=20)
L2 = Label(GUI,text = 'คำสั่งโปรแกรม Turtle',font=('Angsana New',15),fg='blue')
L2.place(x=20,y=50)

####################
def button1():
    text = 'import turtle'
    messagebox.showinfo('คำสั่ง:', text)
    #messagebox.showwarning('เงินในบัญชี', text)
    #messagebox.showerror('เงินในบัญชี', text)

#FB1 = Frame(GUI) #คล้ายกระดาน
#FB1.place(x=20,y=60) #กำหนดตำแหน่งกระดาน
B1 = ttk.Button(GUI,text='คำสั่ง import', command=button1)#สร้างปุ่มใส่ในframและ shoe pop up
#B1.pack(ipadx=10,ipady=20) #packกำหนดปุ่มดา้่นบนสุด
B1.place(x=20,y=100) #place เป็นการกำหนดตำแหน่ง
####################
def button2():
    text = 'ใส่ตัวแปร = turtle.Pen()'
    messagebox.showinfo('คำสั่ง:',text)

B2 = ttk.Button(GUI,text='คำสั่งกำหนดตัวแปร pen', command=button2)
B2.place(x=20,y=130) #place เป็นการกำหนดตำแหน่ง
####################
def button3():
    text = 'ตัวแปร.shape("turtle")'
    messagebox.showinfo('คำสั่ง:',text)

B3 = ttk.Button(GUI,text='คำสั่งกำหนด shape', command=button3)
B3.place(x=20,y=160) #place เป็นการกำหนดตำแหน่ง
####################
def button4():
    text = 'ตัวแปร.forward(ความยาว1px.)'
    messagebox.showinfo('คำสั่ง:',text)

B4 = ttk.Button(GUI,text='คำสั่งลากเส้นเดินหน้า', command=button4)
B4.place(x=20,y=190) #place เป็นการกำหนดตำแหน่ง
####################
def button5():
    text = 'ตัวแปร.left(องศา)'
    messagebox.showinfo('คำสั่ง:',text)

B5 = ttk.Button(GUI,text='คำสั่งเลี่ยวซ้าย', command=button5)
B5.place(x=20,y=220) #place เป็นการกำหนดตำแหน่ง
####################






GUI.mainloop()
