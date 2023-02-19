from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import tkinter as tk
import math


GUI = Tk()
GUI.title('โปรแกรมคำนวน Kva หม้อแปลง 1 phase')
GUI.geometry("400x300")


L1 = Label(GUI,text = 'ใส่ค่า Kva :',font=('Angsana New',15),fg='green')
L1.place(x=20,y=30)
L2 = Label(GUI,text = 'ใส่ค่า Volt :',font=('Angsana New',15),fg='green')
L2.place(x=20,y=60)
L3 = Label(GUI,text = 'กระแส MAX :',font=('Angsana New',15),fg='green')
L3.place(x=5,y=150)
L4 = Label(GUI,text = 'V.',font=('Angsana New',15),fg='green')
L4.place(x=300,y=60)
L5 = Label(GUI,text = 'Amp.',font=('Angsana New',15),fg='green')
L5.place(x=300,y=150)

###########
def on_button_click():
    value = entry1.get()
    print("Value entered:", value)
    a = int(value)
    value1 = entry2.get()
    print("Value entered:", value1)
    b = int(value1)
    value2 = (1000*a)//b
    print("Value entered:",value2)
    entry3.delete(0, tk.END)
    entry3.insert(0, value2)
    
    #messagebox.showinfo('คำสั่ง:',value2)
    


entry1 = tk.Entry(GUI, bg='pink', fg='black')
entry1.place(x=100,y=30)
entry2 = tk.Entry(GUI, bg='pink', fg='black')
entry2.place(x=100,y=60)
entry3 = tk.Entry(GUI, bg='lightgreen', fg='black')
entry3.place(x=100,y=150)

button = tk.Button(GUI, text="คำนวณกระแส", command=on_button_click)
button.place(x=170,y=100)
###########



GUI.mainloop()
