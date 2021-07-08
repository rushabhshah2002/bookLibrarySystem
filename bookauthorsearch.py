import time
import csv
def author():
    print(" "*50+"[all] [particular] ")
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
    author = []
    count = 0
    for i in range(len(mainList)):
        price.append(mainList[i][3])
        book.append(mainList[i][0])
        stock.append(mainList[i][2])
        edition.append(mainList[i][7])
        author .append(mainList[i][1])
    if asking=="all":
        print(" "*50+"Here is your data configuration loading............")
        time.sleep(1)
        print(" "*50+"book     ||      rating")
        for i in range(len(mainList)):
            print(book[i] + "  ||  " + author[i])
    if asking=="particular":
        print(" "*50+"Here is your data configuration loading ......")
        time.sleep(1)
        count = 0
        d = 0
        authorname = input(" "*50+"Enter author name :")
        print(len(mainList))
        for i in range(len(mainList)):
            if authorname == mainList[i][1]:
                count += 1
                if count == 1:
                    print(" "*50+"author           book")
                print(author[i] + "||   book " + book[i]+ "||    edition " + edition[i])
        if count == 0:
            print(" "*50+"Not a single book can be found of this name")
