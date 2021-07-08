import csv
import time
def read():
    
   
    print(" "*50+" we are just confiaaaaguring the setup ")
    print(" "*50+"Loading..........")
    time.sleep(2)
    f = open("Stock.txt","rt")
    f1 = csv.reader(f)
    print(" "*50+"We are loading your data")
    print(" "*50+"loading..........")
    time.sleep(3)
    for i in f1:
        if i!=[]:
            print(i)

def reunion():
   
    mainList= []
    f = open("Stock.txt","rt")
    f1 = csv.reader(f)
    for i in f1:
        if i!=[]:
            mainList.append(i)
    k = 0
    print(" "*50+"This data will be shown by indexing format........")
    time.sleep(1)
    for i in mainList:
        k+=1
        print(k,end=" ")
        for j in i:
            print(j,end="  ")
        print()
