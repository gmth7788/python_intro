#!/usr/bin/python3
#coding=utf-8

import openpyxl

def read_excel(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name("Sheet1")
    for i in range(1,sheet.max_row+1):
        print(str(i))
        for j in sheet[str(i)]:
            print(j.value, end = " ")
        print("\n")

def new_excel(file, num):
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name("Sheet1")
    for i in range(2,num+1):
        sheet[str(i)]
        print(str(i))
        for j in sheet[str(i)]:
            print(j.value, end = " ")
        print("\n")
    


def str_format():
    title = ("剧名", "剩余票数", "票价", "日期")
    rec = (("凤还巢", 10, 30.16, "2019-2-5 19:30:00"),
           ("七星灯", 104, 40.52, "2019-2-7 19:30:00"),
           ("莱茵的黄金", 255, 30.16, "2019-2-6 18:00:00"),
           ("乌盆记", 3, 66.16, "2019-2-10 19:30:00"))
    sche = []
    for i in range(4):
        sche.append(zip(title, rec[i]))

    print("{:20s} {:10s} {:15s} {:20s}".format(title[0],
                                               title[1],
                                               title[2],
                                               title[3]))

    print("-"*60)
    for i in range(len(rec)):
        print("{:<20s} {:>10d} {:>10.2f} {:<20s}".format(rec[i][0],
                                                 rec[i][1],
                                                 rec[i][2],
                                                 rec[i][3]))
    

if __name__=="__main__":
    str_format()
    a = 10
    b = 20
    print(a and b)
    print(a or b)
    print(not a)

    read_excel(r"/home/yuquanlu68/aa.xlsx")
