import csv
import time
import datetime
def detail():
    file1 = "business1.txt"
    file = "stock.txt"
    print(" "*50+"It is compulsory to fill detail of your for future purpose ")
    c = open(file1, "at")
    d = open(file, "rt")
    f1 = csv.writer(c)
    mainList = []
    count = 0
    f2 = csv.reader(d)
    print(" "*50+"Just loading........")
    time.sleep(1)
    print(" "*50+"Enter the data in the format given below ...")
    print(" "*50+"[name] [bookname] [price] [phonenumber] [e-mail] ")
    print(" "*50+"All section write in comma sepertated form  ")
    print(" "*50+"please do not enter space betwwn coma")
    print(" "*50+"Please carefull read all this instruction")
    time.sleep(2)
    det = list(input(" "*50+"Enter here all detail").strip().split(","))
    j = "@gmail.com"
    count1 = 0
    if j in det[4]:
        count += 1
    for i in f2:
        if i != []:
            mainList.append(i)

    for i in range(len(mainList)):
        print(mainList[i][0])
        if det[1] == mainList[i][0] and int(mainList[i][2]) > 0 and det[2] == mainList[i][3] and count1 > 0:
            count += 1
    if len(det[3]) == 10 and count >= 1:
        print(" "*50+"You had complete data filling form ")
        currentdate = datetime.datetime.now()
        currentmd = currentdate.strftime("%d")
        currentm = currentdate.strftime("%m")
        currenty = currentdate.strftime("%Y")
        det.append(currentmd)
        det.append(currentm)
        det.append(currenty)
        d = [det]
        print(" "*50+"Here store data will not be given to anyone ")
        f1.writerows(d)
        c.close()
    else:
        print(len(det[3]))
        if len(det[3]) != 10:
            print(" "*50+"You have to enter correct phone number ")
        if count < 1:
            print(" "*50+"You have wrong book name of something else that does not make it perfect filled form ")
        if count1 < 1:
            print(" "*50+"You had entered wrong emai Id")
        return detail()




