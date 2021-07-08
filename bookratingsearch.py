import time
import csv
def rating():
    mainList = []
    f = open("Stock.txt", "rt")
    f1 = csv.reader(f)
    for i in f1:
        if i != []:
            mainList.append(i)
    rate = []
    book = []
    stock = []
    edition = []
    price = []
    author = []
    count = 0
    for i in range(len(mainList)):
        price.append(mainList[i][3])
        book.append(mainList[i][0])
        stock.append(mainList[i][2])
        edition.append(mainList[i][7])
        rate.append(mainList[i][5])
        author.append(mainList[i][1])
        averagerate = 0
    for i in range(len(price)):
        averagerate+=float(rate[i])
    averagerate = averagerate /len(rate)
    print(" "*50+"[particular] [all]")
    asking  = input(" "*50+"Enter from above here ")
    if asking == "all":
        print(" "*50+"Here is your data configuration loading............")
        time.sleep(1)
        print(" "*50+"book           rating")
        for i in range(len(mainList)):
            print(book[i]+"     "+rate[i])
        print(" "*50+"average rating of all book availble in this store is ",averagerate)
    elif asking == "particular":
        print(" "*50+"Here is your data configuration loading ......")
        time.sleep(1)
        count = 0
        d = 0
        bookname= input(" "*50+"Enter author name :")
        for i in range(len(mainList)):
            if bookname==mainList[i][0]:
                count += 1
                if count == 1:
                    print(" "*50+"book           rating")
                print(" "*50+author[i]+"||   rate "+rate[i]+"||    edition "+edition[i])
                d +=float(rate[i])
        if count!=0:
            avar = d/count
            print(" "*50+"Average rating of this book is " + str(avar))

        if count==0:
            print(" "*50+"Not a single book can be found of this name")
    else:
        print(" "*50+" You had not written properly what you want to find ")
        return rating()









