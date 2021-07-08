import time
import csv
def price():
    print(" "*50+"[particular] [all] ")
    asking = input(" "*50+"Enter the data from above part ")
    print(" "*50+"We are just configuring............")
    time.sleep(2)
    mainList = []
    f = open("Stock.txt", "rt")
    f1 = csv.reader(f)
    for i in f1:
        if i != []:
            mainList.append(i)
    price = []
    book = []
    stock = []
    edition = []
    count = 0
    for i in range(len(mainList)):
        price.append(mainList[i][3])
        book.append(mainList[i][0])
        stock.append(mainList[i][2])
        edition.append(mainList[i][7])
    if asking =="all":
        price1 = int(input(" "*50+"Enter your first range :"))
        price2 = int(input(" "*50+"Enter your second range :"))
        if price1 > price2:
            price2, price1 = price1, price2
        for i in range(len(price)):
            if price1<=int(price[i])<=price2:
                count+=1
                if count==0:
                    print(" "*50+"book"+"      "+"price")
                print(" "*50+"book    "+book[i]+"    ||  price  "+price[i])
        if count<=0:
            print(" "*50+"The range that you enter it is not present in this book store")
    elif asking =="particular":
        bookname = input(" "*50+"Please enter the book name ")
        count1 = 0
        for i in range(len(mainList)):
            if bookname ==book[i]:
                count1+=1
                if count1==1:
                    time.sleep(1)
                    print(" "*50+"Here is your search...........")
                print(" "*50+book[i]+"    "+" edition "+edition[i]+"    "+" price "+price[i])
    else:
        print(" "*50+" You had not written properly what you want to find ")
        return price()

