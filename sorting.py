from datetime import datetime
import csv
def sortieday():
    formattingday = []
    book =[]
    for i in range(len(mainList)):
        formattingday.append(mainList[i][6])
        book.append(mainList[i][0])
    for i in formattingday:
        i = datetime.strptime(i,"%d/%m/%Y")
    formattingday.sort()
    print("      book"+"        "+"day/date/time")
    for i in range(len(book)):
        print(str(i+1)+"     "+str(book[i])+"       "+str(formattingday[i]))
def sortieyear():
    formattingyear= []
    book = []
    unmake = []
    for i in range( len(mainList)):
        year = list(mainList[i][6].split("/"))
        formattingyear.append(year[2])
        x = []
        x.append(year[2])
        x.append(mainList[i][0])
        unmake.append(x)
    formattingyear.sort()
    print("year"+"        "+"book ")
    for i in formattingyear:
        for j in  unmake:
            if i in j:
                print(str(j[0])+"   "+str(j[1]))
mainList = []
f = open("stock.txt", "rt")
f1 = csv.reader(f)
for i in f1:
    if i != []:
        mainList.append(i)
