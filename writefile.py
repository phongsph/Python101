
# write file to txt
import csv


def writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('บรรทัดที่ 1')


# write file แบบขึ้นบรรทัดใหม่
def adddata(text):
    with open('add-data.txt','a',encoding='utf-8')as file:
        file.write(text + '\n')

def readdata():
    with open('add-data.txt',encoding='utf-8')as file:
        #data = file.readlines() # export ออกมาเป็น list
        data = file.read() # export ออกมาปกติ
        print(data)
        

readdata()

#adddata('ซื้อยางลบ 35 บาท')
#adddata('ซื้อน้ำ 20 บาท')

