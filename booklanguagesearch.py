import time
import csv
def languager():
    print(" "*50+"Language portal is open now please enter the language ")
    file = open("stock.txt","rt")
    f = csv.reader(file)
    language = []
    mainList = []
    book = []
    for i in f:
        if i != []:
            mainList.append(i)
    for i in range(len(mainList)):
        language.append(mainList[i][4])
        book.append(mainList[i][0])
    count = 0
    languagename = input(" "*50+"Enter the language here : ")
    print(" "*50+"We re just finding that it is available or not ")
    print(".."*83)
    time.sleep(3)
    print(" "*50+"language"+"     "+"Book")
    print(" "*50+"If it is in store or not, we are just configuring...........")
    time.sleep(3)
    for i in range(len(language)):
        if languagename!="all":
            if languagename==language[i]:
                if count==0:
                    print(" "*50+"We had find the book that you needed : "+languagename)
                count+=1
                print(" "*50+language[i]+"     "+book[i])
        else:
            print(" "*50+language[i] + "  |||||   " + book[i])
    if count<=0:
        print(" "*50+"Book is not present in this store")


            














