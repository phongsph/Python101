import csv
'''
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #data;ist =['pen','pencil','erasor']


data = ["ขนม",20,'บาท']
writecsv(data)
'''

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file writer
        data= list(fr)
    return data

data = readcsv()
print(data)
