import csv
import time
import cleanData
def write():
    print(" "*50+" we are just confoguring the setup ")
    print(" "*50+"Loading..........")
    time.sleep(2)
    f = open("Stock.txt","at")
    f1 = csv.writer(f)
    dataInput = int(input(" "*50+"how many data of the book that you want to enter : "))
    print(" "*50+"please enter the data comma seperately")
    print(" "*50+"plese enter data in specified format as shown below")
    print(" "*50+"Programming With Python,John Smith,25,160,English,4,3/9/2017,5")
    print(" "*50+"Write all thing in this form otherwise it will not be accepted ")
    print(" "*50+"please write data in format dd/mm/yyyy")
    for i in range(dataInput):
        d = []
        c = list(input().split(","))
        print(" "*50+"You had entered "+str(i+1)+" data")
        d=[c]
        print(c)
        f1.writerows(d)
