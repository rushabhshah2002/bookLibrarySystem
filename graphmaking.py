import matplotlib.pyplot as plt
import time
import csv
def graph():
    file = open("business1.txt","rt")
    f1 =  csv.reader(file)
    mainList = []
    for i in f1:
        if i!=[]:
            mainList.append(i)
    price = []
    days = []
    print(" "*50+"If you want  to make month wise or year wise ")
    c = input(" "*50+"[month] [year] choose : ")
    if c=="month":
        for i in range(len(mainList)):
            price.append(mainList[i][2])
            days.append(mainList[i][6])
        month = int(input(" "*50+"please enter the mont in integer form : "))
        monthly = []
        monk = []
        totalrupees1 = []
        for i in range(1,13):
            if i==int(month):
                for  n in range(1,32):
                    monk.append(n)
                    monthy = []
                    totalrupees = []
                    for j in range(len(days)):
                        if int(days[j])==n :
                            count = 0
                            count+=1
                            monthy.append(count)
                            totalrupees.append(int(price[j]))
                    totalrupees1.append(sum(totalrupees))
                    monthly.append(sum(monthy))
        time.sleep(1)
        print(" "*50+" [sell] [totalamount] ")
        l = input(" Enter what you want to see if you want to see as no.of sell of book i or total amount that you get in that month ")
        if l=="sell":
            jkl = ["January","february","march","april","june","july","august","september","october","november","december"]
            plt.plot(monk,monthly)
            plt.xlabel("no. of days")
            plt.ylabel("sells on that day")
            plt.title("This is the data of " +str(l[month]))
            plt.show()
        if l=="totalamount":
            jkl = ["January", "february", "march", "april", "june", "july", "august", "september", "october","november", "december"]
            plt.plot( monk , totalrupees1)
            plt.xlabel("no. of days")
            plt.ylabel("sells on that day")
            plt.title("This is the data of month  " + str(l[month]))
            plt.show()
    if c=="year":
        d = int(input(" "*50+"Enter the year that you want to "))
        year = []
        price =[]
        pricely = []
        month =[]
        yearly =[]
        yearcount = []
        for i in range(len(mainList)):
            price.append(mainList[i][2])
            year.append(mainList[i][7])
            month.append(mainList[i][6])
            pricecount = []
        for k in range(1,12+1):
            yearly.append(k)
            count2 = 0
            count1 = 0
            for l in range(len(year)):
                if k==int(month[l]) and int(year[l])==d:
                    count1+=1
                    count2+=int(price[l])
            yearcount.append(count1)
            pricecount.append(count2)

        print(" "*50+"[sell] [totalamount] ")
        l = input(" "*50+" Enter what you want to see in graph [no.of book sell vs month ] than write sell else write totalamount to find total income that youb had earned in this year ")
        if l == "sell":
            plt.plot(yearly, yearcount)
            plt.xlabel("no. of month")
            plt.ylabel("sells on that day")
            plt.title("This is the data of " + str(int(d)))
            plt.show()
        if l == "totalamount":
            plt.plot(yearly, pricecount)
            plt.xlabel("no. of month")
            plt.ylabel("sells on that day")
            plt.title("This is the data of   " + str(int(d)))
            plt.show()

 













